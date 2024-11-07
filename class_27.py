# from abc import ABC, abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def deposite_money(self,amount):
#         pass

#     @abstractmethod
#     def withdraw_money(self,amount):
#         pass

# class Eshikhon_Bank_LTD(Bank):
#     balance = 0
#     def my_balance(self):
#         print("You have",self.balance," Taka.")

    
#     def deposite_money(self,amount):
#         self.balance = self.balance + amount
#         print(amount," taka deposited.")

#     def withdraw_money(self,amount):
#         if self.balance > amount:
#             self.balance = self.balance - amount
#             print(amount," taka withdrawn.")
#         else:
#             print("insufficient Amount.")


# #Driver Class
# print("============ 1 ==============")
# user_1 = Eshikhon_Bank_LTD()  
# user_1.deposite_money(10000) # 10000 taka deposited.
# user_1.withdraw_money(5000) # # 5000 taka withdrawn.
# user_1.my_balance() # You have 5000 taka.
# print("============ 2 ==============")
# user_2 = Eshikhon_Bank_LTD()
# user_2.deposite_money(10000) # 10000 taka deposited.
# user_2.withdraw_money(15000) # insufficient Amount.
# user_2.my_balance() # You have 10000 taka.
# print("============ 3 ==============")


# from abc import ABC, abstractmethod

# class Library(ABC):
#     @abstractmethod
#     def borrow_book(self, book_title):
#         pass
    
#     @abstractmethod
#     def return_book(self, book_title):
#         pass

# class CityLibrary(Library):
#     def __init__(self):
#         self.borrowed_books = []

#     def borrow_book(self, book_title):
#         self.borrowed_books.append(book_title)
#         print(f"'{book_title}' has been borrowed.")

#     def return_book(self, book_title):
#         if book_title in self.borrowed_books:
#             self.borrowed_books.remove(book_title)
#             print(f"'{book_title}' has been returned.")
#         else:
#             print(f"'{book_title}' was not borrowed.")

#     def list_books(self):
#         print("Currently borrowed books:", self.borrowed_books)

# # Driver Code
# print("==== Scenario 1 ====")
# user_1 = CityLibrary()
# user_1.borrow_book("The Great Gatsby")
# user_1.borrow_book("1984")
# user_1.list_books()
# user_1.return_book("1984")
# user_1.list_books()

# print("==== Scenario 2 ====")
# user_2 = CityLibrary()
# user_2.borrow_book("Moby Dick")
# user_2.return_book("To Kill a Mockingbird")
# user_2.list_books()


# from abc import ABC, abstractmethod

# class ElectricityTracker(ABC):
#     @abstractmethod
#     def record_usage(self, amount):
#         pass
    
#     @abstractmethod
#     def reduce_usage(self, amount):
#         pass

# class HomeElectricity(ElectricityTracker):
#     def __init__(self):
#         self.total_usage = 0

#     def record_usage(self, amount):
#         self.total_usage += amount
#         print(f"{amount} kWh added to usage.")

#     def reduce_usage(self, amount):
#         if self.total_usage >= amount:
#             self.total_usage -= amount
#             print(f"{amount} kWh reduced from usage.")
#         else:
#             print("Not enough usage to reduce.")

#     def current_usage(self):
#         print("Current usage:", self.total_usage, "kWh")

# # Driver Code
# print("==== Scenario 1 ====")
# user_1 = HomeElectricity()
# user_1.record_usage(200)
# user_1.record_usage(150)
# user_1.current_usage()
# user_1.reduce_usage(100)
# user_1.current_usage()

# print("==== Scenario 2 ====")
# user_2 = HomeElectricity()
# user_2.record_usage(300)
# user_2.reduce_usage(400)
# user_2.current_usage()



class Shape():
    def __init__(self,name,area):
        self.area = area
        self.name = name

    def __str__(self):
        return "this is a "+ self.name
    
    def __add__(self,other):
        return Shape("House",self.area + other.area)
    

rectangle = Shape("Rectangle",4)
triangle = Shape("Triangle",2)

house = rectangle + triangle # Problem 1
print(rectangle) # Problem 2
print(house.area)

