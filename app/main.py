from fastapi import FastAPI
from app.routes import instruments, orders, trades, portfolio

app = FastAPI(
    title="Trading API SDK – Bajaj Broking (Simulation)",
    version="1.0.0"
)

app.include_router(instruments.router)
app.include_router(orders.router)
app.include_router(trades.router)
app.include_router(portfolio.router)
