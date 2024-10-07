#SOLVED
bears = int(input())
ordered_pairs = []
barriers = []
for bear in range(bears):
    x1, y1, x2, y2 = input().split(' ')
    ordered_pairs.append([int(x1), int(y1), int(x2), int(y2)])

for pair in ordered_pairs:
    if (pair[0] == 0 or pair[2] == 0) or ((pair[0]>0 and pair[2]<0) or (pair[0]<0 and pair[2]>0)):
        slope = (pair[3] - pair[1]) / (pair[2] - pair[0])
        barrier_point = pair[1] + (slope*(0-pair[0]))
        if barrier_point > 0:
            barriers.append(barrier_point)

barriers.sort()
if barriers == []:
    print(-1.0)
else:
    print(barriers[0])


