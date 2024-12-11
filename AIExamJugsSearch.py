from AIExamJugs import Problem

def constructPath(node, visited):
    path = []
    action, parent = visited[node]
    while parent != None:
        path = [action] + path
        action, parent = visited[parent]
    return path

def bfs (p):
    frontier = [(p.startState(), None, None)]
    visited = {}

    while frontier:
        node, action, parent = frontier.pop(0)
        if node in visited: continue
        visited[node] = (action, parent)
        if p.isGoal (node): return constructPath(node, visited)
        nextStates = p.nextStates(node)
        for n, a in nextStates:
            frontier.append ((n, a, node))
    return None

p = Problem (12, 8, 3, 1)
plan = bfs(p)
print (plan)
