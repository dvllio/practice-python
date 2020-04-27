# User, will have in your head a number between 0 and 100. The program will guess a number and the user will say whether it is too high, too low, or your number.

possibilities = list(range(0, 101))

def findMid(alist):
  lb = 0
  ub = len(possibilities)-1
  tries = 0
  
  while ub >= lb:
    mid = lb + (ub-lb)//2
    
    print("Computer:",mid)
    print("Is it too 'high' or too 'low' or 'ok'? ")

    humanCheck = input()
    tries += 1
    if humanCheck == "ok":
      print("Yay! It took",tries,"tries")
      break
    elif humanCheck == "high":
      ub = mid - 1
    elif humanCheck == "low":
      lb = mid + 1

findMid(possibilities)