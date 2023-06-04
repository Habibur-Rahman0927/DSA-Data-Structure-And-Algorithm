class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def get_minimum(self):
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def delete_minimum(self):
        if not self.heap:
            return None

        # Swap the root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        # Remove the last element
        minimum = self.heap.pop()

        # Heapify down
        self.heapify_down(0)

        return minimum

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify_down(self, i):
        while self.left_child(i) < len(self.heap):
            min_child = self.left_child(i)
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] < self.heap[min_child]:
                min_child = self.right_child(i)

            if self.heap[i] <= self.heap[min_child]:
                break

            self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child


heap = BinaryHeap()
heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)
print(heap.get_minimum())  # 1
print(heap.delete_minimum())  # 1
print(heap.get_minimum())  # 3