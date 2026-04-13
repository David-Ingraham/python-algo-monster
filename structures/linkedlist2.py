class Node:

	def __init__(self, val, next=None):
		self.val = val
		self.next = None

	
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next= c


curr = a
def traverse(curr):

	while curr:
		print(curr.val)
		curr = curr.next

curr = a


traverse(curr)





