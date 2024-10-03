# For Loop

# print 1 to 5

# start = 1
# while start <= 5:
#     print(start)
#     start = start + 1

for start in range(6):
    print(start)

# print(range(1,10,2))

# for start in range(2,8):
#     print("Hello",start)

end = int(input("Enter the last number: "))
total = 0
for num in range(1,end+1):
    total = total + num
print(total)

# Take a number From user and print all the even number upto that number
# n = int(input("Enter the last number: ")) # 10
# start = 1
# while start<=n:
#     if start%2 == 1:
#         print(start)
#     start = start + 1

# *
# **
# ***
# ****
# *****
msg = "BANGLADESH"
for start in range(len(msg)):
    for j in range(start+1):
        print(msg[j],end="")
    print()

    
