numbers = [13, 2, 34, 54, 12, 23, 10]

length = len(numbers)

min_val = numbers[0]
max_val = numbers[0]

for i in range(length):
    if numbers[i] > max_val:
        max_val = numbers[i]

for i in range(length):
    if numbers[i] < min_val:
        min_val = numbers[i]

print("The maximum value in the list is", max_val)
print("The minimum value in the list is", min_val)
