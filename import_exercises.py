##Import Exercises##


#1a 
#import the is_vowel function from my function_exercises.py
from curses import ALL_MOUSE_EVENTS
from function_exercises import is_vowel

#test the function
is_vowel('a')
is_vowel('b')
is_vowel('c')


#1b
#import the calculate tip function from my function_exercises.py
from function_exercises import calculate_tip

#test the function
calculate_tip(.2, 100)
calculate_tip(.12, 100)
calculate_tip(.5, 100)
calculate_tip(.13, 100)


#2
#itertools module - python standard library

import itertools

#cast the created itertools object as a list for readability
print(list(itertools.product('abc', '123')))
#assign the created itertools object to a variable to work with it
x = list(itertools.product('abc', '123'))
#print the length of the list for the new variable to get the number of combinations to answer the exercise
print(len(x))

print(list(itertools.combinations('abcd', 2)))
y = list(itertools.combinations('abcd', 2))
print(len(y))

print(list(itertools.permutations('abcd', 2)))
z = list(itertools.permutations('abcd', 2))
print(len(z))


#3
#json module

import json

profiles = json.load(open('profiles.json'))

#A
#how many users - since it is a list of dictionaries with one dictionary for each user we can get the number of users by getting the length of the list.
print(len(profiles))

#B   
#number of active users
#start a count at 0
count_active = 0
#loop through the list and check for 'isActive' = true and add to the count for each
for user in profiles:
    if user['isActive'] == True:
        count_active += 1
#print the value of the count after the loop is complete 
#(make sure to have the print statement outside of the loop by not having any indentations)  
print(count_active)

#C
#number of inactive users
count_inactive = 0
for user in profiles:
    if user['isActive'] == False:
        count_inactive += 1
print(count_inactive)

#D
#Grand total of balances for all users
#crate a new empty list
balance_list = []
#loop through users
for user in profiles:
    #add balance amounts to new list after removing '$ and commas and converting to a float
    balance_list.append(float(user['balance'].replace('$', '').replace(',', '')))
#verify by printing the new list
print(balance_list)
#calculate the sum of the list items
print(sum(balance_list))
#grand total of balances = 52667.02

#E
#average balance per user
#same for loop as above to crate a list of float values then
print(sum(balance_list) / len(balance_list))
#avg balance = 2771.9484210526316

#F
#user with the lowest balance
print(min(balance_list))
#min balance = 1214.10
newlist = []
for user in profiles:
    if user['balance'] == '$1,214.10':
        newlist.append(user['name'])
        newlist.append(user['balance'])
print(newlist)


#G
#user with the highest balance
print(max(balance_list))
#max balance = 3919.64
newlist2 = []
for user in profiles:
    if user['balance'] == '$3,919.64':
        newlist2.append(user['name'])
        newlist2.append(user['balance'])
print(newlist2)


#H
#most common favorite fruit
#create a new list an add each users favorite fruit
fav_fruit = []
for user in profiles:
    fav_fruit.append(user['favoriteFruit'])
    #print new list to view/verify results
print(fav_fruit)
#use a list comprehension to count the favorite fruits
[[x, fav_fruit.count(x)] for x in set (fav_fruit)]


#returns [['strawberry', 9], ['banana', 6], ['apple', 4]]
def most_common_fav_fruit(fav_fruit):
    return max(set(fav_fruit), key = fav_fruit.count)
print(most_common_fav_fruit(fav_fruit))
#returns 'strawberry'

#I
#least common favorite fruit
def least_common_fav_fruit(fav_fruit):
    return min(set(fav_fruit), key = fav_fruit.count)
print(least_common_fav_fruit(fav_fruit))
#returns 'apple'

#J
#total number of unread messages for all users
#strt a count at 0
ur_messages = 0
#loop through the profiles
for user in profiles:
    #loop through the characters with the key 'greetings'
    for char in user['greeting']:
        #if the character is a digit
        if char.isdigit():
            #turn the character into an integer and add it to the count
            ur_messages += int(char)
#print the total
print(ur_messages)

    

