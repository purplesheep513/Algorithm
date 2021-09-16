# 사이클 찾는 방법에 대해 공부해야겠다 ㅠㅠ https://jackpot53.tistory.com/92
# 머리가 안 돌아가서 일단 조금 풀다가 공부하는중
# 왜ㅐㅐㅐㅐ 시간초과가 날까 계속해서 ㅠㅠ
import sys
sys.setrecursionlimit(111111)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    graph = [0]+list(map(int, sys.stdin.readline().split()))
    visit = [0 for _ in range(N+1)]
    cycle = []
    own = set()
    def dfs(node):
        if node == graph[node] :
            own.add(node)
        if visit[node] != 1:
            visit[node] = 1
            dfs(graph[node])
        elif graph[node] in cycle:
            cycle.append(node)
        elif visit[node] == 1 and graph[node] not in own: 
            cycle.append(node)
        
    for i in range(1,N+1):
        dfs(i)

    print(N-len(cycle)-len(own))