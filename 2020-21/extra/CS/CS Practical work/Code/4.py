a = int(input('Write a number :'))
b = []
for i in range(1,a+1):
    if a%i ==0:
        b.append(i)
    else:
        continue

if len(b) == 2:
    print("The given number is Prime")
else:
    print("The given number is not Prime")



