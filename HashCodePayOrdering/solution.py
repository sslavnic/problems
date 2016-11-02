from collections import defaultdict

N = int(input("Maximum Pay: "))
M = int(input("Number of employees: "))

def t():
	return -1

Ddict = defaultdict(t)
	
	#	Going up, right, or down once
def DR(m, n, rolling_max):
	if m == 1:
		return 1
	if Ddict[m, n, rolling_max] != -1:
		return Ddict[m, n, rolling_max]
		
		
	# Number of ways to get to n, when at (m -1 , <= n) 
	sum = 0
	for k in range(1, n + 1):
		sum += DR(m - 1, k, rolling_max)
	
	# Number of ways to get to n, from above n
	for k in range(n + 1, rolling_max + 1):
		sum += DR(m - 1, k, k)
	
	Ddict[m, n, rolling_max] = sum
	return sum
	
	
sum = 0
for k in range(1, N + 1):
	sum += DR(M, k, N)

#sum = DR(M, N, N)
print(sum)


