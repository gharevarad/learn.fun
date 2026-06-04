# printing an even and odd numbers in python programs

"""num = int(input("print an number you wanted : "))
if num % 2 == 0:
    print(num ,"number is a even number ")
else:
    print(num ,"this is an odd number") """    
    
#  printing an reverse of an number and printing an number is an palindrome or not ??


"""while True:
    try:
        num = int(input("enter positive integer numbers : "))
        reverse = 0
        orignal_num = num

        while num > 0 :
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10
        
        if reverse == orignal_num :    
            print("the given number is an palindrome number ", reverse)
        else :
            print("the given number is not an palindrome number ", reverse)
            
        break

    except ValueError:  
        print("please give an positive integer input ")"""
        
        
        
  # take 3 numbers and print an largest number among the 3 number
        
        
"""num1 = int(input("enter a first number : "))
num2 = int(input("enter a second number : "))
num3 = int(input("enter a third number : "))

if num1 > num2 and num1 > num3 :
    print("first number is the greatest number ")
elif num2 > num1 and num2 > num3 :
    print("second number  is the greatest number ")
else :
    print("third number is the greatest number ")"""


#  Print the multiplication table of a given number


"""num = int(input("enter a number to print table : "))
i = 1
while i <= 10 :
    multiplication = num * i
    print(num," * ",i ," = ", multiplication)
    i += 1
"""


# print the total count of an number user input 12344 and output  5 :


"""num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10      # get last digit
    total = total + digit
    num = num // 10       # remove last digit

print("Sum of digits:", total)"""


# printing an factorial of the number 


"""num = int(input("enter an number of which factorial you want to print : "))

fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)"""


# print wether the number is an prime or not


"""num = int(input("enter an number  : "))

for i in range(2,num):
    if num % i == 0:
        print("number is not an prime numeber ")
        break
else :
    print("number is an prime number")"""
    
    
    
# printing an prime number in an efficient way and prints a numbers from 0 to userinput number 


"""num = int(input("enter a number : "))

for i in range(2,num+1):
    is_Prime = True
    
    for j in range(2,int(i ** 0.5)+1):
        if i % j == 0 :
            is_Prime = False
            break
        
    if is_Prime :
        print(i)"""
        
        
        
# printing an fibonacci series


"""num = int(input("enter a number : "))
v1 = 0
v2 = 1
print(v1)
print(v2)
for i in range(num+1):
    
    Re = v1 + v2
    print(Re)
    v1 = v2
    v2 = Re"""
    
    
# printing an pattern 
                      

"""for i in range(1,6):
    for j in range(i):
        print("*",end = "")
    print()"""    
    
    
"""for i in range(5,0,-1):
    for j in range(i):
        print("*",end = "")
    print()"""
    
    
"""n = 5

for i in range( 1 , n + 1 ):
    # printing spaces
    for j in range(n-i):
        print(" ",end = "")
        
    for z in range (2*i-1):
        print("*", end = "")
        
    print()"""
    
# printing an dimand shape with stars

"""n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
        

m = 4
for j in range(4,0,-1 ):
    print(" " *(5 -j) + "*" * (2*j-1))"""
    
    
# printing an rectangle with spaces inside

"""n = 5
m = 6
for i in range(1,n+1):
    for j in range(1,m+1):
        if i == 1 or j == 1 or j == m or i == n :
            print("*", end = "")
        else :
            print(" ",end = "")
            
            
    print()"""
    
    
# creating an function and calling the function

"""num1 = int(input("enter an number : "))
num2 = int(input("enter an number : "))

def addition(num1,num2):
    return num1 + num2
    
def subtraction(num1,num2):
    return num1 - num2
    
def multiplication(num1,num2):
    return num1 * num2
    
def division(num1,num2):
    return num1 / num2 

print("numtiplication" , multiplication(num1,num2))
print("addition" , addition(num1,num2))
print("subtraction" , subtraction(num1,num2))
print("division" , division(num1,num2))"""

    
# creating an simple calculator without an user interface

"""num1 = int(input("enter an number : "))
num2 = int(input("enter an number : "))
operator = input("enter an operator like + , - , * , / : ")

def check_operator(num1,num2,operator):
    if operator == "+" :
        return num1 + num2
    
    if operator == "-" :
        return num1 - num2
    
    if operator == "*":
        return num1 * num2
    
    if operator == "/":
        if num2 == 0 :
            return ("cant divide by zero")
        return num1 / num2 

result = check_operator(num1,num2,operator)
print(result)"""
              

# starting an oops concept 
# creating an class object and constructor and methods inside it 


"""class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def age(self,age):
        if age < 0 :
            print("invalid age you mentioned sir")
            
    def name(self,name):
        print("you age welcome :",name)
        

    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)
        
        
s1 = Student("varad",21)
s2 = Student("rohan",24)

s1.display()
s2.display()

s1.name()
s2.age()

print(type(s1))
print(type(s2))
print(type(Student))"""

#Create a Car Class Attributes: brand, model, price and give some discount on the price of cars

"""class Car:
    def __init__(self,brand, model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def discount(self):
        after_discount = self.price - (self.price * 0.05)
        return after_discount
        
    def display(self):
        print("the brand of your car is :", self.brand)
        print("the model of the car is :",self.model)
        print("the price of the car is :",self.price)
        
s1 = Car("mercedes","m2",150000)
s2 = Car("audi","m4",120000)

s1.display()
print("price after discount : ",s1.discount())
s2.display()

print("price after discount : ",s2.discount())"""


# polymorphysm practice questions

"""class Animal:
    def animalSound(self):
        pass 
    
class dog(Animal):
    def animalSound(self):
        return "dog is barking"
    
class cat(Animal):
    def animalSound(self):
        return "meow"
    
class goat(Animal):
    def animalSound(self):
        return "maaeey"

animals = [dog(),cat(),goat()]    
for animal in animals :
    print(animal.animalSound())"""
    
    
# polymorphysm practice codes


"""class Calculator():
    def calculate(self,a,b):
        pass


class Add(Calculator):
    def calculate (self,a,b):
        return a + b
    
class Subtract(Calculator):
    def calculate (self,a,b):
        return a - b

class Multiplication(Calculator):
    def calculate(self,a,b):
        return a * b
    
class division(Calculator):
    def calculate(self,a,b):
        return a / b
    
calcu = [Add(),Subtract(),Multiplication(),division()]

cal = Calculator()

obj_add = Subtract()
print(obj_add.calculate(12,34))"""        


# learning an inheritance and incapsulation and getter and setter

"""class Car:
    
    def __init__(self,brand,model):
        self.__brand = brand  # it is a private variable now it cant be accessed in another class
        self.model = model
        
    def get_brand(self):
        return self.__brand
        
        
        
    def fullName(self):
        return f"my car brand is {self.brand} and its model is {self.model}"
        
        
class ElectricCar(Car):
    def __init__(self,batteryLife,brand,model):
        self.batteryLife = batteryLife
        super().__init__(brand,model)
        
electricCar = ElectricCar("tesla","tesla S","10KWH")
print(electricCar.brand,electricCar.model,electricCar.batteryLife)"""
        
                
"""myCar = Car("Toyota","Corola")
print(myCar.brand)
print(myCar.model)

otherCar = Car("Mercedes","Mercedes Gwagon")
print(otherCar.brand,otherCar.model)

print(otherCar.fullName())"""


# learning an polymorphysm

"""class Car:
    
    def __init__(self,fule_Type):
        self.fule_Type = fule_Type
        
    def fule_Types(self):
        print("petrol or desile")
        
class electric_Car(Car):
    
    def __init__(self,fule_Type):
        super().__init__(fule_Type)
        
    def fule_Types(self):
        print("Electricity")
        
        
c1 = Car()
print(c1.fule_Types())

c2 = electric_Car()
print(c2.fule_Types())"""


# string index slicing and encoding

"""name = "Varad"
print(f"here is a string : {name[::4]}")

name = "Robin"
print(f"here  string : {name}")"""

# tuples in python

"""masala_spices = ("cardimum","clove","cinimom")
#masala_spices[0] = "haldi" this cannot be modified because it is immutable
print(masala_spices[1])"""

# list in python

"""incredients = ["water" ,"milk","tea",]
incredients.insert(7 ,"lemon",)
incredients.extend(["varad","ghare","bharat"])
print(len(incredients)) 
print(incredients.pop()) """

# advance data type and we learn here a zip wich is used in loops

"""datetime,time,calander,timedelta
"""

"""vegetables = ("tamato","patato","collyflower","brokely","ladyfinger")
amount = (34,57,74,56)
for vegi,amount in zip(vegetables,amount) :
    print(f"this is {vegi} is worth of rupees {amount}")"""


# using an walrus operator:=   
    
"""if (num := int(input("enter a number you want to print :"))) <= 10 :
    print (f"this number {num} is less then 10 ")
else :
    print("number is greater then 10")"""
    

"""def fetch_Sales():
    print("fetch the sales data... ")
    
    
def filter_valid_sales():
    print("filtering an valid sales data... ")"""
    

# functions

"""num1 = int(input("enter a number to check even or odd :")) 
num2   = int(input("enter a number to check even or odd :"))  
    
def Addition(num1,num2):
    results = num1 + num2 
        
        
result = Addition(num1,num2)
print(result)"""


# local and global variable function

"""x = 10

def channge_variable():
    global x 
    x = 20
    print(x)
    
channge_variable()

print(x)"""

# comprehension in dictonary
"""original = {"a": 1, "b": 2}

swapped = {v: k for k, v in original.items()}
print(swapped"""

# comprehension using an even odd 

"""dict = {x : ("even" if x % 2 == 0 else "odd")for x in range (30)}
print(dict)"""

"""def car_Models():
    yield "mercedese"
    yield "fortuner"
    yield "tata safari"
    yield "bmw"
    
car = car_Models()

print(next(car))
print(car)"""



"""def first_generator():
    yield "here we start our first generator "
    yield "here we finished our first generator "
    
def second_generator():
    yield "Start : "
    yield from first_generator()  # here we are calling an first generator
    yield "stop :"
    
gen = second_generator()

for value in gen:
    print(value)"""
    
# this is an example of the decorators in python
    
"""def decorating(funct):
    def wrapping():
        print("starting :")
        funct()
        print("Ending :")
        
    return wrapping()
        
        
@decorating
def greeting():
    print("hello baccho")
    
greeting()"""

# so here we used argument and kw means key word argument means distionary arguments 

"""import time

def logging(func):
    def wrapping(*args,**kwargs):
        print(f"here the functions starts : {func.__name__}")
        print(f"Arguments : {args},{kwargs}")
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"returned :{result} {end-start:.4f} seconds")
        return result
        
    return wrapping


@logging
def addition(a,b,c,name,age):
    print(name,age)
    return a+b*c

add = addition(12,34,2,name = "varad",age = 25)"""


"""class Test:
    def show(self):   # missing self
        print("Hello")

t = Test()
t.show() """

#Create class Animal with method sound().
#Override it in Dog and Cat.

"""class Animal:
    def sound(self):
        return "animals just sound crazy"
    
class dog(Animal):
    def sound(self):
        return "dog barks" 
    
class  cat(Animal):
    def sound(self):
        super()
        return "cat meyooo "
    
c = cat()
print(c.sound())"""

# file handling programs

"""try:
    with open("file.txt","w") as f :
     f.write("here my file is being created")
    with open("file.txt","r") as f:
        print(f.read())
    f.close()
except FileNotFoundError:
    print("file not found! ")
finally:
    print("program is executed ")  """
    
# it creates the file externaly
    
"""file = open("order.txt","w")
try:
    file.write("here my first file")
finally:
    file.close()"""
    
"""with open("writter.txt","w") as file:
    file.write("aur bete aagaya swadh....")"""
    
    
# concurrency and parallelism 
# here we cover threading.thread ,asyncio,multiprocessing.process 
# and concurrent.future.process.pool.execution

"""import threading
import time

def order():
    for i in range(1,4):
        print(f"taking order for #{i}")
        time.sleep(3)
        
def masala_chai():
    for i in range(1,4):
        print(f"making chai of #{i}")
        time.sleep(4)
        
# creating an thread
order_thread = threading.Thread(target = order)
masala_thread = threading.Thread(target = masala_chai)

order_thread.start()
masala_thread.start()     

order_thread.join()  
masala_thread.join()

print("aaj ki majduri khatam bc.....")"""

# multiprocessing using Pool.processing

"""from multiprocessing import Pool
import time

#inp = int(input("enter a number :"))

def task(n):
    return n*n

if __name__ == "__main__":
    with Pool(7) as p:
        result = p.map(task,{2,4,6})
        
    print(result)"""
        
    
"""def welcome():
    print("hey hello and welcome dostoon.....")
    
print(__name__)
    
if __name__ == "__main__":
    welcome()"""


"""import threading 
import time

def chai():
    print(f"{threading.current_thread().name} Started...")
    count = 0
    for _ in range(100_00_000):
        count += 1
    print(f"{threading.current_thread().name} End...")
    
thread1 = threading.Thread(target = chai,name = "barista")
thread2 = threading.Thread(target = chai,name = "barista")

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()
     
end = time.time()

print(f"total time taken : {end - start:.2f} seconds")"""

        
"""import asyncio

async def brew(name):
    print(f"brewing {name}...")
    await asyncio.sleep(3)
    print(f" {name} is ready...")
    
async def main():
    await asyncio.gather(
        brew("masala chai"),
        brew("tulsi ginger tea"),
        brew("narial chai")
    )
 
asyncio.run(main())"""


"""import time
import asyncio

async def task(name,game):
    
    print(f"{name}  Start")
    await asyncio.sleep(3)   # waits 3 seconds
    print(f"{game}  end")
    
     
async def main():
    await asyncio.gather(
        task("samaj gaya main  ","khatam bc"),
        task("samaj gaya main  ","khatam bc"),
        task("samaj gaya main  ","khatam bc")
)
asyncio.run(main())"""


"""import asyncio

async def task():
    print("Start")
    await asyncio.sleep(2)
    print("End")

async def main():
    t1 = asyncio.create_task(task())
    t2 = asyncio.create_task(task())

    await t1
    await t2

asyncio.run(main())"""
        
        
"""import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    print("Task1 acquiring lock1")
    lock1.acquire(timeout = 2)
    time.sleep(1)

    print("Task1 waiting for lock2")
    lock2.acquire(timeout = 2)

    print("Task1 done")
    lock2.release()
    lock1.release()

def task2():
    print("Task2 acquiring lock2")
    lock2.acquire(timeout = 2)
    time.sleep(1)

    print("Task2 waiting for lock1")
    lock1.acquire(timeout = 2)

    print("Task2 done")
    lock1.release()
    lock2.release()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()"""
        
    
"""from pydantic import BaseModel,Field

class User(BaseModel):
    name: str = Field(min_length = 3,max_length = 10)
    age: int = Field(...)
    email : str = Field(pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$")
        
user = User(name="Varad",age="9")
print(user)
"""
    
"""from pydantic import BaseModel,Field,model_validator

class Address(BaseModel):
    city : str = Field(min_length = 3,max_length = 10)
    pincode : int
    
class User(BaseModel):
    name : str
    address : Address
    
    
User = User(
    name = "varad",
    address = {
        "city" : "mumbai" ,
        "pincode": "400444"
    }
)
    
print(User)"""

# counting a number form a user input

num = int(input("enter a positive integer number : "))
total = 0

while num > 0:
    sub = num % 10     # removing an last element
    total = total + sub
    num = num // 10
    
print(total) 

    
    
    
    
    
    
    
    
    
    
    

