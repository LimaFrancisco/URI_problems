values_list = [] * 100
bigger = 0

for item in range(0, 100):
    values_list.append(int(input()))
    if values_list[item] > bigger:
        bigger = values_list[item]
 
print(f"{bigger}\n{values_list.index(bigger) + 1}")   
