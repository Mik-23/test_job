import uuid
from fastapi import FastAPI
from models import Wallets
from database import engine
from sqlalchemy.orm import sessionmaker
from pydantic_models import WalletsPydantic

app = FastAPI()
Session = sessionmaker(bind=engine)
session = Session()


@app.get("/")
def begin():
    return "Begin"


@app.post("/api/v1/wallets/create")
def create_wallets(wallets_pydantic: WalletsPydantic):
    # Создать новый баланс кошелька
    wallet = Wallets()
    wallet.id = uuid.uuid4()
    wallet.operation_type = wallets_pydantic.operation_type
    wallet.amount = wallets_pydantic.amount
    session.add(wallet)
    session.commit()
    return {"id": wallet.id,
            "operation_type": wallet.operation_type,
            "amount": wallet.amount}


@app.post("/api/v1/wallets/{wallet_uuid}/operation")
def edit_wallets(wallet_uuid: uuid.UUID, wallets_pydantic: WalletsPydantic):
    # Изменить баланс кошелька
    wallet = session.query(Wallets).filter(Wallets.id == wallet_uuid).first()
    wallet.operation_type = wallets_pydantic.operation_type
    wallet.amount = wallets_pydantic.amount
    session.commit()
    return {"operation_type": wallet.operation_type,
            "amount": wallet.amount}


@app.get("/api/v1/wallets/{wallet_uuid}")
def get_wallets(wallet_uuid: uuid.UUID):
    # Получить баланс кошелька
    wallet = session.query(Wallets).filter(Wallets.id == wallet_uuid).first()
    return {"id": wallet.id,
            "operation_type": wallet.operation_type,
            "amount": wallet.amount}
