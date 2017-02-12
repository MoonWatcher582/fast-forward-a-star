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

def incomplete_tree_test():
	h = MinHeap()
	h.insert(2)
	h.insert(1)
	assert h.heap_data[0] == 1
	assert h.heap_data[1] == 2
	assert_size(h, 2)

	elems = []
	elems.append(h.extract())
	elems.append(h.extract())
	assert elems == [1, 2]
	assert_size(h, 0)

def several_elements_test():
	h = MinHeap()
	h.insert(5)
	h.insert(3)
	h.insert(4)
	h.insert(122)
	h.insert(100)
	h.insert(2)
	h.insert(8)
	h.insert(18)
	assert_size(h, 8)

	elems = []
	for i in range(8):
		elems.append(h.extract())
	assert elems == [2, 3, 4, 5, 8, 18, 100, 122]
	assert_size(h, 0)

def assert_size(heap, size):
	assert heap.size == size
	assert len(heap.heap_data) == heap.size

def main():
	print "Testing heap initialization"
	init_test()

	print "Testing inserting and extracting one item"
	single_item_test()

	print "Testing inserting and extracting from an incomplete tree"
	incomplete_tree_test()

	print "Testing inserting and extracting several items"
	several_elements_test()

if __name__ == "__main__":
	print "Launching test suite"
	main()
