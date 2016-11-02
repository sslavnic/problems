
N = int(input("Enter N value: "))

sum = 0

for x in range(1, N-2 + 1):
	for y in range(x + 1, N-1 + 1):
		for z in range(y + 1, N + 1):
			sum = sum + 1

print sum
