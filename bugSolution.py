def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (this will now return 0):
my_numbers = []
average = calculate_average(my_numbers)
print(average)  # Output: 0

# Example with numbers
my_numbers = [10,20,30]
average = calculate_average(my_numbers)
print(average) # Output 20.0