import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    edges = []
    distance = [sys.maxsize for _ in range(n + 1)]
    is_cycle = False
    
    for _ in range(m):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))
        edges.append((e, s, w))

    for _ in range(h):
        s, e, w = map(int, input().split())
        edges.append((s, e, -w))

    for _ in range(n - 1):
        for s, e, w in edges:
            if distance[e] > distance[s] + w:
                distance[e] = distance[s] + w

    for s, e, w in edges:
        if distance[e] > distance[s] + w:
            is_cycle = True
            break

    if is_cycle:
        print("YES")
    else:
        print("NO")
