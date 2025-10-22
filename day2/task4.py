#Password Validator

min_length=8
atleast_l=0
atleast_u=0
atleast_d=0
atleast_s=0

password=input("enter a password: ")

for i in password:
    if i.islower():
        atleast_l+=1
    elif i.isupper():
        atleast_u+=1
    elif i.isdigit():
        atleast_d+=1
    else:
        atleast_s+=1

if len(password)>=min_length and atleast_l >=1 and atleast_u >=1 and atleast_d >=1 and atleast_s >=1:
    print("password created")
else:
    print("password not created, should have : ")
    if len(password) < min_length:
        print("must have atleast 8 char")
    if atleast_l < 1:
        print("must have atleast 1 lowercase char")
    if atleast_u < 1:
        print("must have atleast 1 uperrcase char")
    if atleast_d < 1:
        print("must have atleast 1 digit")
    if atleast_s < 1:
        print("must have atleast 1 symbol")


