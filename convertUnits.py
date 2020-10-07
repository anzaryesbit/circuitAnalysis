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
