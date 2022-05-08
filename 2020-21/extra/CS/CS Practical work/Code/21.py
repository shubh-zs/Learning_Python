import csv
def inse():
    a = []
    s = open('student.csv',"a")
    name = input("Write a name : ")
    roll_no = int(input("Write a Roll no : "))
    a = [roll_no,name]
    csv_wr = csv.writer(s)
    csv_wr.writerow(a)
    print('Done')
    s.close()
    menu()


def m_inse():
    o = int(input("How many records : "))
    for i in range(o):
        b = []
        s = open('student.csv',"a")
        roll_no = int(input("Write a Roll no : "))
        name = input("Write a name : ")
        b = [roll_no,name]
        csv_wr = csv.writer(s)
        csv_wr.writerow(b)
        print('Done')
        s.close()
    menu()

def display():
    s = open('student.csv',"r")
    csv_r = csv.reader(s)
    for i in csv_r:
        print(i)
    menu()
    
def menu():
    print(print("."*118))
    print('Menu')
    print('Choose the Sno writtten against the function you wanna perform')
    print("Sno   Function","1.    Add Record","2.    Add Records","3.    Show Records", sep="\n")
    i = int(input("Choose a function : "))
    if i in [1,2,3]:
        if i == 1:
            inse()
        if i == 2:
            m_inse()
        if i == 3:
            display()
    else:
        print("Error")
menu()




