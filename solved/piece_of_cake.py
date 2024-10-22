sl, h, v = input().split(' ')
sl = int(sl)
h = int(h)
v = int(v)

sizes = []
sizes.append(h*v*4)
sizes.append(h*(sl-v)*4)
sizes.append(v*(sl-h)*4)
sizes.append((sl-h)*(sl-v)*4)
sizes.sort()
print(sizes[-1])

