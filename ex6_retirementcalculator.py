#ex6_retirementcalculator.py
import time
from datetime import date

a = int(input("What is your age? "))
b = int(input("How old would you like to be when you retire? "))
today = date.today()
thisyear = date.today().year

if b > a :
    print ("You have " + str(b-a) + " years to go. Which means " +
       " in " + str(int(thisyear) + (b-a)) + " you'll have a lot more time.")
else:
    print ("You want to already be retired? I can't help you with that. ")
    