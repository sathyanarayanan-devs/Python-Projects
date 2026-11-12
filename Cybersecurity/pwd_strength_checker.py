pwd = input("Enter your password:")

Strength = 0
Has_Upper = False
Has_Lower = False
Has_Digit = False
Has_SChar = False

for char in pwd:
	if(char.isupper() and Has_Upper == False): #This condition helps to check the character is upper or not and ignore repetative upper case characters
		Strength += 2
		Has_Upper = True

	if(char.islower() and Has_Lower == False): #This condition helps to check the character is lower or not and ignore repetative lower case characters
		Strength += 2
		Has_Lower =True

	if(char.isdigit() and Has_Digit == False): #This condition helps to check the character is number or not and ignore repetative numbers
		Strength += 2
		Has_Digit = True

	if(char in "@#$%" and Has_SChar == False): #This condition helps to check the character is special or not and ignore repetative special characters
		Strength += 2
		Has_SChar = True

if(len(pwd) >= 8): #This condition helps to check if the password length is considered to be strong.
	Strength += 2

if(Strength >= 8):
	print("Password Strength: High")
	print("Password Accepted")
elif(Strength >= 5 and Strength < 8):
	print("Password Stength: Medium")
	print("Check if your password is 8 characters and has 1 uppercase, 1 lowercase, 0-9 digits and '@,#,$,%'")
elif(Strength >= 2 and Strength < 5):
	print("Password Strength: Weak")
	print("Password should be atleast 8 characters and have 1 uppercase, 1 lowercase, 0-9 digits and '@,#,$,%'")
else:
	print("Invalid Password!!")
