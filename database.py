from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import settings

database = settings.DATABASE_URI
Base = declarative_base()
engine = create_engine(settings.DATABASE_URI)