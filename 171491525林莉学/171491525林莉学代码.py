import queue
def dfs(adj, start):
    visited = set()
    stack = [[start, 0]]
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}


dfs(graph, 1)