a=int(input("value of side a :"))
b=int(input("value of side b :"))
c=int(input("value of side c :"))
if a==b==c:
    print ("it is equilateral triangle")
elif a==b or b==c or c==a:
    print ("it is isosceles triangle")
else:
    print("it is scalene triangle")