#count volwels
vowels=('a','e','i','o','u')
a=input("enter a word: ").lower()
count = 0
for i in a:
    if i in vowels:
        count+=1

print(f"total vowels = {count}")


#follow up 

count_dict={i : 0 for i in vowels}
for i in a:
    if i in vowels:
        count_dict[i]+=1

print(f"deatiled output = {count_dict}")
