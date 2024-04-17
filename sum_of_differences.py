def sum_of_differences(arr):
    if arr == [] or len(arr) == 1:
        return 0
    else:
        sorted_arr = sorted(arr, reverse=True)
        print(sorted_arr)
        i = 1
        s = 0
        while i < len(arr):
            s = s + sorted_arr[i-1] - sorted_arr[i]
            i = i + 1
        return s    
            






arr = [2, 1, 10]
print(sum_of_differences(arr))