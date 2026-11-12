num = int(input("Enter the number to fetch the multiplication table:"))
n = int(input("Enter number of terms of the multiplication table:"))
for i in range(1,n+1):
	mul = num*i
	print(num,"x",i,"=",mul)
