import heapq
from collections import namedtuple
# ------------------------------
string = input()
# ------------------------------
class Node(namedtuple('Node', ['left', 'right'])):
	def walk(self, code, acc):
		self.left.walk(code, acc + '0')
		self.right.walk(code, acc + '1')
		
class Leaf(namedtuple('Leaf', ['char'])):
	def walk(self, code, acc):
		code[self.char] = acc if acc else '0'
		
freq = {}
heap = []
count = len(heap)
# ------------------------------
# определяем частоты символов
for c in string:
	if c in freq:
		freq[c] += 1
	else: 
		freq[c] = 1
# ------------------------------
for c in freq:
	heapq.heappush(heap, (freq[c], count, Leaf(c)))
	count += 1
# ------------------------------
while len(heap) > 1:
	f1, cnt1, left = heapq.heappop(heap)
	f2, cnt2, right = heapq.heappop(heap)
	heapq.heappush(heap, (f1 + f2, count, Node(left, right) ))
	count += 1
# ------------------------------
code = {}
if len(heap):
	[(f, cnt, root)] = heap
	root.walk(code, '')

# вывод результата
res = ''
for c in string:
	res += code[c]
print(len(list(code.keys())), end=' ')
print(len(res))
for c in code:
	print(c + ': ' + code[c])
print(res)
# ------------------------------
