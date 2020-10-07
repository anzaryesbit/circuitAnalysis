def joules_law(voltage=None, current=None, resistance=None, power=None):
    if resistance is None:
        return voltage ** 2 / power
