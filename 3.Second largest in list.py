numbers=[10,20,4,45,99]

largest=second_largest=float('-inf')#initially

for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        num=second_largest
        
if second_largest==float('-inf'):
     print("second largest not found list contains fewer then 2 elements")
else:
    print ("second largest: ",second_largest)