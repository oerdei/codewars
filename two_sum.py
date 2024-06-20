def two_sum(numbers, target):
    # Create a dictionary to store the indices of the elements
    seen = {}
    
    # Iterate over the array
    for i, number in enumerate(numbers):
        # Calculate the complement that when added to the current number equals the target
        complement = target - number
        
        # Check if the complement is already in the dictionary
        if complement in seen:
            # If it is, return the indices of the complement and the current number
            return (seen[complement], i)
        
        # Otherwise, add the current number to the dictionary
        seen[number] = i

# Test cases
print(two_sum([1, 2, 3], 4))  # Output: (0, 2) or (2, 0)
print(two_sum([3, 2, 4], 6))  # Output: (1, 2) or (2, 1)
print(two_sum([3, 3], 6))     # Output: (0, 1) or (1, 0)
