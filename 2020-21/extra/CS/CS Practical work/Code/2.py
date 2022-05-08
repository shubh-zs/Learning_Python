a = int(input("Write the number of units consumed :"))
r = 0
if a < 100:
    r = 1*a
elif a<300:
    r = 2*a
elif a>300:
    r = 4*a
print("Charges for electricity used : ",r)