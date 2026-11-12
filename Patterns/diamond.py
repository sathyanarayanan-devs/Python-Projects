pattern = input("Enter the pattern to display in a diamond pattern:")
n = int(input("Enter number of steps of the diamond:"))

for i in range(1,n+1):
	for space in range(n-i):
		print(" ",end=" ")

	for j in range(2*i-1):
		print(pattern,end=" ")

	print()

for i in range(n-1,0,-1):
	for space in range(n-i):
		print(" ",end=" ")

	for j in range(2*i-1):
		print(pattern,end=" ")

	print()
