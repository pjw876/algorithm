arr = []
for _ in range(9):
    arr.append(int(input()))

max = max(arr)
print(max)
for i in range(9):
    if max == arr[i]:
        print(i+1)
        break

