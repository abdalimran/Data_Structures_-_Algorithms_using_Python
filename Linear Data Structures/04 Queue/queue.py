class Queue:
	def __init__(self):
		'''
		Initializes the queue.
		'''
		self.items = []

	def isEmpty(self):
		'''
		Checks if the queue is empty or not.
		Returns True or False.
		'''
		return self.items == []

	def enqueue(self,item):
		'''
		Adds an item into the queue.
		'''
		self.items.insert(0,item)
		
	def dequeue(self):
		'''
		Removes an item from the queue.
		'''
		self.items.pop()
		
	def size(self):
		'''
		Returns size of the queue.
		'''
		return len(self.items)
		
	def top(self):
		'''
		Returns the top most item of the queue.
		'''
		return self.items[len(self.items)-1]
	
	def printQueue(self):
		'''
		Prints the full queue.
		'''
		for item in self.items:
			print(item,end=" ")
			
if __name__=='__main__':
	
	'''Example'''
	
	que = Queue()
	que.enqueue(0)
	que.enqueue(1)
	que.enqueue(2)
	que.enqueue(3)
	que.enqueue(4)
	
	print("Queue size: ", que.size())
	print("Top most item: ", que.top())
	
	que.dequeue()
	que.enqueue(5)
	
	print("Queue size: ", que.size())
	print("Top most item: ", que.top())
	
	que.printQueue()
