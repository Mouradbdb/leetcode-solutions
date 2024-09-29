def findClosestNumber(numbers):
    closest = numbers[0]

    for num in numbers:
        if abs(num) < abs(closest) :
            closest = num
    if closest < 0 and abs(closest) in numbers:
        return abs(closest)
    else:
        return closest

print(findClosestNumber([-4, 2, 5, -1, 1])) # outupt 1

