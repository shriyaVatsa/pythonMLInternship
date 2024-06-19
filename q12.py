def fibonacci_sequence(n):

    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_numbers = fibonacci_sequence(n)
print("Fibonacci sequence:", fibonacci_numbers)
