from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuration import DATABASE_URL
from api.fetch_users import fetch_and_store_users
from data_protection.masking import update_users_with_masked_phones
from data_protection.anonymization import update_users_with_anonymized_names
from data_analysis.analysis import analyze_users_data


def main():
    
    # Osa 1: Tietokannan käyttöönotto migraatioilla
    print("\n[Part 1] Database setup")
    project_dir = Path(__file__).resolve().parent
    alembic_cfg = Config(str(project_dir / "alembic.ini"))
    alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
    alembic_cfg.set_main_option("prepend_sys_path", str(project_dir))
    command.upgrade(alembic_cfg, "head")
    
    # Osa 2: Tietojen hakeminen ja tallentaminen
    print("\n[Part 2] Fetching and storing data")
    fetch_and_store_users()
    
    # Osa 3: Tiedon peittäminen
    print("\n[Part 3] Applying data protection")
    update_users_with_masked_phones()
    
    update_users_with_anonymized_names()
    
    # Osa 4: Datan analysointi
    print("\n[Part 4] Data analysis with Pandas")
    
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        analyze_users_data(session)
    


if __name__ == "__main__":
    main()
