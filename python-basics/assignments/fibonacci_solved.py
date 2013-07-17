#!/usr/bin/env python

def sum_fibonacci(n):
	'''gives the sum of the first n numbers in the fibonacci sequence'''
	fib_array=[0,1,1] # have to start somewhere...
	sum = 2
	for i in range(3,n+1):
		seq = fib_array[i-1]+fib_array[i-2]
		fib_array.append(seq)
		print fib_array
		sum+=seq
	print fib_array
	return sum

# NOTE: this is an encoded solution
#       the programme will decode it automatically
#         so you can check your results against it yourself
#       it will create a function called `solution'
solution = None
exec '''sebz vgregbbyf vzcbeg vfyvpr
qrs svobanppv(n=1, o=1):
	juvyr Gehr:
		lvryq n
		n, o = o, n+o
fbyhgvba = ynzoqn a: fhz(vfyvpr(svobanppv(),0,a))
'''.decode('rot13') in locals(), globals()

if __name__ == '__main__':
	# NOTE: some simple tests
	assert sum_fibonacci(10)   == solution(10)   == 143
	assert sum_fibonacci(100)  == solution(100)  == 927372692193078999175L  

	# just check the last digit
	#assert str(sum_fibonacci(1000))[-1] == str(solution(1000))[-1] == '5'
	
	print 'All the tests passed! Great job!'
