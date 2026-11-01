# Generator function to generate numbers
def generate_numbers():

    # Generate numbers from 1 to 10
    for i in range(1, 11):
        yield i


# Store generator object
result = generate_numbers()

# Display generated numbers
for value in result:
    print(value)