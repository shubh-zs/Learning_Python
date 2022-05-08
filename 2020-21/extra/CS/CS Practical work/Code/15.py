a = open("imp.txt",'r')
b = a.read()
c = b.split()
d = 0
for i in c:
    if i.lower() in ['me','my']:
        d += 1
print(d)
a.close()