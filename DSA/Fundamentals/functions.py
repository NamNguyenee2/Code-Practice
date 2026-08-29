## -- Collections --

from collections import deque, defaultdict, Counter

# q = deque()
# q.append(x)
# q.popleft()
# q.pop() 
# q.appendleft(x)

# d = defaultdict(list)
# d = defaultdict(int)

# c = Counter(nums)
# c.most_common

'''
q = deque()
print("q: ", q)

q.append('a')
q.append('b')
q.append('c')
q.append(1)         # We can append any type of object to the deque
print("new q:", q)

q.popleft()
print("pop left q:", q)

q.pop()             # pop the rightmost element
print("pop q:", q)

q.appendleft('z')   # put q to the leftmost position
print("append left q:", q) 
'''

'''
d = defaultdict(list)
print("d:", d)

d = defaultdict(int)
print("d int:", d)

nums = [10, 20, 30, 10, 20, 10, 100, 200, 300, 100, 200, 100]
c = Counter(nums) # what is time complexity of this operation? O(n)
print("c:", c)

print('most common in c:', c.most_common(1)) # time complexity O(n log n) for sorting, but O(n) for finding the most common elements using a heap.
'''

## -- Heaps --
# Tree-based data structure that satisfies the heap property.

import heapq #min-heap

# heapq.heappush(h, x)
# heapq.heappop(h)
# heapq.heapify(arr)
# heapq.nlargest(k, nums)
# heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)

'''
my_heap = [10, 1]
print("my_heap:", my_heap)
heapq.heappush(my_heap, 2)
heapq.heappush(my_heap, 10)
heapq.heappush(my_heap, 4)                          # push x onto heap h at the rightmost position
print("my_heap after heappush:", my_heap)           # must use the same type of elements in the heap, otherwise it will raise a TypeError

# c = Counter(my_heap)
# print("common of my_heap", c.most_common(1))

# heapq.heappop(my_heap)
# print("my_heap after heappop:", my_heap)          # pop the smallest item off the heap, maintaining the heap invariant but 1 is the smallest, why it removed 3?
# heapq.heappop(my_heap)
# print("second heappop:", my_heap)                 # pop the smallest item off the heap, maintaining the heap invariant but 1 is the smallest, why it removed 3?

heapq.heapify(my_heap)                              # arrange a list to get the min-heap structure (the smallest value at index 0)
print("after heapify", my_heap) 

print("n largest", heapq.nlargest(3, my_heap))      # k largest values from the my_heap

products = [
    {'name': 'laptop',   'price': 1200},
    {'name': 'mouse',    'price': 25},
    {'name': 'monitor',  'price': 300},
    {'name': 'keyboard', 'price': 75}
]

expensive_items = heapq.nlargest(1, products, key=lambda x: x['price'])
cheap_items     = heapq.nsmallest(1, products, key=lambda x: x['price'])
print('expensive items:', expensive_items)
print('cheap items:', cheap_items)

min_heap = heapq.nsmallest(1, my_heap)
print('min of my_heap', min_heap)
'''

## -- Binary search --

import bisect

# bisect.bisect_left(arr, x)          # leftmost insertion point
# bisect.bisect_right(arr, x)         # rightmost insertion point
# bisect.insort_left(arr, x)          # find the left insertion point
# bisect.insort_left(arr, x)          # find the right insertion point 
# bisect.insort(arr, x)
arr = [1, 2, 4, 4, 4, 6, 8]

idx_left  = bisect.bisect_left(arr, 4)
print('arr:', arr)
print('bisect left:', idx_left)

idx_right = bisect.bisect_right(arr, 4)
print('arr', arr)
print('bisect right:', idx_right)

bisect.insort(arr, 3)
print('arr:', arr)

