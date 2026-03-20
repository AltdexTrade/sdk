from strategies.breakout import is_breakout
from exchange.binance import get_price as binance_price, place_order as binance_order
from exchange.dex import get_price as dex_price, place_order as dex_order
from streaming.streamer import stream_trade
from utils.logger import log
import time

class Trader:
    def __init__(self):
        self.history = []

    def run(self):
        while True:
            price = binance_price("BTCUSDT")
            self.history.append(price)

            log(f"Price: {price}")

            if is_breakout(self.history):
                log("Breakout detected!")

                binance_order("BTCUSDT", "BUY", 0.001)
                dex_order("SOL", "BUY", 1)

                stream_trade("BINANCE", "BTCUSDT", "BUY", price)

            time.sleep(5)
