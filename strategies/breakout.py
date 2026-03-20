def is_breakout(data):
    if len(data) < 2:
        return False
    return data[-1] > max(data[:-1])
