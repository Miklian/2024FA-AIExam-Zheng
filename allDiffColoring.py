#Problem
graph = {
        'A' : ['B','C'], 
        'B' : ['A','D'],
        'C' : ['A','D','E'],
        'D' : ['B','C','F'],
        'E' : ['C','F'],
        'F' : ['E','D']  
}
#[A][B]
#[C][D]
#[E][F]

colors = ['Red', 'Blue', 'Green', 'Yellow']

def can_color(node, color, coloring, graph):
    for neighbor in graph[node]:
        if coloring.get(neighbor) == color:
            #if neighbor's color is same as node
            return False
    return True

#BFS
def bfs(graph):
    frontier = [('A')]
    coloring = {}

    while frontier:
        node = frontier.pop(0)

        for color in colors:
            if can_color(node, color, coloring, graph):
                coloring[node] = color
                #first color one node
                break
        for neighbor in graph[node]:
            if neighbor not in coloring:
                #append to queue if neighbor hasn't been colored yet
                frontier.append(neighbor)
    
    return coloring

coloring = bfs(graph)
print("Different map colors:")
for node, color in coloring.items():
    print(f"Node {node}: Color {color}")
