#Top 3 Largest Numbers in a List


nums = [12, 45, 2, 77, 23, 89, 5, 23, 77, 1]

mynum=sorted(set(nums))

print(mynum)
print(f" top 3 largest number = {mynum[-1:-4:-1]}")  # here -1 as step because default step is left to right of +1
