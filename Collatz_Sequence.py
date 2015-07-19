import sys

def collatz(num):
	if num % 2 == 0:
		print num // 2
		return num // 2
	elif num % 2 == 1:
		print 3 * num + 1
		return 3 * num + 1

try:
	num = int(input('Enter number: \n'))
except Exception:
	print 'You must enter integer!'	
	sys.exit()
	
while num > 1:
	num = collatz(num)
