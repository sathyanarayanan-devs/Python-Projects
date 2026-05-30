import random

def generate_pwd(length):
	chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pwd = ""

	num_choice =input("Do you want to include numbers in your password:")
	sc_choice =input("Do you want to include symbols in your password:")

	if(num_choice.lower() == "yes"):
		chars+="0123456789"

	if(sc_choice.lower() == "yes"):
		chars+="@#$%"

	for i in range(length):
		pwd+=random.choice(chars)

	return pwd

length = int(input("Enter the length of your password:"))
print("Generated Password:",generate_pwd(length))
