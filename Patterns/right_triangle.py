pattern = input("Enter the pattern to display in right triangle:")
n = int(input("Enter number of steps of the right triangle:"))

for i in range(1,n+1):
	for j in range(i):
		print(pattern,end=" ")
	print()
