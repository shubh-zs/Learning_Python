import pickle
i = open("book.dat","bw")

k = int(input("How many records : "))
for ii in range(k):
    a = int(input("Write Bookno : "))
    b = input("Write Book name : ")
    j = {a : b}
    pickle.dump(j,i)
i.close()