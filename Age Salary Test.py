age = int (raw_input ("Age: "))
salary = int (raw_input ("Salary: "))

x1 = 10
x2 = 20
x3 = 30
x4 = 40
x5 = 50
x6 = 60

if age >= 0 and age <= 10:
    benefit = salary*10/100.0
if age >= 10 and age <= 20:
    benefit = salary*20/100.0
if age >= 20 and age <= 30:
    benefit = salary*30/100.0
if age >= 30 and age <= 40:
    benefit = salary*40/100.0
if age >= 40 and age <= 50:
    benefit = salary*50/100.0
if age >= 50 and age <= 60:
    benefit = salary*60/100.0
if age >= 60:
    benefit = salary*70/100.0

print benefit
