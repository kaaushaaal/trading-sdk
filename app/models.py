from pydantic import BaseModel
from enum import Enum
from typing import Optional
from uuid import UUID

class OrderType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderStyle(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"

class OrderStatus(str, Enum):
    NEW = "NEW"
    PLACED = "PLACED"
    EXECUTED = "EXECUTED"
    CANCELLED = "CANCELLED"

class Instrument(BaseModel):
    symbol: str
    exchange: str
    instrumentType: str
    lastTradedPrice: float

class OrderRequest(BaseModel):
    symbol: str
    quantity: int
    orderType: OrderType
    orderStyle: OrderStyle
    price: Optional[float] = None

class Order(BaseModel):
    orderId: UUID
    status: OrderStatus
    request: OrderRequest

class Trade(BaseModel):
    tradeId: UUID
    orderId: UUID
    symbol: str
    quantity: int
    price: float

class PortfolioHolding(BaseModel):
    symbol: str
    quantity: int
    averagePrice: float
    currentValue: float
