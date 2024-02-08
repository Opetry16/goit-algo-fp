import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap_array):
    heapq.heapify(heap_array)
    heap_root = HeapNode(heap_array[0])
    nodes_stack = [(heap_root, 0)]
    while nodes_stack:
        parent, parent_index = nodes_stack.pop(0)
        left_child_index = 2 * parent_index + 1
        if left_child_index < len(heap_array):
            left_child = HeapNode(heap_array[left_child_index])
            parent.left = left_child
            nodes_stack.append((left_child, left_child_index))
        right_child_index = 2 * parent_index + 2
        if right_child_index < len(heap_array):
            right_child = HeapNode(heap_array[right_child_index])
            parent.right = right_child
            nodes_stack.append((right_child, right_child_index))
    return heap_root

def visualize_heap(heap_array):
    # Побудова дерева з купи
    heap_root = build_heap_tree(heap_array)
    
    # Візуалізація дерева купи
    draw_heap(heap_root)

# Приклад використання:
heap_array = [1, 5, 8, 4, 3, 2, 1, 28, 3, 2, 1]
heapq.heapify(heap_array)
visualize_heap(heap_array)
