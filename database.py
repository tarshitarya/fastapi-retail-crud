from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql://postgres:tarshit@localhost:5432/learn'
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

