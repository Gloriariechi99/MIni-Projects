def lbs_to_kg(weight):
    return weight * 0.45


def kgs_to_lbs(weight):
    return weight / 0.45


def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num >  max:
            max = num
    return max 