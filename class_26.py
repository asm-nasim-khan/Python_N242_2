# class Bird:
#     name = "Bird"
#     def print_name(self):
        
#         print(self.name,self)
    
#     def flight(self):
#         print(self.name,"is Flying.")

# class Cuckoo(Bird):

#     def flight(self):
#         print(self.name,"is Flying happily.")

# Cuckoo_1 = Cuckoo()
# Cuckoo_1.flight()
# Cuckoo_1.name = "Pakhi"
# Cuckoo_1.print_name()
# print(Cuckoo_1)

# Cuckoo_2 = Cuckoo()
# Cuckoo_2.name = "Pakhi_2"
# Cuckoo_2.print_name()


# Abstraction
from abc import ABC, abstractmethod
# class Bird(ABC):
#     @abstractmethod
#     def flight(self):
#         pass

#     @abstractmethod
#     def sound(self):
#         pass

# class Cuckoo(Bird):
#     def print_name(self):
#         print('hello')
    
#     def flight(self):
#         pass

#     def sound(self):
#         pass

# #Driver Class
# cuckoo_1 = Cuckoo()

# class Car(ABC):
#     @abstractmethod
#     def window(self):
#         pass
    
#     @abstractmethod
#     def seats(self):
#         pass

# class Toyota(Car):
#     def window(self):
#         print("This Card has 4 windows")
    
#     def seats(self):
#         print("This Card has 4 seats")


# mycar = Toyota()
# mycar.seats()


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


# Encapsulation
class Cuckoo():
    def __init__(self,name_1,eyes_1): # Constructor
        print("Look A new bird is born.")
        self.name = name_1
        self.__eyes = eyes_1
    
    def get_eyes(self):
        print(self.__eyes)

    def set_eyes(self,eyes):
        self.__eyes = eyes

    def flight(self):
        print("Look I'm Flying.")


#Driver Code
Cuckoo_1 = Cuckoo("Pakhi",2)
Cuckoo_1.set_eyes(1) #setter method
Cuckoo_1.get_eyes()  #Getter Method
# Cuckoo_2 = Cuckoo()
