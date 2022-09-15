import random
res_list = []
for i in range(0,10):
    res_list.append(random.randint(-200,200))
copy_list = res_list
a = res_list[0]
print(res_list)
while(1):
    if not (max(res_list) % 2 == 0):
        res_list.remove(max(res_list))
        if not res_list:
            print(a)
            break
    else: break
if res_list:
    print(max(res_list))
copy_list.sort(reverse = True)
print(copy_list)