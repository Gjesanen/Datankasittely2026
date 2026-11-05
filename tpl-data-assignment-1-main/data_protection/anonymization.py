from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.models import User
from configuration import DATABASE_URL


def anonymize_name(name: str) -> str:
    
    if not name or len(name) < 1:
        return name
    return name[0]


def update_users_with_anonymized_names():
    
    engine = create_engine(DATABASE_URL)
    
    with Session(engine) as session:
        users = session.query(User).all()
        
        for user in users:
            print(f"  {user.name} → {anonymize_name(user.name)}")
            user.name = anonymize_name(user.name)
        
        session.commit()
        print("Database updated")
