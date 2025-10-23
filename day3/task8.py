#Separate numbers and strings into two different lists.
#From the numbers list:
#Find even numbers and odd numbers separately.
#Print their count.
#Find the sum of even numbers.
#From the strings list:
#Find strings longer than 4 characters.
#Count how many start with the letter 'a'
items = [12, "AWS", 45, "docker", 2, 23.1,33.3,0.87,99.9,"kubernetes", 77, "terraform", 23, "ansible", 5, "ci", 100]

numbers=[]
even_numb=[]
odd_numb=[]
strings=[]
total_strings=0
strings_4=[]
count_a=0
for i in items:
    if isinstance(i,str):
        strings.append(i)
        total_strings+=1
        if len(i) > 4:
            strings_4.append(i)
        if i.lower().startswith("a"):
            count_a+=1

    elif isinstance(i,(int,float)):
        numbers.append(i)
        if i%2==0:
            even_numb.append(i)
        else:
            odd_numb.append(i)

print(f"numbers = {numbers}")
print(f"string = {strings}")
print(f"total strings = {total_strings}")
print(f"strings > 4 char = {strings_4}")
print(f"even = {even_numb}")
print(f"odd = {odd_numb}")
print(f"string starts with 'a' = {count_a}")
even_sum=0
for i in even_numb:
    even_sum+=i

print(f"sum of even = {even_sum}")







