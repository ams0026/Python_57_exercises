#

import stateparsing

myState = input("What are we looking up? ")
canonST = stateparsing.parse(myState)

print(myState + "'s codes are: " + canonST[0] + " and " + canonST[1])
