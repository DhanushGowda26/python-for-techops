word=input("enter a word : ").lower()
palindrome =True
for i in range(len(word)//2):
    if word[i] != word[-(i+1)]:
        palindrome = False
        break

if palindrome == True:
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
