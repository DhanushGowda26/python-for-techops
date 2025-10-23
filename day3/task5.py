# Create a new list containing only words with more than 5 characters.

words = ["aws", "docker", "kubernetes", "terraform", "ansible", "ci", "openstack", "kvm", "quemu"]
output=[]
count=0
for i in words:
    if len(i)>5:
        output.append(i)
        count+=1

print(f"words with  more than 5 chars = {output}")
print(f"total item in output {count}")





