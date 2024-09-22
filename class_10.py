# Given the set my_set = {1, 2, 3, 3} and the set DaSet = {"Mango", "Banana", "Apple"}, perform the following operations:
# Add the elements of DaSet to my_set.
# Print the updated my_set

# my_set = {1, 2, 3, 3}
# DaSet = {"Mango", "Banana", "Apple"}
# my_set.update(DaSet)
# my_set = list(my_set)
# print(my_set)
# my_set= set(my_set)
# print(my_set)


my_dict2 = {'Mango': 10, 'Banana': 15, 'Apple': 25}
# new = {'jackfruit':190,
#        'Orange': 130
#        }
# my_dict2['Mango'] = 95
# my_dict2['blueberry'] = 87

# my_dict2.update(new)
# # print(my_dict2)

# # my_dict2.popitem()
# # my_dict2.pop('Mango')
# # del my_dict2['Banana']
# # print(my_dict2)

# # print(my_dict2.keys())
# # print(my_dict2.values())
# # print(my_dict2)

# # for key in my_dict2.keys():
# #     print(my_dict2[key])

# # for item in my_dict2.items():
# #     print(item[0],"==>", item[1])

# new_tup = {
#     (1,2) : "One-Two",
#     1 : [30,[1,2]]
# }
# # print(new_tup[(1,2)])
# my_dict2["Nested"] =  new_tup

# print(my_dict2['Nested'][1][1][1])
# Type checking
# print(type([1,2,3,4]))
# print(type((1,2,3,4)))
# print(type({1,2,3,4}))
# print(type(my_dict2))

# Type Casting
# x = 10.9
# y = int(x)
# print(y)

# x = 10
# y = float(x)
# print(y)


# Assignment

# 1. Given that,
# nested_dict = {
#     'Fruits': {'Apple': 10, 'Banana': 20},
#     'Vegetables': {'Carrot': 5, 'Broccoli': 8}
# }
# Access and print the quantity of Broccoli.
# Add a new vegetable Spinach with a quantity of 12 to the Vegetables key

nested_dict = {
    'Fruits': {'Apple': 10, 'Banana': 20},
    'Vegetables': {'Carrot': 5, 'Broccoli': 8}
}

print(nested_dict['Vegetables']['Broccoli'])
# nested_dict['Vegetables']['Spinach'] = 12
# nested_dict['Vegetables'].update({'Spinach':12})
print(nested_dict)

