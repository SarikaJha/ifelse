year=int(input("enter the year"))
if year%400==00:
    print(year,"is a century year")
elif year%4==00 and year%100!=00:
    print (year,"is a leap year")
else:
    print(year,("is not a leap year"))
