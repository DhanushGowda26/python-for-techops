#Take marks for 5 subjects from the user.

english=float(input("enter english marks : "))
kannada=float(input("enter kannada marks : "))
social=float(input("enter socaial marks : "))
maths=float(input("enter maths marks : "))
science=float(input("enter science marks : "))

print(f"total marks = {sum([english,kannada,social,maths,science])}")
print(f"avarage = {sum([english,kannada,social,maths,science])/5}")


