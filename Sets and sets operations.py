# A school maintains a collection of student names and email addresses. 
# The school wants to ensure that duplicate entries are stored only once, add new students, remove students who have left a list, and check whether particular students or email addresses exist.
# Write a Python program that:
# 1. Creates a set of student names, including some duplicates.
# 2. Adds a new student named Emily.
# 3. Removes John from the student set.
Students = {'Alex', 'Sarah', 'John', 'Alex', 'David', 'Sarah'}
print(Students)
Students.add('Emily')
print(Students)
Students.remove('John')
print(Students)
print('Alex' in Students)

# 4. Checks whether Alex is still in the set.
# 5. Creates a set of email addresses containing duplicates.
# 6. Removes John's email address.
# 7. Checks whether Alex's email address exists in the set.
emails = {"alex@gmail.com", "sarah@gmail.com", "alex@gmail.com", "john@gmail.com", "sarah@gmail.com"}
print(emails)
emails.remove('john@gmail.com')
print(emails)
print('alex@gmail.com' in emails)



# A training academy offers two courses: Python programming and SQL databases.
# The academy has the following students enrolled:
# - Python course: Alex, Sarah, John and David.
# - SQL course: Sarah, David, Emma and James.
# Write a program that uses set operations to:
# 1. Identify students enrolled in both courses.
# 2. Identify all students enrolled in either course, without duplicates.
# 3. Identify students enrolled in the Python course but not the SQL course.
python_students = {'Alex', 'Sarah', 'John', 'David'}
sql_students = {'Sarah', 'David', 'Emma', 'James'}
students_in_both_courses = python_students.intersection(sql_students)
print(students_in_both_courses)
students_in_either_course = python_students.union(sql_students)
print(students_in_either_course)
students_in_python_not_sql = python_students.difference(sql_students)
print(students_in_python_not_sql)



# Create a Python dictionary to store a student's information, including their name, age, course, and country. 
# Print the entire dictionary and access individual values using their keys.
Student = {
    'name': 'Alex',
    'age': 22,
    'course': 'Data analytics',
    'country': 'UK'
}
print(Student)
print(Student['name'])
print(Student['age'])
print(Student['course'])


#  Createa Python dictionary to store a employees information, including their name, job title and salary.
# Print the entire dictionary and access individual values using their keys.
employee = {
    'name': 'Sarah',
    'job': 'Data Analyst',
    'Salary': 3000,
}
print(employee)
employee.update({'Salary': 3500})
employee['department'] = 'Analytics'
print(employee)
print(employee['Salary'])
print(employee['department'])

# Create a Python dictionary to store product information, including the product name, brand, price, and stock quantity
# Display the complete dictionary, access specific values, update the stock quantity, and add a new category to the dictionary.
Product = {
    'name': 'laptop',
    'brand': 'Dell',
    'price': 800,
    'stock': 15
}
print(Product)
print(Product['name'])
print(Product['price'])
Product.update({'stock': 20})
print(Product['stock'])
Product['category'] = 'electronics'
print(Product['category'])

# Create two Python dictionaries to store employee names and salaries.
# Display each employee's salary using f-strings, update the first employee's salary, and print the updated information.
employee1 = {
    'name': 'Alex',
    'salary': 30000,
}

employee2 = {
    'name': 'Sarah',
    'salary': 35000,
}
print(f"{employee1['name']} earns {employee1['salary']}")
print(f"{employee2['name']} earns {employee2['salary']}")
employee1.update({'salary': 32000})
print(f"{employee1['name']} earns {employee1['salary']}")



# Create a Python program to manage product information using dictionaries and sets.
# Store a product's name, price, number sold, and category.
# Display product details, update the number sold, and add a supplier.
# Then use sets to compare products in stock with products sold, identifying products that appear in both sets.
# identify products that are in stock but not sold, and combine both sets to display all unique products.
product = {
    'name':'Laptop',
    'price': 800,
    'number_sold': 15,
    'category': 'electronics'
}
print(product)
print(product['price'])
print(product['number_sold'])
product.update({'number_sold': 20})
product['supplier'] ='Dell'
print(product)
product_in_stock = {'keyboard', 'monitor', 'mouse', 'printer'}
product_sold = {'laptop', 'keyboard', 'laptop', 'mouse', 'headphones'}
both = product_in_stock.intersection(product_sold)
print(both)
in_stock_not_sold = product_in_stock.difference(product_sold)
print(in_stock_not_sold)
products_in_either = product_in_stock.union(product_sold)
print(products_in_either)