#/r/dailyprogrammer -- challenge 344
#In mathematics, the Baum\?Sweet sequence is an infinite automatic sequence of 0s and 1s defined by the rule:
#    b_n = 1 if the binary representation of n contains no block of consecutive 0s of odd length;
#    b_n = 0 otherwise;
#for n >= 0.
#Your challenge today is to write a program that generates the Baum-Sweet sequence from 0 to some number n.
#For example, given "20" your program would emit:
#1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0

def baumsweet(numList):
    numList.pop(0)
    numList.pop(0)
    
    print(numList)
    oddgroup = False
    groupnum = 0
 
    for x in (numList):
      if x == 0:
          groupnum+=1
      else:
          if groupnum%2==0:
             groupnum = 0
          else:
             oddgroup = True

    return oddgroup

n = None
while n == None:
  n = input("What's the ending number? ")
  try:
      n == int(n)
  except:
      n = None
      print("Please enter a decimal number.")

for i in range(int(n)):
    myBinary = list(bin(int(i)))
    print(baumsweet(myBinary))

