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
    connection_order = []

    while len(heap) > 1:
        smallest1 = heapq.heappop(heap)
        smallest2 = heapq.heappop(heap)

        new_cable = Node(smallest1.value + smallest2.value)
        new_cable.left = smallest1
        new_cable.right = smallest2

        total_costs += new_cable.value
        connection_order.append((smallest1.value, smallest2.value, new_cable.value))
        heapq.heappush(heap, new_cable)

    return total_costs, connection_order


# Example usage
cables = [4, 2, 7, 3, 14, 1]
result, connection_order = find_minimal_costs(cables)

print("Total costs:", result)
print("Connection order:")
for connection in connection_order:
    print(f"Connect {connection[0]} and {connection[1]} to get {connection[2]}")
