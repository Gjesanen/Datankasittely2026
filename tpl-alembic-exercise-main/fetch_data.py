import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import API_URL, DATABASE_URL
from db.models import User

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def main():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    users = response.json()

    with SessionLocal() as session:
        for user_data in users:
            user = User(
                id=user_data["id"],
                name=user_data["name"],
                username=user_data["username"],
                email=user_data["email"],
            )
            session.merge(user)
        session.commit()

    print("Users inserted into database.")


if __name__ == "__main__":
    main()
