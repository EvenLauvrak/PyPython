def fibo(n):
	if n == 1 or n == 2:
		return 1
	return fibo(n-1) + fibo(n-2)

for i in range(1,21):
	print fibo(i)