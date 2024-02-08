import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_binary_tree(tree_array):
    if not tree_array:
        return None
    
    root = HeapNode(tree_array[0])
    queue = [(root, 0)]

    while queue:
        node, index = queue.pop(0)
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(tree_array) and tree_array[left_index] is not None:
            node.left = HeapNode(tree_array[left_index])
            queue.append((node.left, left_index))
        if right_index < len(tree_array) and tree_array[right_index] is not None:
            node.right = HeapNode(tree_array[right_index])
            queue.append((node.right, right_index))
    
    return root

def visualize_tree_traversal(root, traversal_type):
    iter_count = 0

    def dfs(node, colors):
        nonlocal iter_count
        if node is None:
            return
        colors[node.id] = generate_color(iter_count)
        iter_count += 1
        dfs(node.left, colors)
        dfs(node.right, colors)

    def bfs(node, colors):
        nonlocal iter_count
        queue = [(node, 0)]
        while queue:
            current_node, _ = queue.pop(0)
            colors[current_node.id] = generate_color(iter_count)
            iter_count += 1
            if current_node.left:
                queue.append((current_node.left, 0))
            if current_node.right:
                queue.append((current_node.right, 0))

    def generate_color(iteration):
        # Змінюємо компоненти кольору (R, G, B) з кожним кроком обходу
        red = (iteration * 5) % 256  # червоний
        green = (iteration * 10) % 256  # зелений
        blue = (iteration * 20) % 256  # синій
        rgba = (red / 255, green / 255, blue / 255, 1.0)  # перетворюємо на кортеж
        return rgba

    colors = {}
    if traversal_type == 'depth':
        dfs(root, colors)
    elif traversal_type == 'breadth':
        bfs(root, colors)
    else:
        raise ValueError("Invalid traversal type")

    pos = {}
    graph = nx.DiGraph()
    graph = add_heap_edges(graph, root, pos)
    node_colors = [colors[node_id] for node_id in graph.nodes]
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

# Приклад використання:
tree_array = [1, 2, 3, 4, 5, 6, 7]  # Приклад дерева
root = build_binary_tree(tree_array)
visualize_tree_traversal(root, 'depth')  # Обхід у глибину
visualize_tree_traversal(root, 'breadth')  # Обхід у ширину


