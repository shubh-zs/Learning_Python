import pickle
i = open("std.bin","rb")
c =[]
q = 1
while True:
    try:
        p = pickle.load(i)
        c.append(p["Roll no"])
    except:
        break
print(1, ":", c)

p = pickle.load(i)
for ii in p:
    if q in ii["Roll no"]:
            p["Roll no"] = int(input("Write new Roll no : "))
            print('done')
            break
        else:
            print("continued")
            continue
    except:
        break

while True:
    try:
        p = pickle.load(i)
        c.append(p["Roll no"])
    except:
        break

print(2, ":" , c)
i.close()

