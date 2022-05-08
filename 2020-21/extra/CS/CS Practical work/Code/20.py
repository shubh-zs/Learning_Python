def insertQ(l):
    print("Orignal list",l)
    a = int(input('Write a number : '))
    l.insert(0,a)
    print(l)

l = [1,2,3,4,5]
insertQ(l)

def RemoveQ(l):
    print("Orignal list",l)
    a = l.pop(0)
    print(l)

l = [1,2,3,4,5]
RemoveQ(l)