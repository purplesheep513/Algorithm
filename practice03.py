#사이클인 노드들이 팀을 이루는 것이길래 사이클만 빼주려고 했는데 왜 시간초과가 되는 것일까... 무엇이 문제인것일까
#

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    answer = set()
    graph = [0]+list(map(int, sys.stdin.readline().split()))
    visit = [-1]+[ 0 for _ in range(len(graph))]
    def dfs(n) :
        stack = []
        visit[n] = 1
        stack.append(n)
        if n==graph[n]: # 자신이면 넣지말고 뺀다
            answer.add(n)
            stack.pop()
        while stack:
            n = stack.pop()
            if n == graph[n] : # 자신일경우
                answer.add(n)
            elif visit[graph[n]] == 1:#사이클o
                answer.add(n)
            elif visit[graph[n]] == 0:#방문을 아직 안 한 것
                visit[graph[n]] = 1
                stack.append(graph[n])

    for i in range(1,N+1):
        if visit[i] == 0 :
            dfs(i)

    print(N-len(answer))