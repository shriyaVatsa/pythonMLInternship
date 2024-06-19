def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]

total_sum = sum_of_list(numbers)

print("The sum of the list is:", total_sum)
