import sys
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    m = list(map(int,sys.stdin.readline().split()))
    for j in range(len(m)):
        if j % 2 != 0 and m[j] !=-1:
            graph[m[0]].append((m[j],m[j+1]))
print(graph)
visit = [-1 for _ in range(N+1)]
def dfs(n,end):
    visit[n] = 0
    stack = []
    stack.append(n)
    while stack:
        n = stack.pop()
        for i,d in graph[n]:
            if visit[i] != -1 :
                visit[i] = visit[n]+d
