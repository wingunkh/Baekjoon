def backtracking(x, depth):
    if depth == 3:
        tmp = ""

        for i in stack:
            tmp += str(i)

        candidate.append(tmp)
        
        return

    for i in range(1, 10):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            backtracking(i, depth + 1)
            stack.pop()
            visited[i] = False

n = int(input())
visited = [False for _ in range(10)]
stack = []
candidate = []

backtracking(0, 0)

for _ in range(n):
    question, strike, ball = map(int, input().split())
    question = str(question)
    tmp = []

    for target in candidate:
        s, b = 0, 0
        
        for i in range(3):
            if target[i] == question[i]:
                s += 1
            elif target[i] in question:
                b += 1

        if s == strike and b == ball:
            tmp.append(target)

    candidate = tmp
            
print(len(candidate))
