# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.

def fileToList(file):
  alist = []
  with open(file, 'r') as open_file:
    line = open_file.readline()
    while line:
      line = line.strip()
      if line not in alist:
        alist.append(line)
      line = open_file.readline()
  return alist

happylist = fileToList("happynumbers.txt")
primelist = fileToList("primenumbers.txt")
commonlist = []

commonlist = [a for a in happylist if a in primelist]

print (commonlist)
print ("Lists have",len(commonlist),"elements in common")