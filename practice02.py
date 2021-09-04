# 1.@.9.@.6.@.7.@. 트.@.리.@.의.@. 지.@.름.@.
# 최단거리나 덩어리 개수만 구해보다가 최장거리는 감이 잡히지 않아 검색을 열심히 해본 결과

#최장거리 구하는 방법: 아무 정점에서 임의의 정점까지의 거리를 구하고 그 중 가장 먼 거리를 가지는 도착지를 시작지점으로 하여 다시 한번 거리를 구하여 가장 긴 것을 찾으면 된다. 이는 증명된 방법으로 항상 참이다.

#라는 법칙이 있다고 한다. 새로운것을 배웠다. 내일(2021-09-04) 다시 살펴볼 것이다.
#아래는 내가 짰다가 오답낸 코드이다. 틀린코드지만 알고 나서 다시 보면 내가 무엇을 틀렸는지 알 수 있을 것같다.
#괜히 틀린코드 볼까봐 서치를 방지하기위해 저렇게 씀 검색안되겠지?

import sys

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)] 

for _ in range(N-1): 
    p, c, d = map(int, sys.stdin.readline().split()) 
    graph[p].append((c,d)) 
    graph[c].append((p,d))


def dfs(x,y):
    stack = []
    visit = [0 for _ in range(N+1)]
    dist = 0
    stack.append(graph[x][y])
    while stack:
        next_node, di = stack.pop()
        if visit[next_node] != 1:
            visit[next_node] = 1
            for i in range(len(graph[next_node])):
                if visit[i] != 1:
                    visit[i] = 1
                    dist += di
                    stack.append(graph[next_node][i])
    return dist

sum = 0
for i in range(N+1):
    if len(graph[i]) == 1:
        sum = max(dfs(i,0),sum)

print(sum)