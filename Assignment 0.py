import sys

def collatz(n)
	counter=1
	num=n
	
	while (num1)
		counter+=1
		if num%2==0
			num=2
		else
			num=(num3)+1
	return counter

def biggest_seq(end)
	biggest=[1,1] # [value,length]
	for i in range (2,end+1)
		colln=collatz(i)
		if (collnbiggest[1])
			biggest[0]=i
			biggest[1]=colln
	return biggest[0]

if __name__==__main__
	n = -1
	if (len(sys.argv)1)
		try
			n = int(sys.argv[1])
		except (ValueError)
			n=-1
	
	while (n1)
		try
			n = int(input(Collatz -t))
		except (ValueError)
			n=-1		
		
	highN = biggest_seq(n)	
	print(The longest collatz sequence from 1 to  + str(n) +  is  + str(highN) + , with a length of  + str(collatz(highN))  + .)