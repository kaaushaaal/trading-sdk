from fastapi import APIRouter, HTTPException
from uuid import UUID
from app.models import OrderRequest
from app.services.order_service import place_order
from app.storage import orders

router = APIRouter()

@router.post("/api/v1/orders")
def create_order(order: OrderRequest):
    try:
        return place_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/v1/orders/{order_id}")
def get_order_status(order_id: UUID):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders[order_id]
