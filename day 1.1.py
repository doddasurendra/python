def hemesh(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
    return True
print(hemesh("fool","poor"))
print(hemesh("foal","poor"))
print(hemesh("too","bar"))
print(hemesh("toto","yaya"))
