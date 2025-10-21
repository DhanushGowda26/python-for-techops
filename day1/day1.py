#1.print a statement
print("hello, world")

#2.print multipline statemnt
print("hello\nworld")

#3.variables of int
a=10
b=10
c=a+b
print(c)
print(type(c))


#4.variables of strings
tech="devops"
print(tech)
print(type(tech))

#5. even space(" ") is a char/string
tools="docker "
length_tools = len(tools)
print(length_tools)

#6.IF ELSE loop
if True:                      # True/False is boolean 
    print("^.^")

if 1+2 == 3:   #using comapring operator
    print("I got it correct")
else:
    print("I got it wrong")

day=input("enter today's day: ").lower()
if day in ("saturday","sunday"):  #here IN ckecks inside tuple
    print("it's Holiday")
elif day in ("monday",):             

#here if we wana use IN we need to make it tuple by keeping coma(,) or elif day == "monday"
    
    print("it's office time after holiday")
else:
    print("weekday")
    
# int + string not possible
# string + string possible
# string * int possible
name="python"
print(name + "3")
print(name * 3)










