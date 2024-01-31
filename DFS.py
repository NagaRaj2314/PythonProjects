# Creation of graph
graph = {
    '1': set(['2', '3', '4']),
    '2': set(['1', '5', '6']),
    '3': set(['1']),
    '4': set(['1', '7', '8']),
    '5': set(['2', '9', '10']),
    '6': set(['2']),
    '7': set(['4', '11', '12']),
    '8': set(['4']),
    '9': set(['5']),
    '10': set(['5']),
    '11': set(['7']),
    '12': set(['7'])
}

# Implementation of DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end=" ")
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

## Calling the function
print("Following is the Depth-First Search")
dfs(graph, '1')
