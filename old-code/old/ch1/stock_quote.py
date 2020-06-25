class StockQuote():
    def __init__(self, symbol, time, price):
        self.symbol = symbol
        self.time = time
        self.price = price

class BinaryTree():
    def __init__(self, value, lowerTree, higherTree):
        self.value = valued
        self.lowerTree = lowerTree
        self.higherTree = higherTree

sym = "AAPL"

quoteTree = BinaryTree(
                StockQuote(sym, time(9,1,45), 166.95),
                BinaryTree(
                    StockQuote(sym, time(9,0,23), 167.25),
                    StockQuote(sym, time(9,0,0), 166.19),
                    BinaryTree(
                        StockQuote(sym, time(9,1,6), 166.08),
                        StockQuote(sym, time(9,0,41), 166.48),
                        None
                    )
                ),
                StockQuote(sym, time(9,2,25), 165.30))

def quoteSearch(tree, quote):
    try:
        tree.value
