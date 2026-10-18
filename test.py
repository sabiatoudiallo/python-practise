from itertools import product
from os import name
# Practise 1
Name = 'Sabiatou' 
Surname = 'Diallo'#
Age = '22'
Favorite_colour = 'pink'
Faviorite_number = '7'
print('My name is', Name, Surname, ' and I am', Age, 'years old. My Favorite colour is', Favorite_colour, 'and my favorite number is', Faviorite_number)
ticket_price = 12
number_of_tickets = 4
Popcorn_price = 5
total_cost = number_of_tickets*ticket_price + Popcorn_price
print(total_cost)

Age = 21
Months = Age*12
print(Months) 

Name = 'Alexander'
print(len(Name))
print(Name[0])
print(Name[0:3])
print(Name[-3:-1])
print(Name[-1])

Laptop = 750
Mouse = 25
Keyboard = 45
Headphones = 80
total_cost = Laptop + Mouse + Keyboard + Headphones
print(total_cost)
Discount = 50
print(total_cost-Discount)

Monthly_salary = 2500
yearly_salary= Monthly_salary*12
print(yearly_salary)
Bonus = 2000
print(yearly_salary+Bonus)
Daily_salary_working_days = 260
Daily_salary_working_days = yearly_salary/260
print(Daily_salary_working_days)

Monthly_salary = 3000
yearly_salary = Monthly_salary*12
Bonus = 2000
total_salary = yearly_salary + Bonus
daily_salary= yearly_salary/260
print(Monthly_salary)
print(yearly_salary)
print(total_salary)
print(daily_salary)

Maths = 78
English = 82
Science = 91
History = 67
Computing = 88
total_marks= Maths + English + Science + History + Computing
print(total_marks)
Average_marks = total_marks/5
print(Average_marks)

Laptop_price = 800
units_sold = 12
Total_1 = Laptop_price*units_sold
Monitor_price = 250
units_sold_2 = 20
Total_2 = Monitor_price*units_sold_2
Keyboard_price = 50
Units_sold_3 = 35
Total_3 = Keyboard_price*Units_sold_3
Total_sales = Total_1 + Total_2 + Total_3
print(Total_sales)

print('hello world')

Students = {'Alex', 'Sarah', 'John', 'Alex', 'David', 'Sarah'}
print(Students)
Students.add('Emily')
print(Students)
Students.remove('John')
print(Students)
print('Alex' in Students)
emails = {"alex@gmail.com", "sarah@gmail.com", "alex@gmail.com", "john@gmail.com", "sarah@gmail.com"}
print(emails)
emails.remove('john@gmail.com')
print(emails)
print('alex@gmail.com' in emails)

print('hello world')

python_students = {'Alex', 'Sarah', 'John', 'David'}
sql_students = {'Sarah', 'David', 'Emma', 'James'}
students_in_both_courses = python_students.intersection(sql_students)
print(students_in_both_courses)
students_in_either_course = python_students.union(sql_students)
print(students_in_either_course)
students_in_python_not_sql = python_students.difference(sql_students)
print(students_in_python_not_sql)

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

