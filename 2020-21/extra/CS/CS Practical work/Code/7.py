a = input('Write a String :')
v = 0
c = 0
u = 0
l = 0

for i in a:
    if i.isupper() == True:
        u += 1
    else:
        l +=1
    if i.lower() in ['a','e','i','o','u']:
        v += 1
    else:
        c += 1
print('The number of vowels :',v)
print('The number of consonants :',c)  
print('The number of uppercase :',u) 
print('The number of lowercase :',l) 




