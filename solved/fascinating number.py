n = int(input())
n2 = 2*n
n3 = 3*n
full_number = (str(n) + str(n2) + str(n3))
full_number = list(str(full_number))
print (full_number)
unique_numbers = []
isFascinating = True
for number in full_number:
    if number in unique_numbers:
        print("already used")
        isFascinating = False
        break
    elif number == '0': 
        print("no 0s")
        isFascinating = False
        break
    else:
        unique_numbers.append(number)
print(isFascinating)