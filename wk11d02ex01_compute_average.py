def computeAverage(numbers):
    total = 0
    count = 0

    for num in numbers:
        if num == 0:
            return total / count
        else:
            total = total + num
            count = count + 1

    return total / count


# Test cases
print(computeAverage([22, 9, 0, 17]))
print(computeAverage([22, 0, 49, 8]))
print(computeAverage([35, 13, 22, 0]))
print(computeAverage([10, 5, -4, 27]))
