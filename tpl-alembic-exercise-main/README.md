# Using Alembic for Database Migrations

## Goal

Learn how to use Alembic with SQLAlchemy to:

- Define ORM models for data from an API ([JSONPlaceholder users endpoint](https://jsonplaceholder.typicode.com/users)).
- Generate and apply a migration to create tables.
- Verify that Alembic creates and updates the database schema based on your SQLAlchemy models.

## 1. Setup Project

Create this structure:

```
alembic_exercise/
│
├─ db/
│  ├─ __init__.py
│  └─ models.py
│
├─ alembic/              # created later by `alembic init`
├─ alembic.ini           # created later by `alembic init`
├─ config.py
├─ requirements.txt
└─ fetch_data.py
```

### requirements.txt & venv

```
SQLAlchemy
alembic
requests
```
Setup the virtual environment and install dependencies.

### config.py

```python
DATABASE_URL = "sqlite:///placeholder.db"
```

## 2. Define ORM Models

**db/models.py**

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Example: table for JSONPlaceholder "users"
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
```

## 3. Initialize Alembic

Run in terminal:

```bash
alembic init alembic
```

This creates `alembic/` and `alembic.ini`.

## 4. Configure Alembic

Edit **alembic.ini** and set the database URL:

```
sqlalchemy.url = sqlite:///placeholder.db
```

Edit **alembic/env.py** to import models:

```python
from db.models import Base
target_metadata = Base.metadata
```

## 5. Create Migration

Run:

```bash
alembic revision --autogenerate -m "create users table"
```

Alembic generates a new migration script in `alembic/versions/`. It will contain SQL for creating the `users` table.

## 6. Apply Migration

Run:

```bash
alembic upgrade head
```

Check that the database now has a `users` table (You can use for example SQLite Viewer extension in VS Code).

## 7. Insert Data from API

### config.py

Add API_URL `https://jsonplaceholder.typicode.com/users`. Remember to import it in the next script.

### fetch_data.py

```python
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def main():
    response = requests.get(API_URL)
    users = response.json()

    session = SessionLocal()
    for u in users:
        user = User(
            id=u["id"],
            name=u["name"],
            username=u["username"],
            email=u["email"]
        )
        session.merge(user)  # merge avoids duplicate key errors
    session.commit()
    session.close()
    print("Users inserted into database.")

if __name__ == "__main__":
    main()
```

Run:

```bash
python fetch_data.py
```

Check the `users` table now.
