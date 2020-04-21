# Two ways to dedup a list

names = ["Michele", "Robin", "Sara", "Michele"]

def dedupset(alist):
  return list(set(alist))

def deduploop(alist):
  blist=[]
  for x in alist:
    if x not in blist:
      blist.append(x)
  return blist

print ("loop: ", deduploop(names))
print ("set: ", dedupset(names))