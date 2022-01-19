year=int(input("enter the years of service :"))
salary=int(input("enter the salary :"))
bonus=5/100
if year>5:
    salary=salary+(bonus*salary)
    print("salary with 5 percent bonus is",salary)
else:
    print("salary of the employee is",salary)