arr=[1,2,3,3,4,1,5,5]

unique_list=[]
for num in arr:
    if num not in unique_list:
        unique_list.append(num)
        
print(unique_list)