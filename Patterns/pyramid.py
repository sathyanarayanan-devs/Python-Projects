pattern = input("Enter the pattern of the pyramid to display:")
n = int(input("Enter number of steps of the pyramid:"))

for i in range(1,n+1):
	for spaces in range(n-i):
		print(" ",end=" ")

	for j in range(2*i-1):
		print(pattern,end=" ")
	print()
