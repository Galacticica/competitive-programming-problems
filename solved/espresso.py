n, s = input().split(' ')
#n, s = [int(x) for x in input().split()]
orders = []
for i in range(int(n)):
    orders.append(input())
refills = 0
tank = int(s)
for i in orders:
    if len(i) == 2:
        oz = int(i[0]) + 1
    else:
        oz = int(i[0])
    
    if tank >= oz:
        tank -= oz
    else:
        refills += 1
        tank = int(s)
        tank -= oz
print(refills)
    