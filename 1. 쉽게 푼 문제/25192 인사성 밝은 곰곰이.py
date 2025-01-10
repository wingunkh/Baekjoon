import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
result = 0

for _ in range(n):
    s = input().rstrip()

    if s == "ENTER":
        dic = dict()
    else:
        if s not in dic:
            result += 1
            dic[s] = 1

print(result)
