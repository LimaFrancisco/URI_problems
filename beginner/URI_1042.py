list = [] * 3
sorted_list = [] * 3
list = input().split()

list = [int(val) for val in list] # converting

sorted_list.extend(list)
sorted_list.sort()

for val in sorted_list:
    print(val)

print("")

for val in list:
    print(val)
