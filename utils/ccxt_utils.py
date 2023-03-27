 
import ccxt

from config import API_KEY, SECRET_KEY


def initialize_exchange():
    exchange = ccxt.okex({
        'apiKey': API_KEY,
        'secret': SECRET_KEY,
        'enableRateLimit': True,
    })

    return exchange
