import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global result
    
    q = deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        now, depth = q.popleft()

        if depth == 2:
            return

        for i in a[now]:
            if not visited[i]:
                q.append((i, depth + 1))
                visited[i] = True
                result += 1

n = int(input())
m = int(input())
a = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
result = 0

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

bfs()

print(result)
