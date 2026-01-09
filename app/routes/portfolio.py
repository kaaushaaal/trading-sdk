from fastapi import APIRouter
from app.services.portfolio_service import get_portfolio

router = APIRouter()

@router.get("/api/v1/portfolio")
def fetch_portfolio():
    return get_portfolio()
