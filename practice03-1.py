# 사이클 찾는 방법에 대해 공부해야겠다 ㅠㅠ https://jackpot53.tistory.com/92
# 머리가 안 돌아가서 일단 조금 풀다가 공부하는중
import sys
sys.setrecursionlimit(111111)

# T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
graph = [0]+list(map(int, sys.stdin.readline().split()))
visit = [0 for _ in range(len(graph))]
cycle = []
own = []
def dfs(node):
    global graph, visit
    if node == graph[node]:
        own.append(node)
    if visit[node] != 1:
        visit[node] = 1
        dfs(graph[node])
    else : cycle.append(node)
    
for i in range(1,N):
    dfs(i)

print(set(cycle))