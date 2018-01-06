#ex7_roomsize.py

I2M = .09290304
x, y = None, None

while x == None: 
     inputone = input("What is the first width (in feet)? ")
     try:
          x = int(inputone)
     except:
          print('"' + inputone + '" is not numeric. Please try again.')

while y == None: 
     inputtwo = input("What is the length (in feet)? ")
     try:
          y = int(inputtwo)
     except:
          print('"'+ inputtwo + '" is not numeric. Please try again.')

width = str(inputone)
length = str(inputtwo)

ImpArea = x * y
MetArea = x * y * I2M 

print ("The room is " + str(ImpArea) + " square feet \n" +
       "and "+ str(MetArea) + " square metres. \n" )
