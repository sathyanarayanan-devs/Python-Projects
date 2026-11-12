pattern = input("Enter the pattern to display in reverse RTriangle:")
n = int(input("Enter number of steps of the Reverse Right Triangle:"))

for i in range(n,0,-1):
	for j in range (i):
		print(pattern,end=" ")
	print()
