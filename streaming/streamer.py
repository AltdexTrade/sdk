from utils.logger import log

def stream_trade(exchange, symbol, side, price):
    log(f"[STREAM] {exchange} {side} {symbol} @ {price}")
