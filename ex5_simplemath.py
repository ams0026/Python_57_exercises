#ex5_simplemath.py
import sys

x, y = None, None


while x == None: 
     inputone = input("What is the first number? ")
     try:
          x = int(inputone)
     except:
          print('"' + inputone + '" is not numeric. Please try again.')

inputtwo = input("What is the second number? ")
try:
     y = int(inputtwo)
except:
     print('"'+ inputtwo + '" is not numeric. Please try again.')
     sys.exit()
ex = str(inputone)
why = str(inputtwo)

print (ex + " + " + why +" = " + str(x + y) + "\n" +
       ex + " - " + why +" = " + str(x - y) + "\n" +
       ex + " * " + why +" = " + str(x * y) + "\n" +
       ex + " / " + why +" = " + str(x / y) + "\n" +
       ex + " % " + why +" = " + str(x % y) + "\n" +
       ex + " ** " + why +" = " + str(x ** y) + "\n" )
