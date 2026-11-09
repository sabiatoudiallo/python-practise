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

# USEFUL FOR TEXT PROCESSING AND DATA VALIDATION.
# Given the name "Alexander", write a program that counts how many characters it contains.
Name = 'Alexander'
print(len(Name))
print(Name[0])
print(Name[-1])
# A string is a sequence of characters.
# Python's built in Len() function counts the number of characters in that sequence.
# 'Alexander' contains nine characters, so len(name) returns 9.
# As python uses a zero-based indexing, the first character is at index 0.
# Negative indexes count backwards from the end of the string, so -1 identifies the last character.

# Given the name "Alexander", write a program that prints the first three characters and the last three characters of the name.
print(Name[0:3])
print(Name[-3:-1])
# String slicing follows the pattern string[start:end].
# The starting position is included, but the ending position is excluded.
# Name[0:3] returns the first three characters producing "Ale".
# Name[-3: -1] starts at the third character from the end and stops before the last character, producing "de".


# A customer purchases the following computer equipment:
# Laptop: £750
# Mouse: £25
#Keyboard: £45
#Headphones: £80
# The customer receives a £50 discount on the total purchase.
#  Calculate the total cost before the discount and the final cost after the discount.
Laptop = 750
Mouse = 25
Keyboard = 45
Headphones = 80
total_cost = Laptop + Mouse + Keyboard + Headphones
print(total_cost)
Discount = 50
print(total_cost-Discount)
# Each variable holds the price of one item. For example, laptop = 750 stores the laptop's price as £750
# The + operator adds all four prices together: 750 + 25 + 45 + 80 = 900
# The discount variable stores the £50 discount
# The - operator subtracts the discount from the original total: 900 - 50 = 850
# Print() to display results


# An employee earns a monthly salary of £2,500. They receive an annual bonus of £2,000 and work 260 days per year.
# Calculate the employee's yearly salary.
# Calculate their total annual earnings, including the bonus.
# # Calculate their daily salary based on 260 working days per year, excluding the bonus.
Monthly_salary = 2500
yearly_salary= Monthly_salary*12
print(yearly_salary)
Bonus = 2000
print(yearly_salary+Bonus)
Daily_salary_working_days = 260
Daily_salary_working_days = yearly_salary/260
print(Daily_salary_working_days)
# The employee earns £2,500 per month. Multiplying this by 12 gives their yearly salary: 2500 x 12 = 30,000
# The bonus is added to the yearly salary to calculate total annual earnings: 30,000 + 2,000 = 32,000
# The yearly salary is divided by 260 to calculate the daily salary: 30,000 / 260 = 115.38 excluding the bonus.

# An employee earns a monthly salary of £3,000. They receive an annual bonus of £2,000 and work 260 days per year.
#1. Stores the employee's monthly salary.
#2. Calculate their yearly salary.
#3. Calculate their total annual earnings, including the bonus.
#4. Calculate their daily salary based on 260 working days, excluding the bonus.
#5. Prints all four results.
Monthly_salary = 3000
yearly_salary = Monthly_salary*12
Bonus = 2000
total_salary = yearly_salary + Bonus
daily_salary= yearly_salary/260
print(Monthly_salary)
print(yearly_salary)
print(total_salary)
print(daily_salary)
# The variable Monthly_salary stores the employee's monthly salary of £3,000.
# There are 12 months in a year, so we multiply the month salary by 12. £3,000 x 12 = £36,000
# The employee receives an annual bonus of £2,000. We add this to the yearly salary. £36,000 + £2,000 = £38,000, including the bonus.
# The yearly salary is divided by 260 to calculate the daily salary: £36,000 / 260 = £138.46 excluding the bonus.
# The print() function displays all four results.



# A student receives the following marks across five subjects:
# - Maths: 78
# - English: 82
# - Science: 91
# - History: 67
# - Computing: 88
# Calculate the student's total marks across all five subjects and their average mark.
Maths = 78
English = 82
Science = 91
History = 67
Computing = 88
total_marks = Maths + English + Science + History + Computing
print(total_marks)
Average_marks = total_marks/5
print(Average_marks)
# Each variable stores the student's mark for one subject. This makes the marks easy to use in calculations.
# The + operator adds all five marks together to calculate the total marks: 78 + 82 + 91 + 67 + 88 = 406
# The total marks are divided by 5 to calculate the average mark: 406 / 5 = 81.2
# The average represents the mean mark across all five subjects.



# An electronics store sells three types of computer equipment. During a sales period, the store sells:
# - Laptops: 12 units at £800 each.
# - Monitors: 20 units at £250 each.
# - Keyboards: 35 units at £50 each.
# Calculate the sales revenue for each product and then calculate the store's total sales revenue across all three products.
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
# The laptop price is £800 and 12 units are sold. 
# Multiplying these together gives the total sales revenue for laptops: £800 x 12 = £9,600
# The store sells 20 monitors at £250 each. £250 x 20 = £5,000
# The store sells 35 keyboards at £50 each. £50 x 35 = £1,750
# The product revenues are added together to calculate the overall sales revenue: £9,600 + £5,000 + £1,750 = £16,350
