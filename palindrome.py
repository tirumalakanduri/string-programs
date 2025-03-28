string = input(" enter the string : ")
if string == string[::-1]:
    print(f" the given {string} is a palindrome")
else:
    print(f"the given {string} is not a palindrome")
