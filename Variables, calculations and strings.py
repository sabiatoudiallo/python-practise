# A customer buys 4 cinema tickets at £12 each and a tub of popcorn for £5. Calculate the total cost of the purchase.
ticket_price = 12
number_of_tickets = 4
Popcorn_price = 5
total_cost = number_of_tickets*ticket_price + Popcorn_price
print(total_cost)
# Ticket_price stores the price of one ticket.
# number_of_tickets stores how many tickets are purchased.
# popcorn_price stores the price of the popcorn.
# Multiplication calculates the total cost of tickets: 4 x 12 = 48
# Addition adds the cost of the popcorn to the total cost of tickets: 48 + 5 = 53
# print() displays the total cost of the purchase, which is 53.

# A person is 21 years old. Calculate how many months old they are. 
Age = 21
Months = Age*12
print(Months) 
# Age stores the person's age in years.
# Multiplying it by 12 converts the number of years into months. 21 x 12 = 252

# Given the name "Alexander", write a program that counts how many characters it contains.
Name = 'Alexander'
print(len(Name))
# A string is a sequence of characters.
# Python's built in Len() function counts the number of characters in that sequence.
# 'Alexander' contains nine characters, so len(name) returns 9.
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