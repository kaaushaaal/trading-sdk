from uuid import UUID

instruments = [
    {
        "symbol": "RELIANCE",
        "exchange": "NSE",
        "instrumentType": "EQUITY",
        "lastTradedPrice": 2500.0
    },
    {
        "symbol": "TCS",
        "exchange": "NSE",
        "instrumentType": "EQUITY",
        "lastTradedPrice": 3900.0
    }
]

orders = {}        # orderId -> Order
trades = []        # list of Trade
portfolio = {}     # symbol -> {quantity, totalCost}
