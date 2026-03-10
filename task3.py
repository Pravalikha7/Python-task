name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))

yearly_salary = salary * 12

print("\n--- Employee Details ---")
print("Name:", name)
print("Age:", age)
print("Monthly Salary:", salary)
print("Yearly Salary:", yearly_salary)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Arithmetic Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)

print("\n--- Comparison Results ---")
print("num1 > num2 :", num1 > num2)
print("num1 < num2 :", num1 < num2)
print("num1 >= num2 :", num1 >= num2)
print("num1 <= num2 :", num1 <= num2)
print("num1 == num2 :", num1 == num2)
print("num1 != num2 :", num1 != num2)


marks = int(input("Enter student marks: "))
attendance = float(input("Enter attendance percentage: "))

eligible = marks >= 60 and attendance > 75

print("\n--- Placement Eligibility ---")
print("Marks:", marks)
print("Attendance:", attendance)

if eligible:
    print("Student is Eligible for Placement")
else:
    print("Student is Not Eligible for Placement")
    
    
    marks = int(input("Enter student marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\nGrade:", grade)

if marks >= 60:
    print("Eligible for Higher Level Training")
else:
    print("Not Eligible for Higher Level Training")