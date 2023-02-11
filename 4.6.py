def delchar(a,b):
    if len(b)!=1:
        return a
    else:
        return a.replace(b,"")
a=input("enter the string:")
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))
