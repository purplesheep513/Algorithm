import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    answer = set()
    graph = list(map(int, sys.stdin.readline().split()))
    graph.insert(0,0)

    def dfs(n) :
        visit = [ 0 for _ in range(len(graph))]
        visit.insert(0,-1)
        stack = []
        visit[n] = 1
        stack.append(n)

        while stack:
            n = stack.pop()
            if visit[graph[n]] == 1:#사이클o
                answer.add(n)
            elif visit[graph[n]] == 0:#방문을 아직 안 한 것
                visit[graph[n]] = 1
                stack.append(graph[n])

    for i in range(1,N+1):
        dfs(i)

    print(N-len(answer))