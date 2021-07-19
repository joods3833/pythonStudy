#queue

#push(5) - push(2) - push(3) - push(7) - pop - push(1) - push(4) - pop

from collections import deque

queue = deque()

queue.append(5) # 5
queue.append(2) # 2 5
queue.append(3) # 2 5 3
queue.append(7) # 2 5 3 7
queue.popleft() # 5 3 7
queue.append(1) # 5 3 7 1
queue.append(4) # 5 3 7 1 4
queue.popleft() # 3 7 1 4

print(queue) #먼저 들어온 순서대로 출력
queue.reverse()
print(queue)
data = list(queue)
print(data)