# While

# i = 0  # Start
# n = 6 # end
# #Increament = 1

# iter = 1
# while iter<=5:
#     print(iter)
#     iter+=1 

# n = int(input("How mane times: "))
# start = 0
# while start<n:
#     year = int(input("Enter A year: "))
#     if year%400 == 0 or (year%4 == 0 and  year%100 != 0):
#         print('Leap Year')
#     else:
#         print("Not Leap year")
#     start = start + 1 #increament


# Take a number From user and print all the even number upto that number
# n = int(input("Enter the last number: ")) # 10
# start = 1
# while start<=n:
#     if start%2 == 1:
#         print(start)
#     start = start + 1

# 2,4,8,16,32,64,128,512 Print the series
# start = 1
# stop = 9
# while start<=stop:
#     print(2**start,end=",")
#     start = start + 1



# Assignemnt From Previous Class

# Problem 4: Day of the Week
# Write a program that takes a number between 1 and 7 as input and prints:
# "Monday" for 1,
# "Tuesday" for 2,
# "Wednesday" for 3,
# "Thursday" for 4,
# "Friday" for 5,
# "Saturday" for 6,
# "Sunday" for 7.
# Hints: Use Dictionary

day = int(input("Enter a number between 1 - 7: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")

weeks = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
print(weeks[day])
