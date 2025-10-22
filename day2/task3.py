#Number Type Detector
#Positive, Negative, or Zero
#Divisible by both 3 and 5

num1=float(input("enter a number : "))
if num1 > 0:
    print(f"{num1} is positive number")
elif num1 < 0:
    print(f"{num1} is negative number")
else:
    print(f"It's a zero (0)")



if num1%3==0 and num1%5==0:
    print(f"{num1} is divisble by both 3 and 5")
else:
    print(f"{num1} is not divisble by both 3 and 5")

