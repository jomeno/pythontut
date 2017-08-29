"""Useful Modules"""
import random
import math
from datetime import date
import time
from os import path
import urllib2

print random.randint(0, 10)
print random.random()

MYLIST = [1, 8, True, 77, "Lorem", 438, "Ipsum"]
print random.choice(MYLIST)

print math.pi

#datetime samples
print time.time() #seconds since Unix Epoch, Jan 1st, 1970
print date.fromtimestamp(time.time()) #current time
DAYS = int(time.time()/(60*60*24))
TODAY = date.fromordinal(DAYS)
CURRDATE = date.fromtimestamp(time.time())
print CURRDATE.strftime("%d/%m/%y")
print path.exists("/Users/jomeno")
print date.fromtimestamp(path.getatime("/Users/jomeno"))
print path.getsize("/Users/jomeno/desktop/pythontut/index.py")
print path.join("C:", "/Users") #returns "C:/Users"

print urllib2.urlopen("http://google.com").read(100)
