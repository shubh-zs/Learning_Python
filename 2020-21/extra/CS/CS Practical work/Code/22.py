import pickle
import os

def inse():
    o = open("std.bin","wb")
    i = int(input("How many records : "))
    for ii in range(i):
        a = int(input("Write the Roll number : "))
        b = input("Student's Name : ")
        c = input("Inititals of Subjects he has chosen : ")
        std_rec = {'Roll no' : a ,"Name" :b,"Sub" : c}
        pickle.dump(std_rec,o)
    o.close()


def show():
    o = open("std.bin","rb")
    
    while True:
        try:
            a = pickle.load(o)
            for i in a:
                print(i,":",a[i])
        except:
            break
    o.close()
    print('done')

def upd():
    o = open("std.bin","rb")
    o2 = open("temp.bin",'wb')
    d = pickle.load(o)
    d2 = {}
    n = input("Write old name : ")
    c = 0
    for i in d:
        if n == d["Name"]:
            c = 1
            d["Name"] = input("New Name : ")
            d['Roll no'] = input("New Roll no : ")
            d["Sub"] = input("New Subject : ")
        d2 = d.copy()
    if c == 1:
        pickle.dump(d2,o2)
        os.remove("std.bin")
        os.rename("temp.bin","std.bin")
    else:
        print("Given name isnt in the file")
upd()

