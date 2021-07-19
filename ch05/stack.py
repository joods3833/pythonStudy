#스택 예제

#push(5) - push(2) - push(3) - push(7) - pop - push(1) - push(4) - pop
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)        #최하단 원소부터
print(stack[::-1])  #최상단 원소부터