from uuid import uuid4
from app.models import Order, OrderStatus, Trade
from app.storage import orders, trades, portfolio, instruments

def place_order(order_req):
    if order_req.quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if order_req.orderStyle == "LIMIT" and order_req.price is None:
        raise ValueError("Price is mandatory for LIMIT orders")

    order_id = uuid4()
    order = Order(
        orderId=order_id,
        status=OrderStatus.PLACED,
        request=order_req
    )

    orders[order_id] = order

    instrument = next(
        i for i in instruments if i["symbol"] == order_req.symbol
    )

    execution_price = (
        order_req.price
        if order_req.orderStyle == "LIMIT"
        else instrument["lastTradedPrice"]
    )

    trade = Trade(
        tradeId=uuid4(),
        orderId=order_id,
        symbol=order_req.symbol,
        quantity=order_req.quantity,
        price=execution_price
    )

    trades.append(trade)
    order.status = OrderStatus.EXECUTED

    holding = portfolio.get(
        order_req.symbol,
        {"quantity": 0, "totalCost": 0}
    )

    holding["quantity"] += order_req.quantity
    holding["totalCost"] += execution_price * order_req.quantity

    portfolio[order_req.symbol] = holding

    return order
