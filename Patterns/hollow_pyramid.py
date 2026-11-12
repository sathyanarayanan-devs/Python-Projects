pattern = input("Enter the pattern to display as a hollow pyramid:")
n = int(input("Enter number of steps of the hollow pyramid:"))

for i in range(1,n+1):
	for spaces in range(n-i):
		print(" ",end=" ")

	for j in range(2*i-1):
		if(j == 0 or j == 2*i-2 or i == n):
			print(pattern,end=" ")
		else:
			print(" ",end=" ")
	print()
