num = int(input("Enter an integer: "))
sum_of_digits = 0

while num > 0:

    digit = num % 10

    sum_of_digits += digit

    num //= 10

print("The sum of digits is", sum_of_digits)
