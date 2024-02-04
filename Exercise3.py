import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.vertices[from_vertex][to_vertex] = weight

def dijkstra(graph, start_vertex):
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0

    # Ініціалізація бінарної купи з кортежами (відстань, вершина)
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Перевірка чи не потрапили ми в дану вершину з меншою вагою
        if current_distance > distances[current_vertex]:
            continue

        # Обхід всіх сусідів поточної вершини
        for neighbor, weight in graph.vertices[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань менша, оновити відстань та додати вершину в бінарну купу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
g = Graph()

# Додавання вершин та ребер
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

start_vertex = 'A'
shortest_distances = dijkstra(g, start_vertex)

print(f"Shortest distances from vertex {start_vertex}:")
for vertex, distance in shortest_distances.items():
    print(f"To vertex {vertex}: {distance}")
