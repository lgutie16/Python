class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

node1 = Node("node1", None)
node2 = Node("node2", node1)
node3 = Node("node3", node2)
node4 = Node("node4", node3)
node5 = Node("node5", node4)
node6 = Node("node6", node5)
node7 = Node("node7", node6)
node8 = Node("node8", node7)
node9 = Node("node9", node8)

head = node9

fastP = head
slowP = head

while fastP.next != None and fastP.next.next != None:
	fastP = fastP.next.next
	slowP = slowP.next

print slowP.data

		