# Day 8: Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/    

operations = ["--X","X++","X++"]
x=0
for i in operations:
    if i == "X++" or i == "++X":
        x+=1
    elif i == "X--" or i == "--X":
        x-=1

# leetcode solution format
# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         x=0
#         for i in operations:
#             if i == "X++" or i == "++X":
#                 x+=1
#             elif i == "X--" or i == "--X":
#                 x-=1
#         return x

#2nd problem
#https://leetcode.com/problems/defanging-an-ip-address/

address="1.1.1.1"
for i in address:
    if i=='.':
        address=address.replace('.','[.]')
        break
print(address)

# leetcode solution format
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         for i in address:
#             if i=='.':
#                 address=address.replace('.','[.]')
#                 break
#         return address        

#pronlem 3
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

head = [1,1,2]
for i in head:
    if head.count(i)>1:
        head.remove(i)
print(head)
