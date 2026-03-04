#Part-1:Data Types

#Creating Variables

a = 250
b = 45.75
c = "Python Training"
d = True
e = [10,20,30,40,50]
f = (5,10,15)
g = {1,2,3,4}
h = {"Course":"Python","Duration":"3 Months"}

#Printing Data Types

print("             Data Types                 ")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

#Part:2-Indexing Operations

#String Indexing

text = "Programming"
print("\n          String Indexing           ")
print("First character:",text[0])
print("Fourth character:",text[3])
print("Last character:",text[-1])

#List Indexing

numbers = [100,200,300,400,500]
print("\n          List Indexing           ")
print("Second element:",numbers[1])
print("Fourth element:",numbers[3])
print("Last element:",numbers[-1])

#Part:3-Slicing Operations

#String Slicing

data = "Data Science"
print("\n          String Slicing           ")
print("First 5 characters:",data[:5])
print("Last 4 characters:",data[-4:])
print("Characters from index 2 to 7:",data[2:8])

#List Slicing

nums = [1,2,3,4,5,6]
print("\n          List Slicing           ")
print("First 4 elements:",nums[:4])
print("Elements from index 1 to 4:",nums[1:5])
print("Reversed list:",nums[::-1])