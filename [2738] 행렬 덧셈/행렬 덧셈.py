N, M = map(int, input().split())
arr = []
arr2 = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(N):
    arr2.append(list(map(int, input().split())))

result = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(arr[i][j]+arr2[i][j])
    result.append(temp)

for i in result:
    for j in i:
        print(j, end=" ")
    print()