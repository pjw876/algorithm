import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

max = 0
for i in range(9):
    for j in range(9):
        if max < arr[i][j]:
            max = arr[i][j]
print(max)

for i in range(9):
    for j in range(9):
        if max == arr[i][j]:
            print(i+1, j+1)
            break