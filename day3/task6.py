#Sum of Multiples of 3 or 5


nums = list(range(1, 51))

count =0

for i in nums:
    if i%3==0 or i%5==0:
        count+=i


print(f"sum of multiples of 3 ot 5 between 1 to 50 = {count}")

