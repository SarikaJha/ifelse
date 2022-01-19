basic=float(input("enter a number"))
if (basic<=10000):
    DA=basic*(80/100)
    HRA=basic*(20/100)
elif(basic<=20000):
    DA=basic*(90/100)
    HRA=basic*(25/100)
else:
    DA=basic*(95/100)
    HRA=basic*(30/100)
gross=basic+HRA+DA
print("the gross salary" , gross )

