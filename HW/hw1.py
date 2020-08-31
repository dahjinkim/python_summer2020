class Portfolio():
    def __init__(self, cash = 0, stock = [], mutualfund = []):
        self.cash = cash
        self.stock = stock
        self.mutualfund = mutualfund

    def __str__(self):
        return 'cash: ${:.2f}\nstock: {}\nmutual fund: {}'.format(self.cash, self.stock, self.mutualfund)

    def addCash(self, money): # adds cash
        self.cash += money
        return 'Current cash: {:.2f}'.format(self.cash)

    def withdrawCash(self, money): # removes cash
        self.cash -= money
        return 'Current cash: {:.2f}'.format(self.cash)

    def buyStock(self, share, stock):
        if type(share) != int:
            return print('Stock must be whole unit')
        elif self.cash - (share * stock.price) < 0:
            return print('Not enough money!')
        else:
            self.cash -= (share * stock.price)
            self.stock.append((share, stock.symbol))

    def buyMutualFund(self, share, fund):
        if self.cash - share < 0:
            return print('Not enough money!')
        else:
            self.cash -= share
            self.mutualfund.append((share, fund.symbol))

    # def sellStock(symbol, a): # sell a share of stock with symbol

    # def sellMutualFund(symbol, a): # buy a share of mutualfund with symbol

    # def history(): # prints list of all transactions ordered by time

class Stock():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol

class MutualFund():
    def __init__(self, symbol):
        self.symbol = symbol


portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
portfolio.buyStock(10.3, s)
portfolio.buyStock(100, s)
mf1 = MutualFund("BRT")
portfolio.buyMutualFund(10.3, mf1)
print(portfolio)
