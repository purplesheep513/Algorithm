#1. visit에 각 노드가 다른 노드에 도달하는 방법의 최대거리를 넣는다.
#2. visit배열의 max값을 구한다.

#거리를 구할때는 한 덩이 한 덩이 세는 것과는 조금 다른 생각을 해야하는 것 같다.
#distance 배열에 해당 노드가 다른 노드에 도달하는 거리를 저장하면 주변 노드는 그 노드값만더해주면 되기 때문에 그런식으로 구하면 될 것 같다.

#생각하기 너무 어렵다. 더 생각해보고 내일 해결할 수 있도록 해야겠다.
#고민 고민 하다가 남들이 생각한 방식을 봤다. 가장 최대 distance의 리프노드를 구해주고 그곳에서 최대값을 구해주면 된다고 되어있었다. 이제 시험해 볼 것이다.

#드디어 알겠다. 최대지름은 최대 distance를 포함하고 있는 경로를 지날테니 그것의 리프노드를 구하고 거기서 최대값을 구하면 다른 리프노드로 도달할 것이다

import sys
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    parent_node, child_node, distance = map(int, sys.stdin.readline().split())
    graph[child_node].append((parent_node,distance))
    graph[parent_node].append((child_node,distance))

def dfs(node, fin):
    stack = []
    distance = [-1 for _ in range(N+1)]
    stack.append(node)
    distance[node] = 0
    while stack:
        node = stack.pop()
        for i,d in graph[node]:
            if distance[i] == -1 :
                stack.append(i)
                distance[i] = distance[node]+d
    if fin :
        return distance.index(max(distance))
    else :
        return max(distance)

print(dfs(dfs(1,True),False))