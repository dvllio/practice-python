# Print string in backwards order.

x = input("enter string: ")

def reversal(input_string):
  input_string = input_string.split()
  return " ".join(input_string[::-1])

print (reversal(x))