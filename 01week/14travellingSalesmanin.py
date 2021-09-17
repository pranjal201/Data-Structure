# in this we have a weighted graph
#applying the brute force method
# time complexity -- O(n!)


from sys import maxsize
from itertools import permutations
V =4
s=0
def tsp(graph, s):

    # storing all the vertex apart from the source vertex
    vertex = []
    for i in range(V):
        vertex.append(i)

    #store minmum weight hamiltonian cycle
    min_path = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:

        current_pathweight = 0

        k=s
        for j in i:
            current_pathweight += graph[k][j]
            k=j
        current_pathweight += graph[k][s]

        #update minimum
        min_path = min(min_path, current_pathweight)
    return min_path
    
if __name__ == '__main__':

    graph = [[0, 10,15,20],
            [10, 0, 35, 25],
            [15,35 , 0,30],
            [20, 25, 30, 0]]


    for i in graph:
        print(i)


    print("Min Cost= ",tsp(graph,s))
