### Function Exercises ###

##1##
#this function accepts one input
#and returns true if it is the number 2 or the string 2 and returns false if it is not
def is_two(n):
    #the if statement checks the argument against the values in the () 
    #and returns true if there is a match
    if n in (2, '2', 'two'):
        return True
    #otherwise it returns false
    else:
        return False

#test arguments for the function#
is_two(2)
is_two('2')
is_two(5)
is_two('twenty')
is_two('two')


##2##
#this function accepts a string character
#and returns true if it is a vowel and false if it is not
def is_vowel(char):
    #the if statement checks the argument character against the characters in 'aeiouAEIOU' 
    #and if there is a match it returns true
    if char in 'aeiouAEIOU':
        return True
    #otherwise it returns false
    else:
        return False

#test arguments for the function#
is_vowel('a')
is_vowel('b')


##3##
#this function accepts a string character 
#and returns true if it is a consonant or false if it is not
def is_consonant(char):
    #the function for finding a vowel from the above exercise is used to check the argument first 
    #and false is returned if there is a match
    if is_vowel(char):
        return False
    #otherwise true is returned
    else:
        return True

#test arguments for the function#
is_consonant('a')
is_consonant('b')
is_consonant('c')


##4##
#this function accepts a string that is a word 
#and capitalizes the first letter of the word if it starts with a consonant
def is_a_word(string):
    #the if statement uses the 'is_consonant' function from the previous exercise 
    #and uses it to check if the first letter in the argumnet is a consonant using the character index of the first letter
    if is_consonant(string [0]):
        #if the first letter is a consonant
        #it returns the argument with the first letter capitalized using the capitalize() function
        return string.capitalize()
        #if the first letter is not a consonant
        #it returns the argument string as entered
    else: 
        return string

#test arguments for the function#
is_a_word('word')
is_a_word('and')


##5##
#this function accepts a tip percentage as a number between 0 and 1
#then calculates the value of the tip based on the argument values
def calculate_tip(tip_percent, bill_amount):
    return bill_amount * tip_percent

#test arguments for the function#
calculate_tip(.2, 100)
calculate_tip(.12, 100)


##6##
#this function accepts an original price and a discount percentage as a number between 0 and 1
#and returns the price of the item after the discount has been applied
def apply_discount(original_price, discount_percentage):
    #the return statement first calculates the amount of the total price that will be discounted 
    #then subtracts that amount from the original price
    return original_price - (original_price * discount_percentage)

#test arguments for the function#
apply_discount(100, .2)
apply_discount(100, .45)


##7##
#this function accepts a string that is a number and has commas and returns an integer
def handle_commas(strnum):
    #the return statement first removes (replaces with nothing) any commas
    #then turns the string into an integer and returns the result
    return int(strnum.replace(',', ''))

#test arguments for the function#
handle_commas('1,000,000')
#the below type function will return the data type for the result of the function to verify it has changed to an integer
type(handle_commas('1,000,000'))


##8##
#this function accepts a number grade and returns a letter grade
def get_letter_grade(num_grade):
    #the if statement checks the entered argument (number grade) against the different number ranges
    #and returns the associated string value when it finds a match
    if num_grade in range(90, 101):
        return 'A'
    elif num_grade in range(80, 90):
        return 'B'
    elif num_grade in range(70, 80):
        return 'C'
    elif num_grade in range(60, 70):
        return 'D'
    else:
        return 'F'

#test arguments for the function#
get_letter_grade(80)
get_letter_grade(90)
get_letter_grade(43)
get_letter_grade(93)


##9##
#this function accepts a string and returns the string without any vowels
def remove_vowels(str):
    #the loop goes through each character in the argument string and compares it to each character in 'aeiouAEIOU' 
    #and if there is a match it removes (replaces it with nothing) the character in the reassigned value of 'str'
    for char in 'aeiouAEIOU':
        str = str.replace(char, '')
    #the return statement returns the reassigned value of 'str'
    return str

#test arguments for the function#
remove_vowels('was')
remove_vowels('banana')
remove_vowels('aeious')


##10##
#this function accepts a string and returns a valid python identifier
def normalize_name(name):
    #the loop goes through the input argument character by character
    #and removes (replaces with nothing) any character that is not alphanumeric and is not a space or underscore
    for char in name:
        if not char.isalnum() and char not in (' ', '_'):
            name = name.replace(char, '')
    #the return statement takes the results from the loop
    #and makes all characters lower case,
    #removes any white spaces at either end of the argument,
    #replaces any spaces with an underscore, and returns the result
    return name.lower().strip().replace(' ', '_')

#test arguments for the function#
normalize_name('  Nathan Sharick%  ')
normalize_name('Nathan_Sharick')


##11##
#the cumulative_sum function returns a list that is the cumulative sum of the numbers in the input list
def cumulative_sum(numlist):
    #first createa new emptly list to add values to
    cumsum_list = []
    #than create a variable to work with that has a starting value of 0.
    n = 0
    #this loop will go through each value in the passed argument list 
    # and reassign the value of 'n' as the previous value of 'n' + the next argument value 
    # and print each reassigned value of 'n' in the empty list we created.
    for num in range(0, len(numlist)):
        n += numlist[num]
        cumsum_list.append(n)
    #last we will return the contents of the new list we created.
    return cumsum_list

#test arguments for the function#
cumulative_sum([1, 2, 3])
cumulative_sum([1, 2, 3, 4, 5])

##Bonus Exercises##

#1a
#this funciton takes in a 12 hour format time with am/pm
#and returns the time in a 24hour format
def twelveto24(time):
    #the first if statement checks if the input is 'am'
    #and if the hour of the time is '12'
    #if it is true it will change the '12' to '00' for the 24 hour format
    if time[-2:] == 'am' and time[:2] == '12':
        return '00' + time[2:-2]
        #the first elif statement removes the 'am'
    elif time[-2:] == 'am':
        return time [:-2]
        #the second elif statement checks for 'pm' 
        #and if the first two elements are 12
    elif time[-2:] == 'pm' and time[:2] == '12':
        return time[:-2]
        #the else statement adds the 12 hours to the pm time
        #and returns the time without the 'pm'
    else:
        return str(int(time[:2]) + 12) + time[2:5]

#test arguments
print(twelveto24('08:05 pm'))
print(twelveto24('08:05 am'))
print(twelveto24('12:05 pm'))
print(twelveto24('12:05 am'))

#1a extra bonus#
#import the time library
import time
#create a variable to hold the 24 hour time value
time24 = '13:00'
#create a translateable variable using time functions that represents the 24 hour time value
#striptime() parses the entered time value according to the format indicators 
#(in this case %H for hour using the 24 hour clock, :, and %M for minutes)
t = time.strptime(time24, "%H:%M")
#create a variable that parses the above created variable acording to the format indicators and returns it as a string
#(in this case %I for hour on a 12 hour clock, :, %M for minutes, and %p for either am or pm based on the give time value)
time12 = time.strftime( "%I:%M %p", t)
#print the created 12  hour clock time created
print(time12)



