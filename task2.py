# Arithmetic Expression Task
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = int(input("Enter value of d: "))
e = int(input("Enter value of e: "))

result = (a + b) * (c - d) / e
print("Result:", result)


# Power and Modulus Task
num = int(input("Enter a number: "))
print("Square:", num ** 2)
print("Cube:", num ** 3)
print("Modulus (num % 2):", num % 2)


# Multiple Assignment Operator Task
x = 10
print("Initial value:", x)

x += 5
print("After += :", x)

x *= 2
print("After *= :", x)

x -= 4
print("After -= :", x)

x /= 2
print("After /= :", x)


# Comparison Result Display
a = 15
b = 10

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


# Logical Evaluation Task
p = True
q = False
r = True

print("p and q :", p and q)
print("p or q :", p or q)
print("not p :", not p)
print("q and r :", q and r)
print("p or r :", p or r)


# Bitwise Calculation Task
x = 10
y = 5

print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)


# Membership Test on String
text = "Python Training Program"

print("'Python' in text:", "Python" in text)
print("'Java' not in text:", "Java" not in text)


# Identity Operator Practice
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)


# String Multiplication Task
msg = "Python "
print(msg * 5)


# Operator Precedence Task
result = 10 + 5 * 2 ** 2 - 8 / 2
print("Final result:", result)


