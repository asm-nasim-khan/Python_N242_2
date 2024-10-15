# Write a Python program that takes a word as 
# input and checks if it ends with a vowel (a, e, i, o, u) or Consonant

# vowels = ['a','e','i','o','u']
# # vowels = ['A','E','I','O','U']

# # text_vowels = 'aeiouAEIOU'

# user_inp = input('Enter a word: ')

# if user_inp[-1].lower() in vowels:
#     print('Ends With Vowels')
# else:
#     print('doest Ends With Vowels')


#   Write a Python program that takes the age of a person 
# as input and checks if they are eligible to vote. The voting age is 18 years or older.  

# age = int(input("Enter Your age: "))
# if age >= 18:
#     print('You are eligible to vote')
# else:
#     print('You are not eligible to vote')


# Take input the Age of the users,
# Print "Child" if the age is less than 18 years old.
# Print "Adult" if the age is greater or equal to 18 years old.
# Print "Old" if the age is greater than 65 years old.

# age = int(input("Enter Your age: "))
# if age<18:
#     print("Child")
# elif age>= 18 and age<= 65:
#     print('Adult')
# elif age>65:
#     print("Old")

# if age>65:
#     print("Old")
# elif age>= 18 :
#     print('Adult')
# else:
#     print("Child")

# Positive, Negative, or Zero: Write a Python program that takes 
# a number and checks if it's positive, negative, or zero.  

# num = int(input("Enter Your Number: "))
# if num == 0:
#     print("Zero")
# elif num < 0:
#     print("NEgative")
# elif num>0:
#     print("positive")


# n = int(input("Enter a number: "))
# n_2 = 0
# n_1 = 0
# for i in range(n):
#     if i == 0:
#         print(i,end=',')
#         n_2 = i
#     elif i == 1:
#         print(i,end=',')
#         n_1 = i
#     else:
#         temp = n_2
#         n_2 = n_1
#         n_1 = n_2 + temp
#         print(n_1,end=",")


# Factorial Calculation
# : Write a function that takes an integer n as input and returns the factorial of n. 
# The factorial of n is the product of all positive integers less than or equal to n.


# def Fact_n(num):
#     result = 1
#     if num == 0:
#         return 1
#     for i in range(1,num+1):
#         result = result * i
#     return result

# print(Fact_n(5))

#  Error Handling 

# print(20/0)

lst = (1,2)


# print(vowels)
# print(lst[3])

# try:
#     print("hello")
#     # print(vowels)
#     print(209/0)
# except AttributeError:
#     print("We Found an Error that AttributeError")
# except ZeroDivisionError:
#     print("We Found an Error that ZeroDivisionError")
# except NameError:
#     print("We Found an Error that NameError")

def my_divide(a,b):
    if b == -4:
        raise ZeroDivisionError("Division by -4 is not allowed!")
    print(a/b)

try:
    my_divide(20,-4)
except ZeroDivisionError as e:
    print('Found an error:',e)