f = open("Places.txt","r")
a = f.readlines()
print("Every line in the file RN :")
for i in a:
    print(i)
print("Lines starting with P or S : - ")
for i in a:    
    if i[0] in ["P", "S","p","s"]:
        print(i)
