from tradersbot import *
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import py_vollib

#Initialize variables: positions, expectations, future customer orders, etc
position_limit = 5000
case_length = 450
cash = 0
position_lit = 0
position_dark = 0
time = 0
topBid = 0
topAsk = 0
#etc etc
"""
py_vollib.black_scholes_merton.implied_volatility.implied_volatility(price, S, K, t, r, q, flag)[source]
Calculate the Black-Scholes-Merton implied volatility.

Parameters:	
S (float) – underlying asset price
K (float) – strike price
sigma (float) – annualized standard deviation, or volatility
t (float) – time to expiration in years
r (float) – risk-free interest rate
q (float) – annualized continuous dividend rate
flag (str) – ‘c’ or ‘p’ for call or put.
>>> S = 100
>>> K = 100
>>> sigma = .2
>>> r = .01
>>> flag = 'c'
>>> t = .5
>>> q = 0
>>> price = black_scholes_merton(flag, S, K, t, r, sigma, q)
>>> iv = implied_volatility(price, S, K, t, r, q, flag)
>>> expected_price = 5.87602423383
>>> expected_iv = 0.2
"""


def register(msg, TradersOrder):
    #Set case information
    pass

def update_market(TradersOrder):
    #Update market information
    pass

def update_trader(TradersOrder):
    #Update positions
    pass

def update_trade(msg, TradersOrder):
    #Update trade information
    pass

def update_order(msg, TradersOrder):
    #Update order information
    pass

def update_news(msg, TradersOrder):
    #Update news information
    pass

def process():
    #Do stuff to trade
    pass

t = TradersBot('127.0.0.1', 'trader0', 'trader0')

t.onAckRegister = register
t.onMarketUpdate = update_market
t.onTraderUpdate = update_trader
t.onTrade = update_trade
t.onAckModifyOrders = update_order
t.onNews = update_news

t.run()
