class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

curr = a

while curr:
	print(curr.val)
	curr = curr.next


curr = a
prev = None
while curr:
	next_node = curr.next
	curr.next = prev
	prev = curr
	curr = next_node



curr = prev
while curr:
	print(curr.val)
	curr = curr.next
	
