def coruntine():
	for i in range(100):
		yield i
		print('hello world')
		yield 
		print("hello world xx "+str(i))

def test():
	gen = coruntine()
	i = gen.next()
	gen.next()
	gen.next()
	gen.next()
	gen.next()
	print(str(i))



if __name__ == '__main__':
	test()
