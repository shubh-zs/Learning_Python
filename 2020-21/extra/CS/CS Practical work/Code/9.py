a = input('Write a String :')
if a[::-1].lower() == a.lower():
    print("Its a palindrome")
else:
    print("It is not a palindrome")
