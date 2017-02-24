class Node:
	'''
	This is the node for constructing linked list.
	'''
	def __init__(self,initdata):
		self.data = initdata
		self.next = None
		
	def getData(self):
		return self.data
	
	def getNext(self):
		return self.next
		
	def setData(self,newdata):
		self.data = newdata
		
	def setNext(self,newnext):
		self.next = newnext


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		
	def isEmpty(self):
		'''
		Checks if the list is empty or not.
		'''
		return self.head == None
		
	def add(self,item):
		'''
		Add a new item in the list.
		'''
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		
	def size(self):
		'''
		Returns the size of the list.
		'''
		current = self.head
		count = 0
		
		while current != None:
			count += 1
			current = current.getNext()
		return count
		
	def search(self,item):
		'''
		Search for a particular item into the list.
		'''
		current = self.head
		found = False
		
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
		
	
	def remove(self,item):
		'''
		Removes a particular item from the list.
		'''
		current = self.head
		previous = None
		found = False
		
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
				
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
			
	def print_list(self):
		'''
		Prints the full list.
		'''
		current = self.head
		while current != None:
			print(current.getData())
			current = current.getNext()
	
	
if __name__=="__main__":
	lnkdlist = SinglyLinkedList()
	
	lnkdlist.add(5)
	lnkdlist.add(6)
	lnkdlist.add(7)
	lnkdlist.remove(6)
	lnkdlist.print_list()
