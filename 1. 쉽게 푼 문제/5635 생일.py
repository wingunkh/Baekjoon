n = int(input())
a = []

for _ in range(n):
    n, d, m, y = list(input().split())
    d, m, y = map(int, (d, m, y))
    a.append((n, d, m, y))

a.sort(key = lambda x: (x[3], x[2], x[1]))

print(a[-1][0])
print(a[0][0])
