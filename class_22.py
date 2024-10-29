# def LOOP(i):
#     #base condition
#     if i == 6:
#         return 0
#     LOOP(i+1)
#     print(i)
#     print('Good')

# LOOP(1)



# def my_sum(a,b,c):
#     b = b + c
#     a = b + 3
#     print(a,b)

# x = lambda a,b,c : a*(b+c)

# print(x(3,6,4)+5)

x = 6
# if x %2 == 0:
#     print("even")
# else:
#     print("odd")

# . Introduction to Comprehension


# result = "Even" if x%2 == 0 else "odd"
# lst = []

# for i in range(1,20):
#     if i%2==0:
#         lst.append('Even')
#     else:
#         lst.append('odd')

# lst = ["Even" if i%2==0 else "Odd" for i in range(1,20)]
# print(lst)

# Dictionary
# dict_1 = {
#     "key_1" : "value_1",
#     "key_2" : "value_2",
# }

keys = [1,2,3,4,5]
values = ['One','Two','Three','Four',"Five"]

myDict = {k:v for (k,v) in zip(keys,values)}
print(myDict)

# nums = [1,2,3,4,5]

# myDict = {k:k**2 for k in nums}
# print(myDict)

# lst = [i for i in range(1,101,5)]
# print(lst)