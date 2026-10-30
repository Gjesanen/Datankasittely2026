import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuration import API_URL, DATABASE_URL
from database.models import User


def fetch_and_store_users():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        for u in response.json():
            session.merge(User(
                id=u["id"],
                name=u["name"],
                username=u["username"],
                email=u["email"],
                city=u["address"]["city"],
                company_name=u["company"]["name"],
                phone=u["phone"],
                website=u["website"],
            ))
        session.commit()