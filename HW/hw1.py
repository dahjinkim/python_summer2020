"""
Class: Python 2020
Homework Assignment 1
Author: Jin Kim
"""

## Importing necessary modules
import random

## Create portfolio class
class Portfolio():
    def __init__(self): # attributes of portfolio
        self.cash = 0
        self.stock = {}
        self.mutualfund = {}
        self.transactions = []

    def __str__(self): # print function
        return 'cash: ${:.2f}\nstock: {}\nmutual fund: {}'.format(self.cash, self.stock, self.mutualfund)

    def addCash(self, money): # adds cash
        self.cash += money
        self.transactions.append("Added ${:.2f}; Total: ${:.2f}".format(money, self.cash)) # records transactions
        return 'Current cash: {:.2f}'.format(self.cash) # prints out current amount

    def withdrawCash(self, money): # removes cash
        if self.cash < money: # check if the account has enough cash
            return 'Not enough deposit!'
        else:
            self.cash -= money
            self.transactions.append("Withdrew ${:.2f}; Total: ${:.2f}".format(money, self.cash)) # records transactions
            return 'Current cash: {:.2f}'.format(self.cash) # prints out current amount

    def buyStock(self, share, stock): # buys certain shares of stock
        if type(share) != int: # if the share is not a whole number
            return print('Stock must be whole unit')
        elif self.cash - (share * stock.price) < 0: # check if we have enough money to buy
            return print('Not enough money!')
        else:
            self.cash -= (share * stock.price) # update cash by subtracting cost
            if stock.symbol in self.stock.keys(): # check if we have the same stock in place
                self.stock[stock.symbol]['share'] += share # update share
            else:
                self.stock[stock.symbol] = {'share': share, 'price': stock.price}  # tracks stocks in possession with share and original price
            self.transactions.append("Bought {} shares of {} for ${:.2f}; Total: ${:.2f}".format(share, stock.symbol, share * stock.price, self.cash)) # records transactions

    def buyMutualFund(self, share, fund): # buys certain shares of fund
        if self.cash - share < 0: # checks cash
            return print('Not enough money!')
        else:
            self.cash -= share
            if fund.symbol in self.mutualfund.keys():
                self.mutualfund[fund.symbol]['share'] += share
            else:
                self.mutualfund[fund.symbol] = {'share': share, 'price': 1.00} # tracks funds in possession
            self.transactions.append("Bought {} shares of {} for ${:.2f}; Total: ${:.2f}".format(share, fund.symbol, share, self.cash)) # records transactions

    def sellStock(self, symbol, unit): # sell unit share of stock with symbol
        if symbol not in self.stock.keys(): # check if you have it
            return 'Not in possession!'
        elif self.stock[symbol]['share'] - unit < 0: # if you are trying to sell too many
            return 'Not enough share! Can only sell up to {} shares'.format(self.stock[symbol]['share'])
        else:
            self.stock[symbol]['share'] -= unit # change share in possession
            profit = random.uniform(self.stock[symbol]['price']*0.9, self.stock[symbol]['price']*1.2) * unit # calculate profit
            self.cash += round(profit, 2) # update cash
            self.transactions.append("Sold {} shares of {} for ${:.2f}; Total: ${:.2f}".format(unit, symbol, profit, self.cash))


    def sellMutualFund(self, symbol, unit): # buy unit share of mutualfund with symbol
        if symbol not in self.mutualfund.keys(): # check if you have it
            return 'Not in possession!'
        elif self.mutualfund[symbol]['share'] - unit < 0: # if you are trying to sell too many
            return 'Not enough share! Can only sell up to {} shares'.format(self.mutualfund[symbol]['share'])
        else:
            self.mutualfund[symbol]['share'] -= unit
            self.mutualfund[symbol]['share'] = round(self.mutualfund[symbol]['share'], 2) # round up to 2 floats
            profit = random.uniform(0.9, 1.2) * unit
            self.cash += round(profit, 2)
            self.transactions.append("Sold {} shares of {} for ${:.2f}; Total: ${:.2f}".format(unit, symbol, profit, self.cash))

    def history(self): # prints list of all transactions ordered by time
        return print(self.transactions)


## Create Stock class
class Stock():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol

## Create MutualFund class
class MutualFund(Stock):
    def __init__(self, symbol, price = 1):
        self.symbol = symbol
        self.price = price

## Bonus: create Bonds class
class Bonds(Stock):
    pass


## Test examples
portfolio = Portfolio() # creates portfolio
portfolio.addCash(300.50) # adds cash
s = Stock(20, "HFH") # creates stock
portfolio.buyStock(5, s) # buys 5 shares of s stock
portfolio.buyStock(10.3, s) # error: stock must be whole unit
portfolio.buyStock(100, s) # error: not enough cash
mf1 = MutualFund("BRT") # creates mutualfund
mf2 = MutualFund("GHT") # creates another mutualfund
portfolio.buyMutualFund(10.3, mf1) # buys 10.3 shares of mf1
portfolio.buyMutualFund(2, mf2) # buys 2 shares of mf2
print(portfolio) # lists cash and assets in possession
portfolio.sellMutualFund("BRT", 3) # sell 3 shares of mf1
portfolio.sellMutualFund("AAA", 2) # error: not in possession
portfolio.sellMutualFund("GHT", 10) # error: not enough to sell
portfolio.sellStock("HFH", 1) # sell 1 share of s stock
portfolio.withdrawCash(50) # withdraws cash
portfolio.history() # prints out all transactions
print(portfolio) # prints cash and assets in possession


#######################################
### Afterthoughts:
# My codes are very repetitive.
# There must be a cleaner way to code this using inheritance, but I'm submitting what I have so far.
# It will be cool to create unittest for this homework with test examples.
# I might try to re-write this homework and create a test file later.
