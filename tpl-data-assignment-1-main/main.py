"""
Main script that runs the full data pipeline:
Part 1: Database setup
Part 2: Fetch and store data from API
Part 3: Apply data protection (masking and anonymization)
Part 4: Data analysis with Pandas
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuration import DATABASE_URL
from api.fetch_users import fetch_and_store_users
from data_protection.masking import update_users_with_masked_phones
from data_protection.anonymization import update_users_with_anonymized_names
from data_analysis.analysis import analyze_users_data


def main():
    print("=" * 80)
    print("DATA PIPELINE - ORCHESTRATION SCRIPT")
    print("=" * 80)
    
    # Part 1: Database Design and Migration
    print("\n[Part 1] Database setup")
    print("-" * 80)
    print("Database initialized with Alembic migrations")
    
    # Part 2: Fetch and Store Data
    print("\n[Part 2] Fetching and storing data")
    print("-" * 80)
    print("Fetching users from JSONPlaceholder API...")
    fetch_and_store_users()
    print("Data fetched and stored in database")
    
    # Part 3: Data Protection (Masking and Anonymization)
    print("\n[Part 3] Applying data protection")
    print("-" * 80)
    
    print("\n  3.1 Masking phone numbers")
    update_users_with_masked_phones()
    
    print("\n  3.2 Anonymizing names")
    update_users_with_anonymized_names()
    
    # Part 4: Data Analysis
    print("\n[Part 4] Data analysis with Pandas")
    print("-" * 80)
    print("Data analysis results:")
    
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        analyze_users_data(session)
    
    print("\n" + "=" * 80)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 80)


if __name__ == "__main__":
    main()
