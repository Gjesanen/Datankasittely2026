from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.models import User
from configuration import DATABASE_URL


def mask_phone_number(phone: str) -> str:
    
    if not phone or len(phone) < 2:
        return phone
    return '*' * (len(phone) - 2) + phone[-2:]


def update_users_with_masked_phones():
    
    engine = create_engine(DATABASE_URL)
    
    with Session(engine) as session:
        users = session.query(User).all()
        
        for user in users:
            print(f"  {user.phone} → {mask_phone_number(user.phone)}")
            user.phone = mask_phone_number(user.phone)
        
        session.commit()
        print("Database updated")

