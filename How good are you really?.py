def better_than_average(class_points, your_points):
    sum_class = 0
    for i in class_points:
        sum_class += i
    mid_score = sum_class / len(class_points)
    print(mid_score)
    if mid_score < your_points:
        return class_points, your_points, True
    else:
        return class_points, your_points, False





print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))