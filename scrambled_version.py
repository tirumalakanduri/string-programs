s1 = input("enter the first string : ")
s2 = input("enter the second string : ")
if sorted(s1) == sorted (s2):
    print("scrambled version : true")
else:
    print("scrambled version : false")