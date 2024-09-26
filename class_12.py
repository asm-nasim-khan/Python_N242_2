# # Nested if else
# num_1 = int(input('Enter a Number: '))
# num_2 = int(input('Enter another Number: '))
# num_3 = int(input('Arekta please: '))

# if num_1>num_2:
#     # Num1 is Greater than num 2
#     if num_1>num_3:
#         print("Num_1 Is Largest")
#     else:
#         print("Num_3 Is Largest")
# else:
#     # Num2 is Greater than num 1
#     if num_2>num_3:
#         print("Num_2 Is Largest")
#     else:
#         print("Num_3 Is Largest")


# x = 6

# if x>4:
#     print("hello")

# num = 43


# if num%2 == 0:
#     print("Even")
# else:
#     print("odd")

# if num%2 == 1:
#     print("Odd")
# else:
#     print("Even")

# print(102 * (20/100))

# Leap Year

# year = 2024

# 1. Divisible By 4
# 2. Divisible By 100

# 1. Divisible By 400

# if year%400 == 0:
#     print('Leap Year')
# elif year%4 == 0:
#     if year%100 != 0:
#         print('Leap Year')
#     else:
#         print("Not Leap year")
# else:
#     print("Not Leap year")
# print("done")

# if year%400 == 0:
#     print('Leap Year')
# elif year%4 == 0 and  year%100 != 0:
#     print('Leap Year')
# else:
#     print("Not Leap year")
# print("done")
# =========================================================
# if year%400 == 0 or (year%4 == 0 and  year%100 != 0):
#     print('Leap Year')
# else:
#     print("Not Leap year")
# print("done")


# print(False or True)
# print(False and False)
# False = 0
# True = 1
# and = *
# or = +
# print(1 * 0)
# print(0 + 1)

num = 23
# if num%2 == 1:
#     print("Odd")
# else:
#     print("Even")


# result = "Even" if num%2 == 0 else "Odd"
# print(result)



# user_number =int(input("entre a number:"))

# if user_number>0:
#     print("positive")
# else:
#     if user_number == 0:
#         print('Zero')
#     else:
#         print("negative")

# result = "positive" if user_number > 0 else "Zero" if user_number == 0 else "Negative"
# print(result)

year = 2000
if year%400 == 0 or (year%4 == 0 and  year%100 != 0):
    print('Leap Year')
else:
    print("Not Leap year")
print("done")