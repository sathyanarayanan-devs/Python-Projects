pattern = input("Enter the pattern to display in butterfly format:")
n = int(input("Enter the number of steps of butterfly format:"))

for i in range(1,n+1):
	for j in range(i):
		print(pattern,end=" ")

	for s in range(2*(n-i)):
		print(" ",end=" ")

	for k in range(i):
		print(pattern,end=" ")
	print()

for i in range(n-1,0,-1):
	for j in range(i):
		print(pattern,end=" ")

	for s in range(2*(n-i)):
		print(" ",end=" ")

	for k in range(i):
		print(pattern,end=" ")
	print()
