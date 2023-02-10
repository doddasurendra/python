l=[3,7,9,6,4,7,34,86,9,78]
def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even=even+i**2
        else:
            odd=odd+i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))
