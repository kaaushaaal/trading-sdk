from app.services.order_service import place_order
from app.models import OrderRequest, OrderType, OrderStyle

def test_market_order_execution():
    order = place_order(
        OrderRequest(
            symbol="RELIANCE",
            quantity=5,
            orderType=OrderType.BUY,
            orderStyle=OrderStyle.MARKET
        )
    )
    assert order.status.value == "EXECUTED"
