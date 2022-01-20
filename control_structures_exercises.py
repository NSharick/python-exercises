# control structures exercises

#1a
#possible inputs ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
today_is = input('Enter a three character day of the week:')

if today_is == 'mon':
    print('Today is Monday')
else:
    print('Today is not Monday')


#1b
#possible inputs ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
today_is = input('Enter a three character day of the week:')

if today_is in ('sat', 'sun'):
    print('Its the weekend')
else:
    print('Its a weekday')

##from lesson review -- written this way the statement has better input control by switching the inpur to all lower and only looking at the letter that the input starts with
today_is = input('Enter a three character day of the week:')

if today_is.lower().startswith('s'):
    print('weekend')
else:
    print('weekday')



#1c
hours_worked_in_week = 50
hourly_rate = 25

if hours_worked_in_week <= 40:
    weeks_paycheck = hours_worked_in_week * hourly_rate
else:
    weeks_paycheck = (hours_worked_in_week * hourly_rate) + ((hours_worked_in_week - 40) * (hourly_rate / 2))
print(weeks_paycheck) 

##from lesson review -- writing the statement like this makes it easyer to read by defining all the variables seperately
if hours_worked_in_week <= 40:
    paycheck = hours_worked_in_week * hourly_rate
else:
    overtime_hours = hours_worked_in_week - 40
    overtime_pay = overtime_hours * 1.5 * hourly_rate
    base_pay = 40 * hourly_rate
    paycheck = base_pay + overtime_pay

print(paycheck)


#2a
i = 5
while i <= 15:
    print(i)
    i += 1

x = 0
while x <= 100:
    print(x)
    x += 2

y = 100
while y >= -10:
    print(y)
    y -= 5

a = 2
while a <= 1000000:
    print(a)
    a = a * a

b = 100
while b >= 5:
    print(b)
    b -= 5


#2b
n = input("enter a positive integer:")
n = int(n)
for number in range(1, 11):
    print(f'{n} X {number} = {n * number}')


for number in range(1, 10):
    print(str(number) * number)


#2c
x = input('Enter a number between 1 and 50:')
x = int(x)
for n in range(51):
    if n % 2 == 0:
        continue
    elif n == x:
        print(f'Yikes! Skipping number: {n}')
    else:
        print(f'Here is an odd number: {n}')

## from lesson review -- added more input control with .isdigit and making sure the input is an odd number before calling 
while True:
    posited_num = input('Please insert an odd number between 1 and 50: ')
    if posited_num.isdigit():
        if int(posited_num) % 2 == 1 and int(posited_num) <= 50:
            break

posited_num = int(posited_num)

for num in range(1, 50, 2):
    if num == posited_num:
        print('Yikes! skipping number: ', num)
    else:
        print('Here is an odd number: ', num)


#2d
x = input('Enter a positive whole number:')
x = int(x)
i = 0
while i <= x:
    print(i)
    i += 1

y = input('Enter a positive integer:')
y = int(y)
while y >= 1:
    print(y)
    y-= 1


#3
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('fizzbuzz')
    elif x % 3 == 0:
        print('fizz')
    elif x % 5 ==0:
        print('buzz')
    else:
        print(x)


#4
x = input('What number would you like to go up to?:')
x = int(x)
print('Here is your table!')
for i in range(1, x+1):
    print(i, '|', i**2, '|', i**3)


#5
grd = input('Enter a numerical grade from 0 - 100:')
grd = int(grd)
if grd in range(88, 101):
    print('A')
elif grd in range(80, 88):
    print('B')
elif grd in range(67, 80):
    print('C')
elif grd in range(60, 67):
    print('D')
elif grd in range(0, 60):
    print('F') 


grd = input('Enter a numerical grade from 0 - 100:')
grd = int(grd)
if grd in range(99, 101):
    print('A+')
elif grd in range(90, 99):
    print('A')
if grd in range(88, 90):
    print('A-')
if grd in range(86, 88):
    print('B+')
elif grd in range(82, 86):
    print('B')
elif grd in range(80, 82):
    print('B-')
elif grd in range(78, 80):
    print('C+')
elif grd in range(69, 78):
    print('C')
elif grd in range(67, 69):
    print('C-')
elif grd in range(65, 67):
    print('D+')
elif grd in range(62, 65):
    print('D')
elif grd in range(60, 62):
    print('D-')
elif grd in range(0, 60):
    print('F') 


#6
books = [{'title': 'Extreme Ownership' , 'author': 'Jocko Wilnik', 'genre': 'leadership'},
         {'title': 'Grit', 'author': 'Angela Duckworth', 'genre': 'popular applied psychology'},
         {'title': 'At the grave of the unknown fisherman' , 'author': 'John Gierach', 'genre': 'sports and outdoors'},
         {'title': 'The Naturalist', 'author': 'Darrin Lunde' , 'genre': 'biography'}]

for book in books:
    print(f"title: {book['title']}, author: {book['author']}, genre: {book['genre']}")


x = input('Enter a genre:')
for book in books:
    if x in book['genre']:
        print(f"Title: {book['title']}, Author: {book['author']} ")



