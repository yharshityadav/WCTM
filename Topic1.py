# Find the largest of two numbers
a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))
if a > b:
    print(a, "is the largest number")
else:
    print(b, "is the largest number")

# Check if a Number is positive, Negativ, Zero
a = int(input("Enter a Number:"))
if a > 0:
    print(a, "is a Positive Number")
elif a < 0:
    print(a, "is a Negative Number")
else:
    print(a, "is Zero")

# Swap two number
a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))
print("Before Swapping:")
print("First Number:", a)
print("Second Number:", b)
a, b = b, a
print("After Swapping:")
print("First Number:", a)
print("Second Number:", b)

# Print the Multiplication Table of a Number
a = int(input("Enter a Number:"))
for i in range(1, 11):
    print(a, "x", i, "=", a * i)

# Sum of all digit in a number
a = int(input("Enter a Number:"))
sum = 0
while a > 0:
    sum += a % 10
    a //= 10
print("Sum of all digit in a number:", sum)

# Print reverse order of list of numbers
a = [11,23,45,3,463,45,4,52,36,46,35,2,63,5]
a.reverse()
print("Reverse Order of List:", a)

# Check the vowels present in a string
a = input("Enter a String:")
vowels = "aeiouAEIOU"
for char in a:
    if char in vowels:
        print("Yes Vowel present in string")
    else:
      print("No Vowel is not present in string")

# Code to implement basic arithmetic operation on integar
a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))
sum = a + b
difference = a - b
product = a * b
quotient = a / b
reaminder = a % b
print("Sum of", a, "and", b, "is", sum)
print("Difference of", a, "and", b, "is", difference)
print("Product of", a, "and", b, "is", product)
print("Quotient of", a, "and", b, "is", quotient)
print("Remainder of", a, "and", b, "is", reaminder)

# list
list = [10,20,30,40]
list.append(50)
print(list)
list.pop(0)
print(list)
list.remove(30)
print(list)
list.sort()
print(list)
list.reverse()
print(list)

# find largest, smallest and equal
num1 = 10
num2 = 20
num3 = 30

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print("The largest number is", largest)
print("The smallest number is", smallest)

if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Two numbers are equal")


# tuples
tuple = (10,20,30,40)
print(tuple)
print(tuple[0])
print(tuple[1])
a,b,c,d = tuple
print(a,b,c,d)

# Set
set_a = {1,2,3}
set_b = {3,4,5}
print(set_a | set_b)
print(set_a & set_b)

# Dictionaries
student = {'name':'ALice','age':'20','grade':'A'}
print(student.get('age'))
print(student.keys())
print(student.values())

# Write a code to find the area of equilateral triangle(and area should in float)
side = float(input("Enter the Side of Equilateral Triangle:"))
area = (1.732050807568877*side*side)/4
print("Area of Equilateral Triangle is",area)

# Write a code of area of Rhombus
d1 = float(input("Enter the First Diagonal of Rhombus:"))
d2 = float(input("Enter the Second Diagonal of Rhombus:"))
area = (d1*d2)/2
print("Area of Rhombus is",area)

# Write a code of comparing three number and display the largest, smallest and middle number
num1 = float(input("Enter the first Number:"))
num2 = float(input("Enter the second Number:"))
num3 = float(input("Enter the third Number:"))
if num1>num2 and num1>num3:
  print(num1,"is the largest number")
elif num2>num1 and num2>num3:
  print(num2,"is the largest number")
else:
  print(num3,"is the largest number")
if num1<num2 and num1<num3:
  print(num1,"is the smallest number")
elif num2<num1 and num1<um3:
  print(num2,"is the smallest number")
else:
  print(num3,"is the smallest number")
if num1>num2 and num1<num3:
  print(num1,"is the middle number")
elif num2>num1 and num2<num3:
    print(num2,"is the middle number")
else:
    print(num3,"is the middle number")

# Write a code of making calculator with different cases of operators and with display the result
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = (input("Enter the operator"))
if c == "+":
  print(a+b)
elif c == "-":
  print(a-b)
elif c == "*":
  print(a*b)
elif c == "/":
  print(a/b)1