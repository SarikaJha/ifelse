unit=float(input("enter the unit consumed :"))
if (unit<50):
    amt=unit*0.50
    sur=20
elif(unit<=150 and unit>=50):
    amt=unit*0.75
    sur=20
elif(unit<=250 and unit>=150):
    amt=unit*1.20
    sur=20
else:
    amt=unit*1.50
    sur=20
total=amt-sur
print("electricity bill is", total)