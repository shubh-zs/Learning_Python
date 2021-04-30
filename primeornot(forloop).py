#calculation of whether the number is prime or not using for loop
#Made by   Shourya Purohit
#Compiled on 2 may 2019


found=0

n=int(input('Enter the number here :'))

for x in range(2,n,1):
        if(n%x==0):
                found=1

if(found==0):

        print('Prime number')

else:

        print('Composite Number')
