from collections import defaultdict

N = int(input("Maximum Pay: "))
M = int(input("Number of employees: "))

def t():
	return -1

Ddict = defaultdict(t)
	

def DR(m, n, roll_min, roll_max):
	if m == 1:
		return 1
	if Ddict[m, n, roll_min, roll_max] != -1:
		return Ddict[m, n, roll_min, roll_max]
		
	sum = 0

	#Above min, so only allowed to go down
	if(n > roll_min):
		for i in range(1, n + 1):

			if(i <= roll_min):
				sum += DR(m - 1, i, i, roll_max)
			else:
				sum += DR(m - 1, i, roll_min, roll_max)

	#Below or at min, so can go up as well
	else:

		#Everything below is below the min as well
		for i in range(1, n + 1):
			sum += DR(m - 1, i, i, roll_max)

		#Make sure not to go over max
		for i in range(n + 1, roll_max + 1):
			sum += DR(m - 1, i, roll_min, i)


	Ddict[m, n, roll_min, roll_max] = sum
	return sum

sum = 0
for k in range(1, N + 1):
	sum += DR(M, k, k, N)

#sum = DR(M, N, N)
print(sum)


