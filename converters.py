def lbs_to_kg(weight):
    return weight * 0.45


def kgs_to_lbs(weight):
    return weight / 0.45


def find_max(numbers):
    max1 = numbers[0]
    for num in numbers:
        if num >  max1:
            max1 = num
    return max1 