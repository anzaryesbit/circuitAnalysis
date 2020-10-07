#string -> number
#write ohms as O
def ohms_law(voltage=None, current=None, resistance=None):
    try:
        current_comp = current.split(" ")
        current_amt = float(current_comp[0])
        current_unit = current_comp[1]
        voltage_comp = voltage.split(" ")
        voltage_amt = float(voltage_comp[0])
        voltage_unit = voltage_comp[1]
        resistance_comp = resistance.split(" ")
        resistance_amt = float(resistance_comp[0])
        resistance_unit = resistance_comp[1]
    except AttributeError:
        pass
    if voltage is None:
        current_amt = do_conversion(current_amt, current_unit)
        resistance_amt = do_conversion(resistance_amt, resistance_unit)
        return "voltage: " + str(current_amt * resistance_amt)
    elif current is None:
        voltage_amt = do_conversion(voltage_amt, voltage_unit)
        resistance_amt = do_conversion(resistance_amt, resistance_unit)
        return "current: " + str(voltage_amt / resistance_amt)
    elif resistance is None:
        current_amt = do_conversion(current_amt, current_unit)
        voltage_amt = do_conversion(voltage_amt, voltage_unit)
        return "resistance: " + str(voltage_amt / current_amt)
    else:
        raise ValueError


def joules_law(voltage=None, current=None, resistance=None, power=None):
    if resistance is None:
        return voltage ** 2 / power

#conversion stuff
def do_conversion(num, value):
    if value[0] == "m":
        return mili_to_normal(num)
    elif value[0] == "k":
        return kilo_to_normal(num)
    elif len(value) == 1:
        return num

def mili_to_normal(num):
    return num / 1000

def kilo_to_normal(num):
    return num * 1000

def centi_to_normal(num):
    return num / 100
