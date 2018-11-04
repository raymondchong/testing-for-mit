import tradersbot as tt
import math
import random


# Initialize #
t = tt.TradersBot(host='127.0.0.1', id='trader0', password='trader0')

# For now ^, for later:

# import sys
# t = tt.TradersBot(host=sys.argv[1], id=sys.argv[2], password=sys.argv[3])

# Functionality #
"""
py_vollib.black_scholes_merton.implied_volatility.implied_volatility(price, S, K, t, r, q, flag)[source]
Calculate the Black-Scholes-Merton implied volatility.
Parameters: 
S (float) – underlying asset price || K (float) – strike price
sigma (float) – volatility || t (float) – time in years
r (float) [ =0 ] – risk-free interest rate || q (float) [ =0 ] –  dividend rate
flag (str) – ‘c’ or ‘p’ for call or put.

e.g.
>>> price = black_scholes_merton(flag, S, K, t, r, sigma, q)
>>> iv = implied_volatility(price, S, K, t, r, q, flag)
>>> expected_price = 5.87602423383
>>> expected_iv = 0.2
"""

SECURITIES = {}

# Initializes the prices
def ack_register_method(msg, order):
    global SECURITIES
    print("_____Register Method____")
    print("Msg",msg)
    print("Order",order)
    security_dict = msg['case_meta']['securities']
    print(security_dict)
    for security in security_dict.keys():
        if not(security_dict[security]['tradeable']): 
            continue
        SECURITIES[security] = security_dict[security]['starting_price']

# Updates latest price
def market_update_method(msg, order):
    global SECURITIES
    SECURITIES[msg['market_state']['ticker']] = msg['market_state']['last_price']
    print("_____MARKET UDPATE Method____")
    print("Msg",msg)
    print("Order",order)
# Buys or sells in a random quantity every time it gets an update
# You do not need to buy/sell here
def trader_update_method(msg, order):
    
    global SECURITIES
    print("_____TradeR update Method____")
    print("Msg",msg)
    print("Order",order)
    # print(SECURITIES)
    # print(msg)
    positions = msg['trader_state']['positions']
    print(positions)
    for security in positions.keys():
        if random.random() < 0.5:
            quant = 50
            order.addBuy(security, quantity=quant,price=SECURITIES[security])
        else:
            quant = 50
            order.addSell(security, quantity=quant,price=SECURITIES[security])
# Sample copy market
def trade_method(msg, order):
    print("_____Trade Method____")
    print("Msg",msg)
    print("Order",order)
def ack_modify_orders_method(msg,order):
#####################


def ack_register_method(msg, order):
    global MARKET
    security_dict = msg['case_meta']['securities']
    for security in security_dict.keys():
        if not(security_dict[security]['tradeable']):
            continue
        type = security[-1].lower()
        price = security_dict[security]['starting_price']
        MARKET[security] = {}
        MARKET[security]['type'] = type
        MARKET[security]['cur_price'] = price
        MARKET[security]['prices'] = []
        #MARKET[security]['price'] = [price]
        if security != "TMXFUT":
            strike = int(security[1:-1])
            MARKET[security]['strike'] = strike
            MARKET[security]['cur_iv'] = iv(price, 100, strike, INTEREST_RATE, 1/12, type)
            MARKET[security]['ivs'] = []
    print(MARKET)


# Updates latest price periodically
def market_update_method(msg, order):
    global MARKET
    security = msg['market_state']['ticker']
    MARKET[security]['cur_price'] = msg['market_state']['last_price']
    MARKET[security]['prices'].append(MARKET[security]['cur_price'])
    if security != "TMXFUT":
        try:
            MARKET[security]['cur_iv'] = iv(MARKET[security]['cur_price'], 100, MARKET[security]['strike'], INTEREST_RATE, exp_time(), MARKET[security]['type'])
            MARKET[security]['ivs'].append(MARKET[security]['cur_iv'])
        except:
            MARKET[security]['cur_iv'] = 0
            MARKET[security]['ivs'].append(MARKET[security]['cur_iv'])
            print(security)

        # if security != "TMXFUT":
        #     MARKET[security]['ivs'].append(MARKET[security]['cur_iv'])
        # print(MARKET[security]['prices'])
        # print(MARKET[security]['ivs'])


# Updates market state after each trade
def trade_method(msg, order):
    global MARKET
    print('TRADE')
    trade_dict = msg['trades']
    for trade in trade_dict:
        security = trade["ticker"]
        MARKET[security]['cur_price'] = trade["price"]
        MARKET[security]['prices'].append(MARKET[security]['cur_price'])
        #security['price'].append(trade["price"])
        # security['vol'] = calc_vol(security['type'] == 'C', trade['price'], 100, security['strike'], exp_time(), INTEREST_RATE)
        if security != "TMXFUT":
            try:
                MARKET[security]['cur_iv'] = iv(MARKET[security]['cur_price'], 100, MARKET[security]['strike'], INTEREST_RATE, exp_time(), MARKET[security]['type'])
                MARKET[security]['ivs'].append(MARKET[security]['cur_iv'])
            except:
                MARKET[security]['cur_iv'] = 0
                MARKET[security]['ivs'].append(MARKET[security]['cur_iv'])
                print(security)




###########################
def news_method(msg):
    #should we try to logically track who is the insider?
    #regex to pull the word buy/sell is all right?
    # "___ is [buy/sell]ing ___ shares of ___!"
    print("_____News Method____")
    print("Msg",msg)
    print("Order",order)
###############################################
#### You can add more of these if you want ####
###############################################

t.onAckRegister = ack_register_method
t.onMarketUpdate = market_update_method
t.onTraderUpdate = trader_update_method
t.onTrade = trade_method
t.onAckModifyOrders = ack_modify_orders_method
t.onNews = news_method
t.run()