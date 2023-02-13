grade=input("enter the grade of employee")
if grade!='A' or grade != 'B':
    print("Enter a valid Grade either A or B")
salary=input("Enter the salary of the employee")
salary=int(salary)
if salary <=0:
    print("Enter a positive value")
elif grade=='A':
    if salary < 10000:
        bonus=salary*0.07
    else:
        bonus = salary * 0.05
        print(bonus)
    salary = salary + bonus
    print(salary)
elif grade=='B':
    if salary < 10000:
        bonus=salary*0.12
    else:
        bonus = salary * 0.1
    print("bonus:",bonus)
    salary = salary + bonus
    print("total to bepaid:",salary)

    
