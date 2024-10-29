# import datetime

# print(datetime.time.hour())

import json

import json

# x = '{"name" : "Nasim", "age":99} '

# # type(x)
# y = json.loads(x)

# print(y['age'])

# myDict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# my_json = json.dumps(myDict)

# print(my_json)


import re

# txt = "I Love 123 Python 12234 its Easy 3334"

# # result = re.findall("\D",txt)

# # if result:
# #     print("No digit")
# # else:
# #     print("Digit ache")

# # result = re.split("\d",txt)
# # print(result)

# # res = re.sub("[0-9]","*",txt,10)
# res = re.sub("[A-Z]","*",txt,10)

# print(res)


re_exp = "[a-z]+[0-9]*@[a-z]+.[a-z]+" # email
email = "nasim123@gmail.com"

print(re.search(re_exp,email))