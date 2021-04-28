import heapq
from collections import defaultdict


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


data = 'Huffman coding algorithm works by creating a binary tree of nodes'
frequency = defaultdict(int)
for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)
x = 0
s = 0
for p in huff:
    x += 1
    s += len(p[1])
    print('"' + p[0].ljust(1)+ '"' + " = " + p[1])
y = s/x
print("freq = "+ str(y))