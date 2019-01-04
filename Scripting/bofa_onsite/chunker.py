
def chunker(iterable, chunk_size):
	start = 0
	end = chunk_size
	for elements in range(len(iterable)//chunk_size + len(iterable)%chunk_size):
		yield iterable[start:end]
		start = end
		end += chunk_size

for i in chunker(range(25),4):
	print(list(i))


