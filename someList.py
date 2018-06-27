import heapq
from collections import Counter


MyList = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(MyList)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print("Liste de nums:", nums)
'''
for i in nums:
    print(i)

print("Liste de nums:", nums)
'''

MyHeap = list(nums)
heapq.heapify(MyHeap)

print("Myheap première fois:", MyHeap)

print("pop:", heapq.heappop(MyHeap))
print("Myheap deuxième fois:", MyHeap)
print("pop:", heapq.heappop(MyHeap))
print("Myheap 3ième fois:", MyHeap)

print("Les 3 plus petits restant:", heapq.nsmallest(3, nums))  # Print 3 smallest number from nums

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print("Les trois plus fréquents:", top_three)

print("Mots et fréquence:", word_counts)

