def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    count = len(numeric_numbers)
    return total / count

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [1, 2, 3, "a", 4]
average = calculate_average(my_list)
print(f"The average is: {average}")
