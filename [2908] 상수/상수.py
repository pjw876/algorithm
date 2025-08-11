import sys
input = sys.stdin.readline

a, b = map(int, input()[::-1].split())
if a > b:
    print(a)
else:
    print(b)