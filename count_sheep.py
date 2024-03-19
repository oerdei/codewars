def count_sheep(sheep_array):
    # Check if the input is valid (not None)
    if sheep_array is None:
        return "Invalid input: Array is None"

    # Use a list comprehension to count the number of True values
    count_true = sum(1 for sheep in sheep_array if sheep is True)

    return count_true

# Example usage
sheep_array = [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, False, False, True, True]
result = count_sheep(sheep_array)
print(f"The number of sheep present is: {result}")

