def is_even(n):
    # Check if the number is an integer or float with a decimal part equal to zero
    if isinstance(n, int) or (isinstance(n, float) and n.is_integer()):
        # Check if the number is even
        return n % 2 == 0
    else:
        # For floats with a non-zero decimal part, consider them as uneven
        return False

# Test cases
print(is_even(4))      # True
print(is_even(3))      # False
print(is_even(-6))     # True
print(is_even(0))      # True
print(is_even(3.0))    # False
print(is_even(4.5))    # False
