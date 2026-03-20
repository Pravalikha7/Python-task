# ================================
# TASK 01: STRINGS
# ================================

text = "   Hello Python World   "

print("Original:", text)
print("Slice [3:15]:", text[3:15])
print("Reverse:", text[::-1])

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Strip:", text.strip())

words = text.strip().split(" ")
print("Split:", words)

joined = "-".join(words)
print("Join:", joined)

new_text = text.replace("Python", "Java")
print("Replace:", new_text)


# ================================
# TASK 02: LISTS
# ================================

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]
print("Squares:", squares)

even = [x for x in numbers if x % 2 == 0]
print("Even:", even)

numbers.append(6)
print("Append:", numbers)

numbers.extend([7, 8])
print("Extend:", numbers)

numbers.insert(0, 0)
print("Insert:", numbers)

numbers.remove(3)
print("Remove:", numbers)

numbers.pop()
print("Pop:", numbers)

numbers.sort(reverse=True)
print("Sort Desc:", numbers)


# ================================
# TASK 03: TUPLES & SETS
# ================================

tuple_data = (10, 20, 30)

a, b, c = tuple_data
print("Unpacking:", a, b, c)

list_data = [1, 2, 2, 3, 4, 4]
unique = set(list_data)
print("Remove duplicates:", unique)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)


# ================================
# TASK 04: DICTIONARIES
# ================================

student = {
    "name": "Prav",
    "age": 20,
    "marks": {"math": 90, "science": 85}
}

print("Name:", student["name"])
print("Math Marks:", student["marks"]["math"])

student["age"] = 21
student["grade"] = "A"

for key, value in student.items():
    print(key, ":", value)

students = {
    "s1": {"name": "A", "marks": 80},
    "s2": {"name": "B", "marks": 90}
}

for s, details in students.items():
    print(s, details["name"], details["marks"])
