# lst = [5,1,9,6,3]

# # print(sorted(lst,reverse=True))
# lst.sort()
# print(lst)

# import numpy as np
# lst = np.array([5,1,9,6,3])
# sorted_lst = np.sort(lst)
# print(sorted_lst)
# Bubble Sort


lst = [5,1,9,6,3]

# Ascending
# n = len(lst) # Size = 5
# for i in range(n):
#     for j in range(n-1):
#         if lst[j]>lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j] #Swaping
# print(lst)

# Descending
# n = len(lst) # Size = 5
# for i in range(n):
#     for j in range(n-1):
#         if lst[j]<lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j] #Swaping
# print(lst)


# Insertion Sort
# lst = [5,1,9,6,3]
# n = len(lst)
# for i in range(1,n):
#     key = lst[i]
#     j = i-1
#     while j>= 0 and key<lst[j]:
#         lst[j+1] = lst[j]
#         j = j - 1
#     lst[j+1] = key
# print(lst)

# Selection sort
# lst = [5,1,9,6,3]

# n = len(lst)
# for i in range(n):
#     minm = lst[i]
#     min_loc = i
#     for j in range(i,n):
#         if lst[j]<minm:
#             minm = lst[j]
#             min_loc = j
#     lst[i],lst[min_loc] = lst[min_loc] , lst[i]
# print(lst)
