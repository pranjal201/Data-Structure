# Graph is a collection of nodes
# One element can be connected with many other elements

# Classification of Graphs
# 1.  Directed / Unidirected
# 2. Undirected/ Bi-directional
# https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/862227317/

# have to learn this technique

edges = [[0,1],[1,2],[2,0]]
n = len(edges)
graph = [[] for _ in range(n)]
for s,e in edges:
    graph[s].append(e)
    graph[e].append(s)
    print(graph)

print('Pranjal')
visited = [False for _ in range(n)]
print(visited)
