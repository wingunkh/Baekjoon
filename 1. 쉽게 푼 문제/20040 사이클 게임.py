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
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(1, m + 1):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(i)
        break
    else:
        union(a, b)
else:
    print(0)
