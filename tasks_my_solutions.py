# The Complete Python Bootcamp From Zero to Hero course
# Teacher Jose Portilla
# Tasks from Statements section - my solutions
# link to the tasks: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/07-Statements%20Assessment%20Test.ipynb


# Exercise 1: Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

list1 = st.split()

for word in list1:
    if word[0].lower() == 's':
        print(word)


# Exercise 2: Use range() to print all the even numbers from 0 to 10.


even_list = []
for number in range(0,11):
    if number % 2 == 0:
        even_list.append(number)
print(even_list)


# Exercise 3: Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

div_by_3 = [x for x in range(0, 51) if x % 3 == 0]
print(div_by_3)


# Exercise 4: Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
word_list = st.split()

for x in word_list:
    if len(x)%2 == 0:
        print('even!')


# Exercise 5: Write a program that prints the integers from 1 to 100. But for multiples of three
# print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".


for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


# Exercise 6: Use List Comprehension to create a list of the first letters of every word
# in the string below:

st = 'Create a list of the first letters of every word in this string'
st_list = st.split()

letters = [word[0] for word in st_list]
print(letters)
