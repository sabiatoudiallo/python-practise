# laptop_sales = 120
# Phone_sales = 150
# print(laptop_sales > Phone_sales)
# print(Phone_sales > laptop_sales)
# print(laptop_sales == Phone_sales)
# print(laptop_sales < Phone_sales)

# # customers get a discount if they are 18 or older and purchase is 100 or more
# Age = 25
# Purchase = 120
# print(18<= Age and Purchase >= 100)
# Age = {'Age': 17}
# print(18>= Age['Age'] and Purchase >= 100)
# Purchase = ({'purchase': 80})
# print(18>= Age['Age'] and Purchase['purchase'] >=100)

# Products = {'laptop', 'Phone', 'Tablet', 'keyboard', 'Mouse'}
# print('laptop' in Products)
# print('printer' not in Products)
# print('camera' not in Products)

#     # Customers under 18 or 65 or over get a discount
#     Age = 25
#     print(Age < 18 or Age >= 65)
#     Age = ({'age': 16}, {'age': 70})
#     print(Age[0]['age'] < 18 or Age[1]['age'] >= 65)

# Age = 20
# if Age < 13: 
#     print('child')
# elif Age < 18:
#     print('Teenage')
# else: 
#     print('Adult')
# Age = 10
# if Age <13:
#     print('child')
# elif Age < 18:
#     print('Teenager')
# else:
#     print('Adult')
# Age = 15
# if Age < 13:
#     print('child')
# elif Age < 18:
#     print('Teenager')
# else:
#     print('Adult')
# Age = 25
# if Age < 13:
#     print ('child')
# elif Age <18:
#     print('Teenager')
# else:
#     print('Adult')

# Score = 75
# if Score >= 70:
#     print('A')
# elif Score >= 60:
#     print('B')
# elif Score >= 50:
#     print('C')
# else:
#     print('Fail')

# Purchase = 120
# if Purchase >= 200:
#     print('20 discount')
# elif Purchase >= 100:
#     print('10 discount')
# elif Purchase >= 50:
#     print('5 discount')
# else:
#     print('No discount')
# discount = Purchase * 10/100
# print(discount)
# final_price = Purchase - discount
# print(final_price)

# Salary = 35000
# if Salary <30000:
#     print('junior') 
# elif Salary>= 30000:
#     print('mid-level')
# else:
#     print('Senior') 

range(1, 11)
for number in range(1, 11):
    print(number)

range(10, 0, -1)
for number in range(10, 0, -1):
    print(number)

fruits = ["apple", "banana", "orange", "grape"]

for fruit in fruits:
    print(fruit)

numbers = [2, 4, 6, 8, 10]
for number in numbers:
    print(number*2)

    for number in range(1, 21):
        if number % 2 == 0:
            print(number)

numbers = [5, 10, 15, 20]
total = 0
for number in numbers:
    total = total + number
    print(total)

# Use a for loop to print each character on a sparate line.
name = 'python' 
for letter in name:
    print(letter)

# Count how many numbers in this list are greater than 10:
numbers = [4,15,7,22,3,18,9]

count = 0

for number in numbers:
    if number > 10:
        count = count + 1
        print(count)

# write a loop that prints "Even" if a number is even and "odd" if a number is odd:
numbers = [3, 8, 11, 14, 17, 20]
for number in numbers:
    if number % 2 == 0:
     print(number, 'Even')
    else:
        print(number,'Odd')

# Find the largest number in:
numbers = [12, 45, 7, 89, 34, 23]

largest = numbers[0]

for number in numbers:
 if number > largest:
    largest = number
    print(largest)

# Count how many times the letter "a" appears in:
word = "banana"

count = 0

for letter in word:
    if letter == "a":
        count += 1

        print(count)

# Print "Pass" for scores ≥ 60 and "Fail" for scores below 60.
scores = [55, 72, 91, 48, 86, 67]
for score in scores:
    if score >= 60:
        print(score,'pass')
    else:
        print(score,'fail')


# Calculate the average of this using a loop.
# Average = total/number of scores
scores = [80, 90, 70, 60, 100]

total = 0
count = 0

for score in scores:
    total += score
    count += 1

average = total / count

print(average)

# Write a for loop that prints each name
names = ["Alex", "John", "Sarah", "Mike"]
for name in names:
    print(name)

# Write a loop that prints each number multiplied by 2
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number*2)

# What will this output?
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number + 10)
# Answer - 11, 12, 13, 14

# Write a loop that prints only the numbers greater than 50:
numbers = [20, 75, 42, 90, 15, 63]
for number in numbers:
    if number > 50: 
        print(number)

# Write a loop that calculates the sum of:
numbers = [10, 20, 30, 40]
total = 0
for number in numbers:
   total = total + number
print(total)

# Write a loop that prints whether each number is even or odd
numbers = [12, 7, 9, 20, 31]
for number in numbers:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

# Write a loop that prints only sales greater than 1000
sales = [500, 1200, 300, 2500, 800]
for x in sales:
    if x > 1000:
     print(x)

# Write a loop that counts how many numbers are greater than 50
numbers = [25, 75, 80, 10, 45, 90, 100]

count = 0
for number in numbers:
    if number > 50:
        count += 1
        print(number)

# Use a for loop to print only salaries above 40,000
salaries = [35000, 42000, 55000, 28000, 75000]
for x in salaries:
    if x > 40000:
        print(x)

#Calculate the average of:
sales = [100, 250, 300, 150, 200]
cost = 0
total = 0
for x in sales:
        total = total + x # or total += x
        cost += 1
        average = total / cost
        print(average)

# These are customers ages. Use a for loop to print only customers who are 18 or older
ages = [18, 25, 42, 16, 30, 14, 55]
for age in ages:
    if age >= 18:
        print(age)

# Use a loop to print:
# Laptop costs £1000
#Mouse costs £25
#Keyboard costs £50
#Monitor costs £300

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [1000, 25, 50, 300]
for i in range(len(products)):
    print(f'{products[i]} costs £{prices[i]}')

# Use a loop to calculate how many sales were £1000 or more
sales = [1200, 500, 750, 2000, 300]

count = 0
for sale in sales:
    if sale >= 1000:
        count += 1
        print(count)

# Use a for loop to find the largest number without using Python's max() function
numbers = [10, 25, 3, 89, 42, 7, 100]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
        print(largest)

# Level 3 - Nested for loops
for i in range(1,4):
    for j in range (1,4):
        print(i,j)

for i in range(1, 6):
    for j in range(i):
      print("*", end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Use nested loops to print every possible department/employee combination.
departments = ["Sales", "Marketing", "Finance"]
employees = ["Alice", "Bob", "Charlie"]
for department in departments:
    for employee in employees:
        print(department, employee)

# Use nested loops to print every number
numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
for row in numbers:
    for number in row:
        print(number)

for i in range(3):
    for j in range(1,4):
     print(j, end=" ")
    print()

for i in range(4):
    for j in range(1, 5):
        print(j, end=" ")
    print()

    #What will this output?
    for i in range(5):
     print(i)
     # 1
     # 2
     # 3
     # 4

for i in range(1, 21):
    print(i)

for i in range(5):
    print('Hello')


# write a loop that prints the number 10 to 1.
for i in range(10, 0, -1):
    print(i)

fruits = ["Apple", "Banana", "Orange", "Mango"]
for fruit in fruits:
    print(fruit)

numbers = [2, 4, 6, 8, 10]
for number in numbers:
    print(number *2)


# Create a function called 'greet' that prints:
def greet():
 print('Hello, welcome to python!')
    
greet()

# print 'say hello' three times
def say_hello():
 print('Hello!')
 

say_hello()
say_hello()
say_hello()

# What will this code print? answer: Learning python, Learning python
def my_function():
    print("Learning Python")

my_function()
my_function()


def greet():
 print("Hello!")

greet()


def greet_user(name):
  print(f'Hello, {name}!')

greet_user("Alex")

