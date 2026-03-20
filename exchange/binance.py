import requests
from utils.logger import log

BASE_URL = "https://fapi.binance.com"

def get_price(symbol="BTCUSDT"):
    url = f"{BASE_URL}/fapi/v1/ticker/price?symbol={symbol}"
    res = requests.get(url).json()
    return float(res["price"])

def place_order(symbol, side, quantity):
    log(f"[BINANCE] {side} {quantity} {symbol}")
