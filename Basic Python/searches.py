from collections import deque

def bfs(graph, start):
    visited = set()  
    queue = deque([start])  

    while queue:
        node = queue.popleft()  
        
        if node not in visited:
            visited.add(node)  
            print(node, end=" ")  

            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor) 


graph_bfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}
print("BFS Traversal :")
bfs(graph_bfs, 'A')  









# dfs

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  
    
    visited.add(start)  
    print(start, end=" ")  
    
   
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph_dfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}
print("\n")
print("DFS Traversal :")
dfs(graph_dfs, 'A')  
