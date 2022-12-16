n = int(input())
logs = []
counter = 0
for i in range(n):
    row = input()
    numbers = map(int, row.split())
    logs.append(list(numbers))


for i in range(len(logs)):
    if i == len(logs) - 1:
        if logs[-1] > logs[-2]:
            counter += 1
    else:
        if logs[i + 1] > logs[i]:
            counter += 1
            
print(counter)