user_input1=float(input("enter side 'a':"))
user_input2=float(input("enter side 'b':"))
user_input3=float(input("enter side 'c':"))
if "a+b>c" and "a+c>b" and "b+c>a":
    print("traiangle can be formed")
else:
    print("traiangle can not be formed")