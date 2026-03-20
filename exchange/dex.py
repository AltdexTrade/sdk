from utils.logger import log
import random

def get_price(token="SOL"):
    return random.uniform(10, 50)

def place_order(token, side, amount):
    log(f"[DEX] {side} {amount} {token}")
