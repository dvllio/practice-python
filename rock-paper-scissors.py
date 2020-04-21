#Rock beats scissors
#Scissors beats paper
#Paper beats rock

import os
again = True

while again:
  os.system('clear')
  p1 = 0
  p2 = 0
  valid1 = False
  valid2 = False

  while not valid1:
    p1 = input("p1 rock, paper or scissors? ")
    if p1 == "rock":
      valid1 = True
      os.system('clear')
    elif p1 == "paper":
      valid1 = True
      os.system('clear')
    elif p1 == "scissors":
      valid1 = True
      os.system('clear')

  while not valid2:
    p2 = input("p2 rock, paper or scissors? ")
    if p2 == "rock":
      valid2 = True
      os.system('clear')
    elif p2 == "paper":
      valid2 = True
      os.system('clear')
    elif p2 == "scissors":
      valid2 = True
      os.system('clear')

  if p1 == p2:
    print ("exequo!")
  elif p1 == "rock":
    if p2 == "scissors":
      print ("p1 wins")
    else: 
      print ("p2 wins")
  elif p1 == "scissors":
    if p2 == "paper":
     print ("p1 wins")
    else:
      print ("p2 wins")
  elif p1 == "paper":
    if p2 == "rock":
     print ("p1 wins")
    else:
      print ("p2 wins")

  print ("-------")
  if input("type `no` to stop, enter to restart ") == "no":
    again = False