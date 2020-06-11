# Deque

# It is an optimised list to perform insertion and deletion easily
# It is similar to list and it has same functionality that of list, difference is its perormance is high
# the real differences between deques and list in terms of performance are: Deques have O(1) speed for appendleft() and
# popleft() while lists have O(n) performance for insert(0, value) and pop(0).
# List append performance is hit and miss because it uses realloc() under the hood.

from collections import deque

deck = deque(['name', 'id', 'age', 'exp'])
print(deck)

deck.append('lang')
deck.appendleft('Surname')
print(deck)

deck.pop()
deck.popleft()
print(deck)
