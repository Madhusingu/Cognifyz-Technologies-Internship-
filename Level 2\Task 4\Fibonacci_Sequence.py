def generate_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    elif n == 1:
        print("Fibonacci sequence:")
        print("0")
    elif n == 2:
        print("Fibonacci sequence:")
        print("0, 1")
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)
        print("Fibonacci sequence:")
        print(", ".join(map(str, fib_sequence)))

try:
    terms = int(input("Enter the number of terms: "))
    generate_fibonacci(terms)
except ValueError:
    print("Invalid input. Please enter an integer.")
