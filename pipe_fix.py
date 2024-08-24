def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))

nums = [1, 3, 5, 6, 7, 8]
output_pipes = pipe_fix(nums)
print(output_pipes)
