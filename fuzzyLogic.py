def fuzzor(x,y)
    max (x,y)
def fuzzand(x,y)
    min (x,y)
def fuzznot(x)
    1 - x
def fuzzcon(x,y)
    1 - max (0, x-y)
