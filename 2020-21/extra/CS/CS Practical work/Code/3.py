
def mini_calc():
    print("."*100)
    print('Mini calculator')
    print("Select the serial number against the options provided below")
    print("1. Area of Circle","2. Area of Square", '3. Area of Rectangle',sep= "\n")
    a = int(input('What do you want to calculate :'))
    def circ():
        i = 'n'
        r = int(input('Radius of Circle :'))
        A = 3.14*(r**2)
        print("Area is :",A,"unit**2")
        i = input(("Want to use more features? (y/n)"))
        if i == "y":
            mini_calc1()
        else:
            print('Thanks for using out programme')
            
    

    def sqr():
        a = int(input('Side of Square :'))
        A = 4*(a**2)
        print("Area is :",A,"unit**2")
        i = input(("Want to use more features? (y/n)"))
        if i == "y":
            mini_calc1()
        else:
            print('Thanks for using our programme')
            
        



    def rec():
        l = int(input('Length of Rectangle :'))
        b = int(input('Breadth of Rectangle :'))
        A = 2*(l*b)
        print("Area is :",A,"unit**2")
        i = input(("Want to use more features? (y/n)"))
        if i == "y":
            mini_calc1()
        else:
            print('Thanks for using our programme')
            
            


    if a in [1,2,3]:
        if a == 1:
            circ()
        if a == 2:
            sqr()
        if a == 3:
            rec()
    else :
        print("Error : Please provide a number according to the serial number provided against the feature you want to use")

def mini_calc1():
    print("Select the serial number against the options provided below")
    print("1. Area of Circle","2. Area of Square", '3. Area of Rectangle',sep= "\n")
    
    a = int(input('What do you want to calculate :'))
    def circ():
        r = int(input('Radius of Circle :'))
        A = 3.14*(r**2)
        print("Area is :",A,"unit**2")
        i = input(("Want to use more features? (y/n)"))
        if i == "y":
            mini_calc1()
        else:
            print('Thanks for using our programme')
            
        

    def sqr():
        a = int(input('Side of Square :'))
        A = 4*(a**2)
        print("Area is :",A,"unit**2")
        i = input(("Want to use more features? (y/n)"))
        if i == "y":
            mini_calc1()
        else:
            print('Thanks for using our programme')
            


    def rec():
        l = int(input('Length of Rectangle :'))
        b = int(input('Breadth of Rectangle :'))
        A = 2*(l*b)
        print("Area is :",A,"unit**2")
        i = input(("Want to use more features? (y/n)"))
        if i == "y":
            mini_calc1()
        else:
            print('Thanks for using our programme')

        


    if a in [1,2,3]:
        if a == 1:
            circ()
        if a == 2:
            sqr()
        if a == 3:
            rec()
    
        print("Error : Please provide a number according to the serial number provided against the feature you want to use")    




mini_calc()
