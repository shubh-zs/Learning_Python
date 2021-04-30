#calculation of whether the number is prime or not
#Made by   Shourya Purohit
#Compiled on 2may 2019
found=0
n=int(input('Enter a number :'))
x=1
while(x<(n-1)):
        x=x+1
        if(n%x==0):
                found=1
if(found==0):
        print('Prime Number')
else:
        print('Composite Number')
