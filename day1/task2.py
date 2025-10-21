#Largest of 3 Numbers
a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))

if a >= b and a >= c:
    print(f"{a} is greater")
elif b >= c:
    print(f"{b} is graeter")
else:
    print(f"{c} is greater")

# Follow up question

if a == b == c:
    print("all are equal")
else:
    if a>=b and a>=c:
        largest =a
        second=max(b,c)
    elif b>=a and b>=c:
        largest=b
        second=max(a,c)
    else:
        largest=c
        second=max(a,b)
        
    print(f"largest = {largest}")
    print(f"2nd largest = {second}")

