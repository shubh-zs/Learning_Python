def PushS(l):
    print("Orignal list",l)
    a = int(input('Write a number : '))
    l.append(a)
    print(l)

l = [1,2,3,4,5]
PushS(l)

def PopS(l):
    print("Orignal list",l)
    l.pop()
    print(l)

l = [1,2,3,4,5]
PopS(l)