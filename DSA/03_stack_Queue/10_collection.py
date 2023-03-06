# queue

from collections import deque

deque = deque(maxlen=3)

print(deque)

deque.append(1)
deque.append(2)
deque.append(3)
deque.append(4)

print(deque.popleft())

print(deque)


# stack
import queue as q


queue = q.Queue(maxsize=3)

print(queue.empty())
print(queue.qsize())
print(queue.full())
print(queue.put(1))
print(queue.get())

# multiprocessing queue as a FIFO

from multiprocessing import Queue

customQueue = Queue(maxsize=3)

customQueue.put(1)

print(customQueue.get())