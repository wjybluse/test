def factorial(n):
	r= _factorial(n, 1)
	print(r)

def _factorial(n,result):
	if n<=1:
		return result
	return _factorial(n-1, result*n)


def fib(num):
	print(_fib(num, 0, 1))

def _fib(num,a,b):
	if num<=1:
		return b
	return _fib(num-1, b, a+b)

if __name__ == '__main__':
	#factorial(500)
	fib(4)
