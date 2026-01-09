from app.storage import portfolio, instruments
from app.models import PortfolioHolding

def get_portfolio():
    result = []

    for symbol, data in portfolio.items():
        ltp = next(
            i["lastTradedPrice"]
            for i in instruments
            if i["symbol"] == symbol
        )

        avg_price = data["totalCost"] / data["quantity"]

        result.append(
            PortfolioHolding(
                symbol=symbol,
                quantity=data["quantity"],
                averagePrice=avg_price,
                currentValue=ltp * data["quantity"]
            )
        )

    return result
