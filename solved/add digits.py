def add_digits(num: int) -> int:
    global sum
    if len(str(num)) == 1:
        return (num)
    num = [int(x) for x in str(num)]
    while len(num) != 1:
        sum = 0
        for n in num:
            sum = sum + n
        num = [int(x) for x in str(sum)]
        print(num)
    return (sum)

print(add_digits(int(input())))