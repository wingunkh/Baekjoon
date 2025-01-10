import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse = True)

print(*a, sep = "\n")
