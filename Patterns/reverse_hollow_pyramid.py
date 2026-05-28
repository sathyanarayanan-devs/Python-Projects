pattern = input("Enter the pattern to display in Reverse Hollow Pyramid:")
n = int(input("Enter number of steps of Reverse Hollow Pyramid:"))

for i in range(n,0,-1):
	for space in range(n-i):
		print(" ",end=" ")

	for j in range(2*i-1):
		if(j == 0 or j == 2*i-2 or i == n):
			print(pattern,end=" ")
		else:
			print(" ",end=" ")
	print()
