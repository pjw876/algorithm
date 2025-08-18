N = int(input())

check = False
for i in range(1, 1000000):
    sum = 0
    sum += i
    for x in str(i):
        sum += int(x)
    if sum == N:
        print(i)
        check = True
        break

if check == False:
    print(0)


