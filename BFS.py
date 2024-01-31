graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
def bfs(graph, start):
    visited = []  
    queue = []    
    visited.append(start)
    queue.append(start)
    print("Following is the Breadth-First Search:")
    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
# Starting BFS from node '5'
bfs(graph, '5')
