#Separate numbers and strings into two different lists.
#From the numbers list:
#Find numbers greater than 20.
#Print their count.
#From the strings list:
#Find words with more than 5 characters.
#Print the count of these words.
#Print all the results in a readable format.

items = [12, "aws", 45, "docker", 2, "kubernetes", 77, "terraform", 23, "ansible", 5]

string=[]
numbers=[]
count_str=0
count_20=0
for i in items:
    if isinstance(i,str):
        string.append(i)
        if len(i)>5:
            count_str+=1
    elif isinstance(i,int): 
        
        # elif number.append(i) modifyes numbers[] and returns none ---> elif none ---> elif block won't run
        
        numbers.append(i)
        if i > 20:
            count_20+=1




print(string)
print(numbers)
print(f"count_str={count_str}")
print(f"count_20={count_20}")
