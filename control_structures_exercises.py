# control structures exercises

#1a
the_day_is_monday = True

if the_day_is_monday:
    print('Today is Monday')

#1b
#possible inputs ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
today_is = 'wed'

if today_is in ('sat', 'sun'):
    print('Its the weekend')
else:
    print('Its a weekday')

#1c
hours_worked_in_week = 50
hourly_rate = 25

if hours_worked_in_week <= 40:
    weeks_paycheck = hours_worked_in_week * hourly_rate
else:
    weeks_paycheck = (hours_worked_in_week * hourly_rate) + ((hours_worked_in_week - 40) * (hourly_rate / 2))
print(weeks_paycheck) 

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
