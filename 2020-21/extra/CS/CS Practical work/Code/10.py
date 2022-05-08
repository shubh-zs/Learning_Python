a =  []
n = int(input("How many element in the list : "))
for i in range(n):
    b = int(input("Elemnts in the list : "))
    a.append(b)

print("orignal : ",a)

for i in range(0,n): #0,1,2,3,4,5
    for j in range(0, n-i-1): # 0,6-0-1 = 0,5 = 0,1,2,3,4
        if a[j] > a[j+1] : # 1>2
            a[j], a[j+1] = a[j+1], a[j]
        else:
            continue
print("Sorted : ",a)
print("The largest number in the list is : ", a[-1])
print("The smallest number in the list is : ", a[0])



