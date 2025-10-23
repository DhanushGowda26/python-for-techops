#print common elements in 2 lists

cloud = ["proxmox","aws","azure","gcp","oracle","openstack","e2e","truenas","ceph"]
tools = ["aws","docker","k8s","terraform","ansible","cicd","openstack","kvm","quemu"]
common=[]
common_count=0

for i in cloud:
    if i in tools:
        common.append(i)
        common_count+=1


print(f"common elements = {common}")
print(f"common count = = {common_count}")



