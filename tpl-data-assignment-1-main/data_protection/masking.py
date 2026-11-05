from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.models import User
from configuration import DATABASE_URL


def mask_phone_number(phone: str) -> str:
    
    if not phone or len(phone) < 2:
        return phone
    return '*' * (len(phone) - 2) + phone[-2:]


def get_masked_users():
    
    engine = create_engine(DATABASE_URL)
    
    with Session(engine) as session:
        users = session.query(User).all()
        masked_users = []
        
        for user in users:
            masked_user = {
                "id": user.id,
                "name": user.name,
                "username": user.username,
                "email": user.email,
                "city": user.city,
                "company_name": user.company_name,
                "phone": mask_phone_number(user.phone),  # Apply masking
                "website": user.website,
            }
            masked_users.append(masked_user)
        
        return masked_users


def update_users_with_masked_phones():
    
    engine = create_engine(DATABASE_URL)
    
    with Session(engine) as session:
        users = session.query(User).all()
        
        print(f"Masking phone numbers for {len(users)} users...")
        print("-" * 80)
        
        for user in users:
            original_phone = user.phone
            user.phone = mask_phone_number(user.phone)  # Apply masking
            print(f"User ID {user.id}: {original_phone} → {user.phone}")
        
        # Save changes to database
        session.commit()
        print("-" * 80)
        print("✓ Database updated successfully!")
        return True


def mask_users_in_db():
    
    masked_users = get_masked_users()
    
    print("Users with masked phone numbers:")
    print("-" * 80)
    for user in masked_users:
        print(f"ID: {user['id']}")
        print(f"  Name: {user['name']}")
        print(f"  Username: {user['username']}")
        print(f"  Email: {user['email']}")
        print(f"  Phone: {user['phone']}")
        print(f"  City: {user['city']}")
        print(f"  Company: {user['company_name']}")
        print(f"  Website: {user['website']}")
        print("-" * 80)

