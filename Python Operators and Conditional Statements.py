laptop_sales = 120
Phone_sales = 150
print(laptop_sales > Phone_sales)
print(Phone_sales > laptop_sales)
print(laptop_sales == Phone_sales)
print(laptop_sales < Phone_sales)

# customers get a discount if they are 18 or older and purchase is 100 or more
Age = 25
Purchase = 120
print(18<= Age and Purchase >= 100)
Age = {'Age': 17}
print(18>= Age['Age'] and Purchase >= 100)
Purchase = ({'purchase': 80})
print(18>= Age['Age'] and Purchase['purchase'] >=100)

Products = {'laptop', 'Phone', 'Tablet', 'keyboard', 'Mouse'}
print('laptop' in Products)
print('printer' not in Products)
print('camera' not in Products)

 # Customers under 18 or 65 or over get a discount
Age = 25
print(Age < 18 or Age >= 65)
Age = ({'age': 16}, {'age': 70})
print(Age[0]['age'] < 18 or Age[1]['age'] >= 65)

Age = 20
if Age < 13: 
    print('child')
elif Age < 18:
    print('Teenage')
else: 
    print('Adult')
Age = 10
if Age <13:
    print('child')
elif Age < 18:
    print('Teenager')
else:
    print('Adult')
Age = 15
if Age < 13:
    print('child')
elif Age < 18:
    print('Teenager')
else:
    print('Adult')
Age = 25
if Age < 13:
    print ('child')
elif Age <18:
    print('Teenager')
else:
    print('Adult')

Score = 75
if Score >= 70:
    print('A')
elif Score >= 60:
    print('B')
elif Score >= 50:
    print('C')
else:
    print('Fail')

Purchase = 120
if Purchase >= 200:
    print('20 discount')
elif Purchase >= 100:
    print('10 discount')
elif Purchase >= 50:
    print('5 discount')
else:
    print('No discount')
discount = Purchase * 10/100
print(discount)
final_price = Purchase - discount
print(final_price)

Salary = 35000
if Salary <30000:
    print('junior') 
elif Salary>= 30000:
    print('mid-level')
else:
    print('Senior') 