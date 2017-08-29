"""Shopping Manager Module"""
def addtax(price, tax):
    """Add Tax"""
    newprice = price / 100 * (100 * tax)
    return newprice

TAXPRICE = addtax(1000, 5)
print TAXPRICE
