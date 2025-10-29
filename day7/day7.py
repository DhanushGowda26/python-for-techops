#leetcode problem
# https://leetcode.com/problems/score-of-a-string/submissions/

string="abcde"
count=0
for i in range(len(string)-1):
    a=ord(string[i]) - ord(string[i+1])
    count+=abs(a)
print(count)

# solution  in leetcode format

# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         count=0
#         for i in range(len(s)-1):
#             a=ord(s[i]) - ord(s[i+1])
#             count+=abs(a)
#         return count