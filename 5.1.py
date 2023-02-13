def length(str):
    lis=list(str.split(" "))
    print(lis)
    print(len(lis[-1]))
    return len(lis[-1])
str=input("Enter the string to find the last word count")
print("The length of last word is",length(str))
