import math

class MinHeap(object):
	def __init__(self):
		self.heap_data = []
		self.size = 0

	def insert(self, data):
		self.heap_data.append(data)
		self.size += 1
		self.sift_up(self.size - 1)

	def extract(self):
		if self.size == 0:
			return None
		last_elem = self.heap_data.pop()
		if self.heap_data:
			temp = self.heap_data[0]
			heap[0] = last_elem
			self.size -= 1
			self.sift_down(0)
		else:
			temp = last_elem
			self.size -= 1
		return temp

	def sift_up(self, index):
		while index != 0:
			p = self.parent(index)
			if self.heap_data[index] < self.heap_data[p]:
				self.swap(index, p)
				index = p
			else:
				break

	def sift_down(self, index):
		r_index = self.right_child(index)
		r_child = self.safe_get_value(r_index)

		l_index = self.left_child(index)
		l_child = self.safe_get_value(l_index)

		smaller = None
		if r_child and l_child:
			smaller = r_index if r_child < l_child else l_index
		elif r_child: 
			smaller = r_index
		elif l_child: 
			smaller = l_index
		else:
			return

		self.swap(index, smaller)
		self.sift_down(smaller)

	def safe_get_value(self, index):
		if index < self.size:
			return self.heap_data[index]
		return None

	def heapsort(self):
		for i in self.size:
			self.sift_up(i)
		for i in self.size:
			self.sift_down(self.size - i -1)	

	def swap(self, ind1, ind2):
		self.heap_data[ind1], self.heap_data[ind2] = self.heap_data[ind2], self.heap_data[ind1]

	def parent(self, index):
		return int(math.floor((index - 1) / 2))

	def left_child(self, index):
		return int((index * 2) + 1)

	def right_child(self, index):
		return int((index * 2) + 2)
