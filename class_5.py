# num = float(input("Enter A number: "))
# print(num)

# Data Types
# 1. String ---> ( Text )
# 2. integer ---> ( -infinity to +infinity)
# 3. float ---> ( Decimal Number)
# 4. booleann ---> ( True or False)
# ===================================
# list ---> (collection)
# set,tuple, dictoionary
# None / Null / null

# m = 1
# print(m is 1)

# if m:
#     print("True")
# else:
#     print("False")
# myVar  = "Happy"
# yourVar = 'Birthday'

# print("I'm happy")
line = 'I have read "Python For Everybody"'




# print(myVar[4])
# print(yourVar[4])
multiLine = ''' My name is Eshikhon,
                I love Python
'''

# print(multiLine)

# num = -2147483648
# num2 = 2147483647

# print(type(num))

# print(type(multiLine))

# f_num = 9999.334
# print(type(f_num))

# print(4<5)

line = 'I have Read "Python For Everybody"'

# print(line[8])
# print(line[5])
# print(line[6])
# word = line[7:19]
# print(line[0:19]) # 0,2,4,6,

# word = line[0:19:2]
# print(line)
# print(word)
# print("=============")
# print(line[0])
# print(line[2])
# print(line[4])
# print(line[6])


msg = "A paragraph could contain a series of brief examples or a single long illustration of a general point. It might describe a place, character, or process; narrate a series of events; compare or contrast two or more things; classify items into categories; or describe causes and effects."
print(msg[2:11])
print(msg.upper()) # Capitalize
print(msg.lower()) # Lower tha sentence

print(msg.endswith("paragraph"))
print(msg.startswith("A"))

print(msg.isalpha())
print(msg.isdigit())
print(msg.isdecimal())

# x = "5"
# print(x.isdecimal())
# msg = "A paragraph could contain a series of brief examples or a single long illustration of a general point. It might describe a place, character, or process; narrate a series of events; compare or contrast two or more things; classify items into categories; or describe causes and effects."

# def Eshikhon_startWith(text,msg):
#     return text[0] is msg

# print(Eshikhon_startWith(msg,"A paragraph"))


sentence_1 = "The quick brown fox jumps high."
sentence_2 = "A journey of a thousand miles."
sentence_3 = "Python coding is really fun!"
sentence_4 = "Success comes from hard work."
sentence_5 = "Always keep learning new things."
sentence_6 = "Reading books expands your mind."
sentence_7 = "Creativity requires imagination."
sentence_8 = "Consistency is key to progress."
sentence_9 = "Believe in yourself and succeed."
sentence_10 = "Failure is the key to success."


import random

# List of sentences
sentences = [
    sentence_1, sentence_2, sentence_3, sentence_4, sentence_5,
    sentence_6, sentence_7, sentence_8, sentence_9, sentence_10
]

# Function to get a random word from a sentence
def get_random_word(sentence):
    words = sentence.split()  # Split sentence into words
    return random.choice(words)  # Choose a random word

# Get random words from each sentence
# random_words = [get_random_word(sentence) for sentence in sentences]

# # Display the random words
# print(random_words) 




for items in sentences:
    print(items,end="")



