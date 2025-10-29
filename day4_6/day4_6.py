import os

dirs = ["data", "logs", "output", "configs"]

for i in dirs:
    if not os.path.exists(i):
        os.makedirs(i)

#alert if cpu and ram is 80% usage or print current usage

import psutil   
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent

if cpu_usage > 80:
    print("CPU usage is above 80%")
else:
    print(f"CPU usage is {cpu_usage}")


if ram_usage > 80:
    print("RAM usage is above 80%")
else:
    print(f"RAM usage is {ram_usage}")

s="madam"
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

s="madam"
palindrome=True
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        palindrome=False
if palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")

so="madam"
n=len(so)//2    
m=n*2
for i in range(n):
    print(so[i],so[m-i-1])


def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
tables=int(input("Enter a number to print its multiplication table: "))
table(tables)