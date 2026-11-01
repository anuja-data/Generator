# Generator function to generate even numbers
def even_number_generator(start, end):

    # Iterate through the given range
    for number in range(start, end + 1):

        # Check whether number is even
        if number % 2 == 0:

            # Return the value one at a time
            yield number


# Call generator function
even_numbers = even_number_generator(1, 20)

# Display even numbers
print("Even Numbers:")

for num in even_numbers:
    print(num)