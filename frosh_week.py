n, m = input().split(' ')

tasks = [int(i) for i in input().split(' ')]

quiet = [int(i) for i in input().split(' ')]

tasks.sort()
quiet.sort()


task_count = 0
while len(tasks) > 0 and len(quiet) > 0:
    if tasks[0] <= quiet[0]:
        task_count += 1
        tasks.pop(0)
        quiet.pop(0)
    else:
        quiet.pop(0)

print(task_count)