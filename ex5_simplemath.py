#ex5_simplemath.py

inputone = input("What is the first number? ")
# if inputone.isalpha():
#     inputone = input(inputone + " is not numeric. Please try again: ")
# if inputone.isalnum():
#     inputone = input(inputone + " is not numeric. Please try again: ")

inputtwo = input("What is the second number? ")
# if inputtwo.isalpha():
#     inputtwo = input(inputtwo + " is not numeric. Please try again: ")
# if inputtwo.isalnum():
#     inputtwo = input(inputtwo + " is not numeric. Please try again: ")

x = str(inputone)
y = str(inputtwo)

print (x + " + " + y +" = " + str(inputone+inputtwo) + "\n" +
       x + " - " + y +" = " + str(inputone-inputtwo) + "\n" +
       x + " * " + y +" = " + str(inputone*inputtwo) + "\n" +
       x + " / " + y +" = " + str(inputone/inputtwo) + "\n" +
       x + " % " + y +" = " + str(inputone%inputtwo) + "\n" +
       x + " ** " + y +" = " + str(inputone**inputtwo) + "\n" )
