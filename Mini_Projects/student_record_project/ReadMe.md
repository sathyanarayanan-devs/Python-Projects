# Student Management System

A beginner-friendly, menu-driven Student Management System built using Python. This application allows users to manage student records, update marks, calculate averages, assign grades, identify toppers, and sort records by marks.

**Current Storage:** Student records are stored in memory while the program is running. Data is lost when the application is closed.

## Features

- **Add Students:** Add student details including name, registration number, and marks.
- **View Students:** Display all student records in a formatted table.
- **Search Students:** Search for a student using their registration number.
- **Update Marks:** Modify the marks of an existing student.
- **Delete Students:** Delete student records after confirmation.
- **Calculate Average:** Calculate the average marks of all students.
- **Find Topper:** Identify the student(s) with the highest marks, including ties.
- **Assign Grades:** Automatically assign grades based on marks.
- **Sort Students:** Sort student records in descending order of marks.
- **Input Validation:** Handle empty inputs, invalid marks, and incorrect menu choices.

## Requirements

- Python 3.10 or later.
- No external Python libraries are required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the following command:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## Data Structure

Student records are stored in a Python list containing dictionaries.

Example:

```python
{
    "Name": "Arun",
    "Reg_No": "101",
    "Marks": 85.0
}
```

The application uses functions to perform different operations on student records.

## Grade Assignment Rules

| Marks    | Grade |
| -------- | ----- |
| 90–100   | S     |
| 80–89.99 | A     |
| 70–79.99 | B     |
| 60–69.99 | C     |
| 50–59.99 | D     |
| 40–49.99 | E     |
| Below 40 | F     |

These are the currently configured practice grading rules.

## Input Validation

- Name and registration number cannot be empty.
- Marks must be numeric and between 0 and 100.
- Duplicate registration numbers are rejected.
- Invalid menu inputs are handled without terminating the application.

## Testing Checklist

- [ ] Add multiple student records.
- [ ] Check duplicate registration number validation.
- [ ] Test empty name and registration number inputs.
- [ ] Test invalid marks.
- [ ] Search for existing and non-existing students.
- [ ] Update a student's marks.
- [ ] Delete a student record.
- [ ] Calculate the average marks.
- [ ] Find toppers when multiple students have equal marks.
- [ ] Verify grade assignments.
- [ ] Sort student records by marks.
- [ ] Test invalid menu choices.

## Current Limitations

- Student records are stored only in memory.
- All records are lost when the application is closed.
- The application uses a command-line interface.
- No database or file storage is implemented yet.


## Learning Outcomes

Through this project, I practised:

- Python lists and dictionaries.
- Functions and modular programming.
- Loops and conditional statements.
- Searching and sorting.
- Input validation and exception handling.
- Mutable objects and references.
- CRUD operations (Create, Read, Update, Delete).

---