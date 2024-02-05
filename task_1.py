import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.value < other.value


def build_min_heap(cables):
    heap = [Node(cable) for cable in cables]
    heapq.heapify(heap)
    return heap


def find_minimal_costs(cables):
    heap = build_min_heap(cables)
    total_costs = 0

    while len(heap) > 1:
        smallest1 = heapq.heappop(heap)
        smallest2 = heapq.heappop(heap)

        new_cable = Node(smallest1.value + smallest2.value)
        new_cable.left = smallest1
        new_cable.right = smallest2

        total_costs += new_cable.value
        heapq.heappush(heap, new_cable)

    return total_costs, new_cable


def get_connection_order(root):
    order = []

    def traverse(node):
        if node:
            order.append(node.value)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return order


# Example usage
cables = [4, 2, 7, 1]
result, connection_tree = find_minimal_costs(cables)
connection_order = get_connection_order(connection_tree)

print("Total costs:", result)
print("Connection order:", connection_order)
