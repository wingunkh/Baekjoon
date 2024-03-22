import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])

        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]
result = 0

edges.sort(key = lambda x: x[2])

for start, end, weight in edges:
    start = find(start)
    end = find(end)

    if start == end:
        continue

    union(start, end)
    result += weight

print(result)
