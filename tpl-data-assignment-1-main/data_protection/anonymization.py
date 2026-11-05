from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.models import User
from configuration import DATABASE_URL


def anonymize_name(name: str) -> str:
    
    if not name or len(name) < 1:
        return name
    return name[0]

def get_anonymized_users():
    
    engine = create_engine(DATABASE_URL)
    
    with Session(engine) as session:
        users = session.query(User).all()
        anonymized_users = []
        
        for user in users:
            anonymized_user = {
                "id": user.id,
                "name": anonymize_name(user.name),  # Apply anonymization
                "username": user.username,
                "email": user.email,
                "city": user.city,
                "company_name": user.company_name,
                "phone": user.phone,
                "website": user.website,
            }
            anonymized_users.append(anonymized_user)
        
        return anonymized_users


def update_users_with_anonymized_names():
    
    engine = create_engine(DATABASE_URL)
    
    with Session(engine) as session:
        users = session.query(User).all()
        
        print(f"Anonymizing names for {len(users)} users...")
        print("-" * 80)
        
        for user in users:
            original_name = user.name
            user.name = anonymize_name(user.name)  # Apply anonymization
            print(f"User ID {user.id}: {original_name} → {user.name}")
        
        # Save changes to database
        session.commit()
        print("-" * 80)
        print("✓ Database updated successfully!")
        return True


def anonymize_users_in_db():
    
    anonymized_users = get_anonymized_users()
    
    print("Users with anonymized names:")
    print("-" * 80)
    for user in anonymized_users:
        print(f"ID: {user['id']}")
        print(f"  Name: {user['name']}")
        print(f"  Username: {user['username']}")
        print(f"  Email: {user['email']}")
        print(f"  Phone: {user['phone']}")
        print(f"  City: {user['city']}")
        print(f"  Company: {user['company_name']}")
        print(f"  Website: {user['website']}")
        print("-" * 80)