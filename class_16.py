# Write a program to find the sum of digits of even integer in a given range.
# Ask the user for last number.

# Write a program to count the number of vowels in a given string using a for loop. 
# user_in = input("Enter Your word: ")
text = "bangla"

# start = 0
# while start< len(text):
#     print(text[start],end="")
#     start = start + 1

# text = "bangladesh"
# count = 0
# for i in range(len(text)):
#     if text[i] == "a" or text[i] == "e" or text[i] == "i" or text[i] == "o" or text[i] == "u":
#         count = count + 1
#         print("Found A vowel ==> ",text[i])
# print(count)

# text = input("Enter Your word: ")
# count = 0
# vowels = ['a','e','i','o','u']
# for i in range(len(text)):
#     if text[i] in vowels:
#         count = count + 1
#         print("Found A vowel ==> ",text[i])
# print(count)

# Write a program to count how many times a specific character appears in a string using a for loop.  
# text = input("Enter Your word: ")
# key = input("Enter Your character: ")
# count = 0
# for i in range(len(text)):
#     if text[i] == key:
#         count = count + 1
# print(count)

# Write a program to find and print all divisors of a given integer using a for loop.

# num = int(input("Enter Your Number: "))

# for i in range(1,num+1):
#     if num%i == 0:
#         print(i,end=",")
#     print(i)

# Write a program to find if a given number is perfect number or not.

# num = int(input("Enter Your Number: "))
# total = 0
# for i in range(1,num):
#     if num%i == 0:
#         total = total + i

# if total == num:
#     print("perfect Number")
# else:
#     print("Not a perfect Number")

# Write a program to find number of perfect numbers in a range

# num = int(input("Enter Your last number: ")) #10
# count = 0
# for var in range(1,num+1):
#     total = 0
#     for i in range(1,var):
#         if var%i == 0:
#             total = total + i
#     if total == var:
#         count = count + 1
#         print(var)
# print(count)