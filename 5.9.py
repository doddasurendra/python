def shuffle(l1,l2):
    c=[]
    if len(l1)!=0 and len(l2)!=0:
      for i in range(min(len(l1), len(l2))):
        c.extend([l1[i],l2[i]])
      c.extend(l1[i+1:] or l2[i+1:])
    else:
      c.extend(l1[0:] or l2[0:])
    return (c)

n1=int(input("enter the number of terms"))
na=[]
for i in range(0,n1):
             x=int(input("enter"))
             na.append(x)
print(na)
n1=int(input("enter the number of terms"))
nb=[]
for i in range(0,n1):
            x=int(input("enter"))
            nb.append(x)
print(nb)
print(shuffle(na,nb))
