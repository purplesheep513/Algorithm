import sys
T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph.insert(0,0)
for i in graph:
    if i == graph[i]:
        graph[i] = 0
def dfs(n) :
    visit = [ 0 for _ in range(len(graph))]
    visit.insert(0,-1)
    stack = []
    visit[n] = 1
    stack.append(n)

    while stack:
        N = stack.pop()
        if visit[graph[N]] == 0:
            visit[graph[N]] = 1
            stack.append(graph[N])
        elif visit[graph[N]] == -1 :
            print('no cycle')
            print(visit)
        else :
            print('cycle')
            print(visit)

dfs(1)