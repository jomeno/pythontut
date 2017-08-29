"""This is my doc string"""
#from shopping_manager import addtax
from modules import shopping_manager
#FIRSTNAME = raw_input("Please type  your name and press enter:")
#GREETING = "Hello    %s" % FIRSTNAME
#print GREETING
A = 3
B = 4

if A < B:
    print "Success"
D = 0
E = 10
while D < E:
    print D
    D += 1
MYLIST = [1, 2, 3, 4, 5]
for a in MYLIST:
    print a
#out two costs to add up
COST1 = 15
COST2 = 20.3
COST3 = 5
COST4 = 10

def sumcart(cost1, cost2=1):
    """Sum function"""
    totalcost = cost1 + cost2
    return totalcost

CART1 = sumcart(COST1, COST2)
CART2 = sumcart(COST3)

print CART1
print CART2

print 'The number is ' + str(COST1)
print 'The number has a character count: ' + str(len(str(COST1)))
print int(COST2)
NUMBERS = range(1, 11, 2)
print NUMBERS

#demostrating import use
print shopping_manager.addtax(2000, 5)


class Pet(object):
    """Pet class"""
    legcount = 0
    def __init__(self):
        self.legcount = 1

    def sleep(self):
        """Sleep"""
        print "Asleep"

ZEUS = Pet()
print ZEUS.legcount
ZEUS.sleep()
