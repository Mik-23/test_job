from sqlalchemy import Column, String, Integer, UUID
from database import Base, engine


class Wallets(Base):
    __tablename__ = 'wallets'

    id = Column(UUID, primary_key=True, index=True)
    operation_type = Column(String)
    amount = Column(Integer)


Base.metadata.create_all(bind=engine)
