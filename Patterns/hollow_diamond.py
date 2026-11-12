pattern = input("Enter the pattern to display in hollow diamond format:")
n = int(input("Enter the number of steps of hollow diamond:"))

for i in range(1,n+1):
	for space in range(n-i):
		print(" ",end=" ")

	for j in range(2*i-1):
		if(j == 0 or j == 2*i-2):
			print(pattern,end=" ")
		else:
			print(" ",end=" ")
	print()

for i in range(n-1,0,-1):
	for space in range(n-i):
		print(" ",end=" ")

	for j in range(2*i-1):
		if(j == 0 or j == 2*i-2):
			print(pattern,end=" ")
		else:
			print(" ",end=" ")
	print()

