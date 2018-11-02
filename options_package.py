import tradersbot as tt
import math

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
    security_dict = msg['case_meta']['securities']
    for security in security_dict.keys():
        if not(security_dict[security]['tradeable']): 
            continue
        SECURITIES[security] = security_dict[security]['starting_price']

# Updates latest price
def market_update_method(msg, order):
    global SECURITIES
    SECURITIES[msg['market_state']['ticker']] = msg['market_state']['last_price']

# Buys or sells in a random quantity every time it gets an update
# You do not need to buy/sell here
def trader_update_method(msg, order):
    global SECURITIES
    print(SECURITIES)
    print(msg)
    positions = msg['trader_state']['positions']
    for security in positions.keys():
        if random.random() < 0.5:
            quant = 50
            order.addBuy(security, quantity=quant,price=SECURITIES[security])
        else:
            quant = 50
            order.addSell(security, quantity=quant,price=SECURITIES[security])

###############################################
#### You can add more of these if you want ####
###############################################

t.onAckRegister = ack_register_method
t.onMarketUpdate = market_update_method
t.onTraderUpdate = trader_update_method
#t.onTrade = trade_method
#t.onAckModifyOrders = ack_modify_orders_method
#t.onNews = news_method
t.run()