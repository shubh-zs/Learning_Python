a = open("imp.txt",'r')
b = a.read()
c = b.split()
d = 0
for i in c:
    for j in i:
        if j.lower() in ['e','u']:
            d += 1 
print('Total number of e-u in the given file is :',d)
