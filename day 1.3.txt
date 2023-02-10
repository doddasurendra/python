number=3
def isHappyNumber(number):
    reminder = 0
    sum = 0
    while (number!= 0):
        reminder = number % 10
        sum = sum + (reminder * reminder);
        number = number // 10
    return sum
result = number
while (result != 1 and result != 4):
    result = isHappyNumber(result)
if (result == 1):
    print("a happy number")
elif (result == 4):
    print("not a happy number")
