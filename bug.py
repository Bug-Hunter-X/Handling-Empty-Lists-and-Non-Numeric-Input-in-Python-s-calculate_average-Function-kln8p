def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return total / count

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#This is fine for empty list, but what about non-numeric values?