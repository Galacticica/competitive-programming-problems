def plusOne(digits: list[int]) -> list[int]:
    new_number = 0
    new_digits = []
    x = len(digits) - 1
    for digit in digits:
        n = digit * 10**x
        new_number = new_number + n
        x = x-1
    new_number = new_number + 1
    new_digits = [int(y) for y in str(new_number)]
    return new_digits



print(plusOne([int(x) for x in input().split()]))