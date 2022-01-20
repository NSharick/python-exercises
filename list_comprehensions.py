#list comprehension practice

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

numbers_plus_one = [number + 1 for number in numbers]

output = []
for fruit in fruits:
    output.append(fruit.upper())

#1
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)

#2
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

#3
def countvowels(string):
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count = count+1
    return count

fruits_with_more_than_two_vowels = [x for x in fruits if countvowels(x) > 2]
print(fruits_with_more_than_two_vowels)

#4
fruits_with_exactly_two_vowels = [x for x in fruits if countvowels(x) == 2]
print(fruits_with_exactly_two_vowels)

#5
fruit_w_more_than_5_char = [fruit for fruit in fruits if len(fruit) > 5]
print(fruit_w_more_than_5_char)

#6
fruit_w_5_char = [fruit for fruit in fruits if len(fruit) == 5]
print(fruit_w_5_char)

#7
fruit_w_less_than_5_char = [fruit for fruit in fruits if len(fruit) < 5]
print(fruit_w_less_than_5_char)

#8
fruit_length = [len(fruit) for fruit in fruits]
print(fruit_length)

#9
fruit_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruit_with_letter_a)

#10
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

#11
odd_numbers = [number for number in numbers if number % 2 !=0]
print(odd_numbers)

#12
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

#13
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)

#14
two_or_more_numerals = [number for number in numbers if number > 9]
print(two_or_more_numerals)

#15
numbers_squared = [number * number for number in numbers]
print(numbers_squared)

#16
odd_negative_numbers = [number for number in numbers if number < 0 and number % 2 != 0]
print(odd_negative_numbers)

#17
numbers_plus_five = [number + 5 for number in numbers]
print(numbers_plus_five)