# CSC 506_ CT4

import time
from collections import deque

# Stack comparison
list_stack = []
deque_stack = deque()

# Push elements
start = time.time()
for i in range(1000000):
    list_stack.append(i)
end = time.time()
print(f"List-based stack push: {end - start} seconds")

start = time.time()
for i in range(1000000):
    deque_stack.append(i)
end = time.time()
print(f"Deque-based stack push: {end - start} seconds")

# Pop elements
start = time.time()
while list_stack:
    list_stack.pop()
end = time.time()
print(f"List-based stack pop: {end - start} seconds")

start = time.time()
while deque_stack:
    deque_stack.pop()
end = time.time()
print(f"Deque-based stack pop: {end - start} seconds")

# Queue comparison
list_queue = []
deque_queue = deque()

# Enqueue elements
start = time.time()
for i in range(1000000):
    list_queue.append(i)
end = time.time()
print(f"List-based queue enqueue: {end - start} seconds")

start = time.time()
for i in range(1000000):
    deque_queue.append(i)
end = time.time()
print(f"Deque-based queue enqueue: {end - start} seconds")

# Dequeue elements
start = time.time()
while list_queue:
    list_queue.pop(0)
end = time.time()
print(f"List-based queue dequeue: {end - start} seconds")

start = time.time()
while deque_queue:
    deque_queue.popleft()
end = time.time()
print(f"Deque-based queue dequeue: {end - start} seconds")