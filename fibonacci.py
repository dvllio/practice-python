# Asks the user how many Fibonacci numbers to generate and then generates them.

f = []
number = int(input ("how many Fibonnaci numbers do you want? "))

def seqGen(number):
  for x in range (number):
    if len(f) > 1:
      y = f[x-1]+f[x-2]
      f.append(y)
    else:
      f.append(1)
  return f

print (seqGen(number))