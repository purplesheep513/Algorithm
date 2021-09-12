import sys
N = int(sys.stdin.readline())
graph = [[]]
for i in range(1,N+1):
    m = list(map(int,sys.stdin.readline().split()))
    graph.append(m)

def dfs(n,end):
    