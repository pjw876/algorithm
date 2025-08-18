import sys

input = sys.stdin.readline

N, M = map(int, input().split())

n_list = list(map(int, input().split()))

result = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result.append(n_list[i]+n_list[j]+n_list[k])

result.sort(reverse=True)

for x in result:
    if x <= M:
        print(x)
        break