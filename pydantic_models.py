from pydantic import BaseModel


class WalletsPydantic(BaseModel):
    # Валидация кошелька пользователя
    operation_type: str
    amount: int
