#Find Palindromes

numbers = [121, 45, 33, 77, 23, 5, 100]
strings = ['aws', 'radar', 'ansible']

for i in numbers:
    if str(i)==str(i)[::-1]:
        print(i)

for i in strings:
    if i ==i[::-1]:
        print(i)

check_p=input("enter a word : ")
is_palindrome=True
for i in range(len(check_p)//2):
    if check_p[i] != check_p[-(i+1)]:
        is_palindrome=False
        break

if is_palindrome:
     print(f"{check_p} is a palindrome")
else:
    print(f"{check_p} is not a palindrome")
