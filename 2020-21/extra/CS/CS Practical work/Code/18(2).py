import pickle
i = open("book.dat",'br')
b = int(input("Write the book number : "))
while True:
    try:
        a = pickle.load(i)
        for ii in a:    
            if ii == b:
                print(ii ,':', a[ii])
    except:
        break
i.close()


print("Done")