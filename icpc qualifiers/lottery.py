n = int(input())
num_of_results = 10 * n
all_numbers = []
rigged = []

for i in range(num_of_results):
    new_numbers = (int(i) for i in input().split(' '))
    for num in new_numbers:
        all_numbers.append(num)

all_numbers.sort()
while len(all_numbers)>0:
    current_number = all_numbers[0]
    all_numbers.pop(0)
    counter = 1
    if current_number == all_numbers[0]:
        counter += 1
        all_numbers.pop(0)
    else:
        if counter > 2 * n:
            rigged.append(current_number)
            all_numbers.pop(0)



print(rigged)
