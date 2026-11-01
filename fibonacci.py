# Generator function for Fibonacci series
def fibonacci_generator(limit):

    # Initialize first two Fibonacci numbers
    a = 0
    b = 1

    # Generate numbers up to the given limit
    for i in range(limit):

        # Yield the current Fibonacci number
        yield a

        # Calculate the next Fibonacci number
        a, b = b, a + b


# Call the generator function
fib = fibonacci_generator(10)

# Display Fibonacci series
print("Fibonacci Series:")

for number in fib:
    print(number)