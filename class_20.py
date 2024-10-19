# file = open('input.txt','r').read()
# # print(type(file))
# lines = file.split("\n") # Line break down
# # print(lines)
# output_file = open('students.txt','w')
# for items in lines:
#     lst = items.split('\t')
#     # print(lst)
#     output_file.write(lst[0]+" "+lst[1].upper()+"\n")
#     # print(lst[0],lst[1].lower())
# output_file.close()

# # print("Hello\nI am \neshikhon")

# file = open('output.txt','w') # Over write

# file = open('output.txt','a') # Append
# file.write("I love Python.")
# file.close()
import myFunctions

myFunctions.isprime(12)
print(myFunctions.Greetings("nasim"))