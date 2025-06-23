def get_middle(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]

print(get_middle("hello"))
print(get_middle("python"))
print(get_middle("otto"))
