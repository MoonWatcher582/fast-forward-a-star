from heap import MinHeap

def init_test():
	h = MinHeap()
	assert h.heap_data is not None
	assert_size(h, 0)

def single_item_test():
	h = MinHeap()
	h.insert(1)
	assert h.heap_data[0] == 1
	assert_size(h, 1)

	elem = h.extract()
	assert elem == 1
	assert_size(h, 0)

def assert_size(heap, size):
	assert heap.size == size
	assert len(heap.heap_data) == heap.size

def main():
	print "Testing heap initialization"
	init_test()

	print "Testing inserting and extracting one item"
	single_item_test()

if __name__ == "__main__":
	print "Launching test suite"
	main()
