a = [15,12,35,64,15,6,73,88,49]
c = 0
for i in range(len(a)):
    b = str(a[i])
    if b[-1] == "5":
        c += a[i]
    else:
        continue
print(c)