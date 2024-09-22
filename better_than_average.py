def better_than_average(class_points, your_points):
    average = (sum(class_points)+your_points)/(len(class_points) + 1)
    print(average)
    print(len(class_points))
    print(sum(class_points)+your_points)
    if your_points > average:
        return True
    False


class_points = [7,9,10,8]
your_points = 9

print(better_than_average(class_points, your_points))
#print(len(num))