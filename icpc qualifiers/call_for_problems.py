#SOLVED
n = int(input())
d = []
odd_problems = 0
for i in range (n):
    d.append(int(input()))

for num in d:
    if num % 2 != 0:
        odd_problems += 1

print (odd_problems)