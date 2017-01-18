from collections import defaultdict

N = int(input("Maximum Pay: "))
M = int(input("Number of employees: "))


"""
	Approach the problem as if it was a lattice path problem on:

	--------------------------------------------------------  N
	|														|
	|														|
	|														|
	|														|  
	|														|   pay
	|														|
	|														| 
	|														|
	|														|
	|														| 1
	--------------------------------------------------------  
	1						rank							M


	Notice that an invalid ordering in this model is any 3 successively decreasing
	(left to right) or increasing (right to left) points. 

	The number of valid paths at (m,n) will depend on the current pay n's relation
	to two things:

		1) The lowest pay thus far

	If n > lowest pay thus far then paying any more would be an invalid ordering
	so we're restricted to paying <= n in this case.

		2) The highest pay thus far

	If n < lowest pay thus far we can pay more for a lower rank, but must take
	care not to pay greater than our previous max to avoid invalid orderings.
"""

#Function factory for default dictionary value
def neg_factory_func():
	return -1

Ddict = defaultdict(neg_factory_func)

#The recursion
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



#Sum over all starting points
sum = 0
for k in range(1, N + 1):
	sum += DR(M, k, k, N)

print(sum)

# This program runs in something like O(n^5) (what with n=m) which for the input in the problem-statement
# 	makes it a bad idea to use base python. A better implementation could be done in something faster
# 	like C, Cython or mabye with Numpy. This solution checks out for reasonably high values of n and m
#	and I've lost motivation now that I'm pretty sure it's solved.
