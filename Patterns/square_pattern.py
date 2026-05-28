pattern = input("Enter the pattern to display in a square format:")
n = int(input("Enter number of rows of the square:"))

for i in range(1,n+1):
	for j in range(n):
		print(pattern,end=" ")
	print()
