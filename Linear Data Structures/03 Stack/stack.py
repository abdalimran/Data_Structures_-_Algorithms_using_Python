class Stack:
	def __init__(self):
		'''
		Initializes the stack.
		'''
		self.items = []
	
	def isEmpty(self):
		'''
		Checks if the stack is empty or not.
		Returns True or False.
		'''
		return self.items == []
	
	def push(self, item):
		'''
		Adds an item into the back of the stack.
		'''
		self.items.append(item)
	
	def pop(self):
		'''
		Removes an item from the back of the stack.
		'''
		return self.items.pop()
	
	def top(self):
		'''
		Returns the top most item of the stack.
		'''
		return self.items[len(self.items)-1]
	
	def size(self):
		'''
		Returns size of the stack.
		'''
		return len(self.items)
	
	def printStack(self):
		'''
		Prints the full stack.
		'''
		for item in self.items:
			print(item, end=' ')
		
		
if __name__=='__main__':
	
	'''Example'''
	
	stk = Stack()
	stk.push(0)
	stk.push(1)
	stk.push(2)
	stk.push(3)
	stk.push(4)
	
	print("Stack size: ", stk.size())
	print("Top most item: ", stk.top())
	
	stk.pop()
	stk.push(5)
	
	print("Stack size: ", stk.size())
	print("Top most item: ", stk.top())
	
	stk.printStack()
