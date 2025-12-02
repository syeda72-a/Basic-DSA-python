#find max and min in list
numbers = [10, 25, 3, 47, 6, 2, 15]

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Maximum:", max_value)
print("Minimum:", min_value)