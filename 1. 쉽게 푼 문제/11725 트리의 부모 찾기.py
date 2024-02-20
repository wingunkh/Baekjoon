import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)

n = int(input())
a = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
parent = [0 for i in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])
