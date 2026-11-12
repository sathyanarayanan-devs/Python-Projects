#global variable to store the student data
students = []

#function to display the menu
def show_menu():
	print("===== Student Management System =====")
	print("1. Add Student \n2. View Students \n3. Search Student \n4. Update Marks \n5. Delete Student")
	print("6. Calculate Average \n7. Find Topper \n8. Assign Grades \n9. Sort Students by Marks \n10. Exit")
	print("=====================================")

#function to get input which is not a empty space
def get_valid_input(message):
	while True:
		value = input(message).strip()

		if value:
			return value
		print("Input cannot be empty")

#function to get valid marks
def get_valid_marks():
	while True:
		try:
			marks = float(input("Enter marks (0 - 100):"))

			if 0 <= marks <= 100:
				return marks
			print("Marks must be from 0 to 100.")
		except ValueError:
			print("Invalid Marks.")

#function to find student by using their reg_no
def find_student_by_reg_no(reg_no):
	for student in students:
		if student["Reg_No"].lower() == reg_no.lower():
			return student
	return None

#function to add students into the list
def add_students():

	print("-"*4, "Add Student Record", "-"*4)

	name = get_valid_input("Enter student Name: ")
	reg_no = get_valid_input("Enter student register number: ")

	if find_student_by_reg_no(reg_no):
		print("Student Already exists.")
		return
	
	marks = get_valid_marks()

	student = {
		"Name" : name,
		"Reg_No" : reg_no,
		"Marks" : marks
	}

	students.append(student)
	print("Student added Successfully.")

#function to display student details
def display_students():

	print("-"*4,"Student Records","-"*4)

	if not students:
		print("No Student Data Exists..")
		return
	
	print("-"*45)
	print(f"{'Name':<20} {'Reg_No':<15} {'Marks':<10}")
	print("-"*45)
	
	for student in students:
		print(
			f"{student['Name']:<20} "
			f"{student['Reg_No']:<15} "
			f"{student['Marks']:<10.2f}"
		)
	print("-"*45)

#function to search for a specific student
def search_student():
	print("-"*4, "Search Student", "-"*4)

	reg_no = get_valid_input("Enter the registration number to search: ")

	student = find_student_by_reg_no(reg_no)

	if student:
		print("Student Found!")
		print("Name: ", student["Name"])
		print("Register Number: ", student["Reg_No"])
		print("Marks: ", student["Marks"])
	else:
		print("No student data exists")

#function to update the marks of a specific student marks
def update_marks():

	print("-"*4, "Update Marks", "-"*4)

	reg_no = get_valid_input("Enter the register number of the student: ")

	student = find_student_by_reg_no(reg_no)

	if student:
		print("Name: ", student["Name"])
		print("Current Mark: ", student["Marks"])

		new_mark = get_valid_marks()

		student["Marks"] = new_mark

		print("New Mark: ", student["Marks"])

		print("Student Mark Updated successfully")
	else:
		print("Student record not found")

#function to delete a student record completely
def delete_student():

	print("---- Delete Student ----")

	reg_no = get_valid_input("Enter the register number to delete: ")

	student = find_student_by_reg_no(reg_no)

	if student:
		print("Name: ", student["Name"])
		confirm = input("Are You sure about to delete this student (Y/N): ").strip().lower()

		if confirm == "y":
			students.remove(student)
			print("Student record deletion successful")
		else:
			print("Student record deletion Canceled.")
	else:
		print("No student record found")

#function to calculate average of all the students
def calc_avg():
	print("---- Calculate the Average Mark of All the Records ----")

	if not students:
		print("No Records found")
		return
	
	total = 0
	for student in students:

		total += student["Marks"]

	average = total / len(students)
	print(f"Average mark of the Records: {average:.2f}")

#function to find the topper (student with highest mark)
def find_topper():
	print("---- Finding Topper Student ----")
	if not students:
		print("No student record found")
		return
	highest_mark = max(student["Marks"] for student in students)

	print("Topper(s):")

	for student in students:
		if student["Marks"] == highest_mark:
			print(
				f"Name: {student['Name']}\n"
				f"Mark: {student['Marks']}\n"
			)

#function to assign grades to each students
def assign_grade():
	print("--- Grade Assignment ----")

	if not students:
		print("No Student records found")
		return
	
	for student in students:
		mark = student["Marks"]

		if mark >= 90:
			grade = "S"
		elif mark >= 80:
			grade = "A"
		elif mark >= 70:
			grade = "B"
		elif mark >= 60:
			grade = "C"
		elif mark >= 50:
			grade = "D"
		elif mark >= 40:
			grade = "E"
		else:
			grade = "F"

		student["Grade"] = grade

		print(
			f"Name: {student['Name']}\n"
			f"Mark: {mark}\n"
			f"Grade: {student['Grade']}\n"
		)

#function to sort Student records based on marks
def sort_students():
	if not students:
		print("No Student Records Available")
		return
	
	students.sort(
		key=lambda student:student["Marks"],
		reverse=True	
	)

	print("Students record have been sorted (Highest Mark)")

	display_students()


#main function
def main():
	while True:
		try:
			show_menu()
			choice = int(input("Enter Your Choice: "))

			match(choice):
				case 1:
					add_students()
				case 2:
					display_students()
				case 3:
					search_student()
				case 4:
					update_marks()
				case 5:
					delete_student()
				case 6:
					calc_avg()
				case 7:
					find_topper()
				case 8:
					assign_grade()
				case 9:
					sort_students()
				case 10:
					print("Exiting the program...")
					break
				case _:
					print("Invalid Choice")
		except ValueError:
			print("Invalid Input. Please enter a number.")
			continue

if __name__ == "__main__":
	main()