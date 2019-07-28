# Part 2 of the Python Review lab.

def encode(x, y):
	while not prime(x):#same as 'while prime(x)==False' 
		x+=1
	while not prime(y):
		y+=1
	if 1<y<250 and 500<x<1000:
		return x*y
	else:
		return ("invalid input: outside range")

def prime(n):
	if n>1:
		for i in range(2,n):
			if n%i ==0:
				return False
	return True

def decode(coded_message):
	for y in range(2,250):
		if not prime(y):
			continue 
	if coded_message % y ==0 
		x=coded_message // y
		if (prime(x), 500<x<1000):#(always true)
			return (x,y)


