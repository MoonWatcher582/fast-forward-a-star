import math

class MinHeap(object):
	def __init__(self):
		self.heap_data = []
		self.size = 0

	def insert(self, data):
		self.heap_data.append(data)
		self.size += 1
		self.sift_up(len(self.heap_data) - 1)

	def extract(self):
		temp = self.heap_data[0]
		self.heap_data[0] = self.heap_data[len(self.heap_data) - 1]
		del(self.heap_data[-1])
		self.size -= 1
		self.sift_down(0)
		return temp

	def sift_up(self, index):
		while index != 0:
			p = self.parent(index)
			p = int(p)
			if self.heap_data[index] < self.heap_data[p]:
				self.swap(index, p)
				index = p
			else:
				break

	def sift_down(self, index):
		r_index = self.right_child(index)
		l_index = self.left_child(index)
		# if the root is less than both of its children, it is in the correct position; break
		if r_index < self.size:
			if self.heap_data[index] < self.heap_data[r_index]: 
				if l_index < self.size:
					if self.heap_data[index] < self.heap_data[l_index]:
						return
				else:
					return
			else:
				return
		else:
			if r_index < self.size and l_index < self.size:
				if self.heap_data[r_index] < self.heap_data[l_index]:
					smaller = r_index
				else:
					smaller = l_index
			elif r_index < self.size and l_index >= self.size:
				smaller = r_index
			elif r_index >= self.size and l_index < self.size:
				smaller = l_index
			else:
				return
			self.swap(index, smaller)
		self.sift_down(smaller)

	def heapsort(self):
		for i in self.size:
			self.sift_up(i)
		for i in self.size:
			self.sift_down(self.size - i -1)	

	def swap(self, ind1, ind2):
		temp = self.heap_data[ind1]
		self.heap_data[ind1] = self.heap_data[ind2]
		self.heap_data[ind2] = temp

	def parent(self, index):
		return math.floor((index - 1) / 2)

	def left_child(self, index):
		return ((index * 2) + 1)

	def right_child(self, index):
		return ((index * 2) + 2)
