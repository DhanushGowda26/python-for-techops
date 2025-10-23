#Count and Print Even Numbers in Descending Order

nums = [12, 45, 2, 77, 23, 89, 5, 23, 77, 1, 100, 42, 84]
mynums=sorted(set(nums),reverse=True)
output=[]
count = 0
for i in mynums:
    if i%2==0:
        output.append(i)
        count+=1
print(f"even list = {output}")
print(f"even count = {count}")




