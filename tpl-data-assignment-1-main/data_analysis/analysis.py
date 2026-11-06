import pandas as pd
from sqlalchemy.orm import Session
from database.models import User


def analyze_users_data(session: Session) -> None:
    
    
    users = session.query(User).all()
    
    
    data = [
        {
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'email': user.email,
            'city': user.city,
            'company_name': user.company_name,
            'phone': user.phone,
            'website': user.website
        }
        for user in users
    ]
    
    df = pd.DataFrame(data)
    
    
    print(f"\nDataset Shape: {df.shape}")
    print(f"  Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")
    
    
    print("First Two Records:")
    print(df.head(2).to_string())
    print()
    
    
    print("Last Two Records:")
    print(df.tail(2).to_string())
    print()
