n = int(input())

packets = []

for _ in range(n):
    t_i, i = [int(x) for x in input().split()]
    packets.append((i, t_i))


packets.sort()

t_now = 1
total_lag = 0

for _, t in packets:
    total_lag += max(t - t_now, 0)
    t_now = max(t_now, t) + 1

print(total_lag)