#sum of 1st N numbers
n=int(input("enter how many inputs : "))
total = 0
for i in range(1,n+1):
    a=int(input(f"enter number{i}: "))
    total+=a

print(f"Sum of {n} numbers is: {total}")



