# Password generator

import string
import random

pwdLength = int(input("Password length: "))

def pwdGen(length):
  chars = string.ascii_letters + string.digits + string.punctuation
  return "".join(random.choice(chars) for x in range(length))

print (pwdGen(pwdLength))