from stock_quote import StockQuote
from datetime import datetime

print(StockQuote("AAPL", datetime(2018,1,29,17,0), 167.96).time)
