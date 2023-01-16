# Information about our database connection

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# define our engine (engine is the entry point to our database)
# check_same_thread=False allow SQLite more than one request at a time to communicate with the database
engine = create_engine(get_settings().db_url, connect_args={"check_same_thread": False}) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() #connect database engine to the SQLAlchemy functionality of the models

# Note: Base will be the class that the database model inherits from in our models.py