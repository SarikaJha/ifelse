quantity=int(input("enter the required quantity : "))
cost=100
total=quantity*cost
discount=10/100
if total>1000:
    total=total-(discount*total)
    print("your total cost with 10 percent discount is",total)
else:
    print("your total cost is",total)