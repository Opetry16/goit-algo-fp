class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def sorted_insert(self, head, new_node):
        if head is None or head.data >= new_node.data:
            new_node.next = head
            return new_node

        current = head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return head

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self is not None and current_other is not None:
            if current_self.data < current_other.data:
                merged_list.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged_list.insert_at_end(current_other.data)
                current_other = current_other.next

        while current_self is not None:
            merged_list.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged_list.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged_list

# Приклад використання
llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

print("Вихідний список:")
llist.print_list()

llist.reverse_list()
print("\nРеверсований список:")
llist.print_list()

llist.insertion_sort()
print("\nВідсортований список:")
llist.print_list()

llist2 = LinkedList()
llist2.insert_at_end(8)
llist2.insert_at_end(12)
llist2.insert_at_end(18)

merged_list = llist.merge_sorted_lists(llist2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()
