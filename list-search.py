# Three different list search

a = [1, 3, 5, 30, 42, 43, 500]
num = int(input("number to search: "))

def checkList1(alist, num):
  if num in alist:
    return True
  else:
    return False

def checkList2(alist, num, lb, ub):
  
  if ub >= lb:
    mid = lb + (ub-lb)//2

    if alist[mid] == num:
      return True

    elif alist[mid] > num:
      return checkList2(alist, num, lb, mid-1)
    
    elif alist[mid] < num:
      return checkList2(alist, num, mid+1, ub)
  
  else:
    return False

def checkList3(alist, num):

  lb = 0
  ub = len(alist)-1

  while ub > lb:
    mid = ub-lb // 2

    if alist[mid] == num:
      return True

    elif alist[mid] > num:
      ub = mid - 1

    elif alist[mid] < num:
      lb = mid + 1
  
  else:
    return False

print ("check1:",checkList1(a, num))
print ("check2:",checkList2(a, num, 0, len(a)-1))
print ("check3:",checkList3(a,num))