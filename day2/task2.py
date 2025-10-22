#Simple Calculator


number1=float(input("enter a number : "))
number2=float(input("enter a number : "))
oper=input("choose : +,-,*,/,% and ** : ")
if oper == "+":
    result = number1+number2
    print(result)
elif oper == "-":
    result = number1-number2
    print(result)
elif oper == "*":
    result=number1*number2
    print(result)
elif oper == "/":
    result = number1/number2
    print(result)
elif oper == "**":
    result = number1**number2
    print(result)
elif oper == "%":
    result = number1%number2
    print(result)
else:
    print("choose operator correctly")

