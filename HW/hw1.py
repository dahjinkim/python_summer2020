class Portfolio():
    def __init__(self, cash, stock, mutualfund):
        self.cash = cash
        self.stock = stock
        self.mutualfund = mutualfund

    def __str__():
        return 'cash: {}\nstock: {}\nmutual fund: {}'.format(self.cash, self.stock, self.mutualfund)

    def addCash(): # adds cash

    def withdrawCash(): # removes cash

    def buyStock(a, b): # buy a share of stock b

    def sellStock(symbol, a): # sell a share of stock with symbol

    def buyMutualFund(a, b): # buy a share of mutualfund b

    def sellMutualFund(symbol, a): # buy a share of mutualfund with symbol

    def history(): # prints list of all transactions ordered by time


class Stock():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol

class MutualFund():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol
