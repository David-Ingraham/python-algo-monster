class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
a = Node(0)
b = Node(1)
c= Node(2)
d = Node(3)
a.next=b
b.next = c
c.next =d
def traverse(head):
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next
head = a # resetting vars, after traverse head would be None
def reverse(head):
	prev = None
	curr = head
	while curr:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	return prev



traverse(a)
head = a

reverse(a)
head = d
traverse(head)
		



