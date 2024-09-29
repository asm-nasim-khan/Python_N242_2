# num = 1
# total = 0
# while num<=5:
#     # print(num)
#     total = total + num
#     print(num,end=" ")
#     if num == 3:
#         break
#         print("Hola")
#     num = num + 1
# print("Total:",total)

# count = 0
# while True:
#     count+=1
#     print(count)
#     print("Desh")
#     break


# while True:
#     user = input("Enter your Number or enter exit to stop: ")
#     if user == "exit":
#         break
#     else:
#         user = int(user)
#         if user%2 == 0:
#             print("Even")
#         else:
#             print("odd")

# num = 1
# total = 1
# end = int(input("Enter the factorial numb: "))
# while num<=end:
#     total = total * num
#     num = num + 1
# print("Total:",total)

# Tracing


quantity = 8
price = 120

while quantity<=12:
    total = quantity * price
    discount = 0
    if quantity > 10:
        discount_rate = 0.1 
        discount = total * discount_rate
    total =  total - discount
    quantity = quantity + 1
    print("Total cost:", total)