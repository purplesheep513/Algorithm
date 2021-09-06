#1. visit에 각 노드가 다른 노드에 도달하는 방법의 최대거리를 넣는다.
#2. visit배열의 max값을 구한다.

#거리를 구할때는 한 덩이 한 덩이 세는 것과는 조금 다른 생각을 해야하는 것 같다.
#distance 배열에 해당 노드가 다른 노드에 도달하는 거리를 저장하면 주변 노드는 그 노드값만더해주면 되기 때문에 그런식으로 구하면 될 것 같다.

#생각하기 너무 어렵다. 더 생각해보고 내일 해결할 수 있도록 해야겠다.

import sys

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)] 


for _ in range(N-1):
    p,c,d = map(int,sys.stdin.readline().split())
    graph[p].append((c,d))
    graph[c].append((p,d))

def dfs(node,distance):
    
    if len(graph[node]) >1:
        
    else : return 0
