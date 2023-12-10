# Example Python Code

def sum_of_even_numbers(numbers):
    """
    Calculate the sum of even numbers in a list.

    Parameters:
    - numbers (list): A list of integers.

    Returns:
    - int: The sum of even numbers in the list.
    """
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

# Example Usage
if __name__ == "__main__":
    # Sample list of numbers
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Calculate the sum of even numbers
    result = sum_of_even_numbers(number_list)

    # Display the result
    print(f"The sum of even numbers in the list is: {result}")
