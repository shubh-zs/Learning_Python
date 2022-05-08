a = [1,2,3,4,5,6,7]
z = [0,1,2,3,4]
b = len(a)  
c = []
d = []
f = []
if b%2 == 0:
    c.extend(a[:b//2])
    d.extend(a[b//2:])
    d.extend(c)
    print(d)
else:
    c.extend(a[:b//2])
    e = a[b//2]
    d.extend(a[((b//2)+1):])
    f.extend(d)
    f.append(e)
    f.extend(c)
    print(f)

print("Orignal list :",a)
a.reverse()
print(a)