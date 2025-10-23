#list/array
tools=["aws","docker","k8s","terraform","ansible","cicd","openstack","kvm","quemu"]
cloud=["proxmox","aws","azure","gcp","oracle","openstack","e2e","truenas","ceph"]
print(F"cloud = {cloud}")
print(f"tools={tools}")
print(f"items in tools = {len(tools)}")
print(f"data type ={type(cloud)}")
print(f"accessing list = {cloud[0]}")
print(f"accessing list = {tools[5]}")

print(list(range(7))) # start with 0 and ends with n-1(7-1)
print(list(range(2,7))) # starts with 2(0 and 1 not present) and ends with n-1
print(list(range(0,10,2)))
# so to skip/step it does n-1, skip here it is 2 so 1 item it skips, default is 1 so 0 items it skips



for i in range(3,7):               # here i is assigned index via range
    print(cloud[i])
print("------------------------------")
for i in tools:                     # here i is the item/value
    print(i)
