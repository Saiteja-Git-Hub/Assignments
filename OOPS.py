#various usage of static variable

#class Test:
    #a=10
    #def __init__(self):
        #Test.b=20
    #def m1(self):
        #Test.c=30
    #@classmethod 
    #def c1(cls):
        #cls.s=40
        #Test.v=50
    #@staticmethod
    #def s1():
        #Test.f=80

#t=Test()
#t.m1()
#Test.c1()
#Test.s1()
#Test.g=100
#print(Test.__dict__)

#class Test:
    #a=10
    #def __init__(self):
        #self.b=20
#t1=Test()
#t2=Test()
#Test.a=77
#t1.b=99
#print('t1:',t1.a,t1.b) #77,99
#print('t2:',t2.a,t2.b) #77,20

#class Test:
    #a=10
    #def __init__(self):
       #self.b=20
    #def m1(self):
        #self.a=77
        #self.b=88
#t1=Test()
#t2=Test()
#t1.m1()
#print('t1:',t1.a,t1.b)
#print('t2:',t2.a,t2.b)

#class Test:
    #a=10
    #def __init__(self):
        #self.b=20
    #@classmethod
    #def m1(cls):
        #print('this is classmethod')
        #cls.a=99
        #cls.b=100
#t=Test()
#t.m1() #by using obj ref
#Test.m1() #using class name
#t1=Test()
#t2=Test()
#Test.m1()
#print('t1:',t1.a,t1.b)
#print('t2:',t2.a,t2.b)
#print('Test:',Test.a,Test.b)

#assign values using @
#class myclass:
    #def __init__(self,x,y):
        #self.x=x
        #self.y=y
        #print(x)
        #print(y)
        
    #@classmethod
    #def create_from_str(cls,string):
        #print(string)
        #x,y=map(int,string.split(","))#[6,9]
        #return cls(x,y)
    
#obj=myclass.create_from_str("6,9")

#using normal method
#class myclass:
    #def __init__(self,string):
        #self.string=string

    #def m1(self):
        #a,b=map(int,self.string.split(","))
        #print(a) # self.a=a
        #print(b) # self.b=b
    #def m2(self):
        #print(self.a)
        #print(self.b)

#obj=myclass('4,8')
#obj.m1()
#obj.m2()

#class Test:
    #a=10
    #def __init__(self):
        #Test.b=20
        
    #def m1(self):
        #Test.c=80
        #self.u=499
    
    #@classmethod
    #def m2(cls):
        #Test.d=700
        #cls.e=200
        #cls.y=90
    
    #@staticmethod
    #def m3():
        #Test.f=500

# print(Test.__dict__)

#t=Test()
#t.m1()
#Test.m2()
#Test.m3()
#print(t.__dict__)


#class Test:
    #a=10
    #def __init__(self):
        #print(self.a)
        #print(Test.a)
    
    #def m1(self):
        #print(self.a)
        #print(Test.a)

    #@classmethod
    #def m2(self):
        #print(self.a)
        #print(Test.a)

    #@staticmethod
    #def m3():
        #print(Test.a)

# print(Test.a)
# print(Test.__dict__)
#t=Test()
#t.m1()
#t.m2()
#t.m3()
#print(t.a)


#class Test:
    #a=10
    #def __init__(self):
        #self.a=999
    
    #def m1(self):
        #self.a=800
    #@classmethod
    #def m2(cls):
        #cls.a=600
    #@staticmethod
    #def m3():
        #Test.b=200
        #Test.b=300
#print(Test.a)
#t=Test()
#t.m1()
#t.m2()
#t.m3()
#t.b=500
#print(t.a)
#print(Test.b)

#deleting a static variable

#class Test:
    #a=70
    #@classmethod
    #def m1(cls):
        #del cls.a
#Test.m1()
#print(Test.__dict__)

#class Test:
    #a=10
    #def __init__(self):
        #Test.b=20
        #del Test.a
    #def m1(self):
        #Test.c=30
        #del Test.b
    #@classmethod
    #def m2(cls):
        #cls.d=677
        #del Test.c
    #@staticmethod
    #def m3():
        #Test.r=60
        #del Test.d
        
#t=Test()
#t.m1()
#t.m2()
#t.m3()
#print(Test.d)


#import sys
#class customer:
    #Bankname="SBI"
    #def __init__(self,name,balance=0.0):
        #self.name=name
        #self.balance=balance
    #def deposit(self,amount):
        #self.balance=self.balance+amount
        #print("the balance after the deposit is :",self.balance)
    #def checkbal(self,amount):
        #self.balance=self.balance+amount
        #print("Total balance",self.balance)
    #def withdraw(self,amount):
        #if amount>self.balance:
            #print("insufficient amount, please withdraw with in the balance amount")
            #sys.exit()
        #self.balance=self.balance-amount #
        #print('balance after withdraw:',self.balance)#

        #else:
            #print('balance after withdraw:',self.balance-amount)

        
#print("welcome to ",customer.bankname)
#name=input("Enter your name:")
#c=customer(name)
#while True:
    #print("\n d-deposit\n w-withdraw\n c-check bal\n e-exit")
    #option =input("choose your option:").lower()
    #if option=="d":
        #amount=int(input("enter the amount to deposit : "))
        #c.deposit(amount)
    #elif option=="w":
        #amount=int(input(" enter the withdraw amount :"))
        #c.withdraw(amount)
    #elif option=="c":
        #print('total bal in ur acc',amount)
    #elif option=="e":
        #print("thank you for banking with us ")
        #sys.exit()
    #else:
        #print("invaild option, please select correct option ")


#create a class with instance variables

#class person:
    #def __init__(self,name,age):
        #self.name=name
        #self.age=age
    #def details(self):
        #print('Hello, my name is:{} and my age is:{}'.format(self.name,self.age))

#person1=person('sai',25)
#person2=person('vikram',28)

#person1.details()
#person2.details()

#creating vehicle class with out any variables and methods

#class vehicle:
    #pass

#v=vehicle()


#Creating a child class Bus that will inherit all of the variables and methods of the Vehicle class

#class Vehicle:
    #def __init__(self, make, model, year):
        #self.make = make
        #self.model = model
        #self.year = year

    #def display_info(self):
        #print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


#class Bus(Vehicle):
    #def __init__(self, make, model, year, capacity):
        #super().__init__(make, model, year)
        #self.capacity = capacity

    #def display_info(self):
        #super().display_info()
        #print(f"Capacity: {self.capacity}")


#if __name__ == "__main__":
    #bus = Bus("Volvo", "XYZ", 2020, 50)
    #bus.display_info()

#instance method (obj related methods)
#self.grade() # this is for inside the class #display method
#s.garde() #outside the class

#instance method
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def display(self):
#         print("hi",self.name)
#         print("marks",self.marks)
    
#     def grade(self):
#         if self.marks>70:
#             print("you got first garde")
#         elif self.marks>50:
#             print("you got second grade")
#         else:
#             print("got c grade")
    
# s=Student("saiteja",25)
# s.display()
# s.grade()


#class methods

# class human:
#     legs=2
#     @classmethod
#     def walk(cls,name):
#         print("{} walk with {} legs".format(name,cls.legs))

# t=human()
# t.walk("saiteja") 

# human.walk("saiteja")
# human.walk("kalyan")


#a method using
#instance var -->at least one instance var in method, it is instance method
#static var--> class method
#instance var +static var==> Instance method
#imnsatnce var + local var---> instance method
#static var +local var--> @classmethod
#local var ---> @static method(general utility methods)
#class method always talks about class level data ---> static var
# static method never talks about class level var (general)


#accessing members of one class inside another class

# class employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
    
#     def display(self):
#         print("eno : ",self.eno)
#         print("ename ",self.ename)
#         print("esal : ",self.esal)

# class Test:
#     def modify(emp):
#         emp.eno=emp.eno+1000
#         print("printing name inside test class modify method ",emp.ename)
#         emp.display()

# e=employee(23,"aman",2000)
# Test.modify(e)


#accessing members of two classes inside another class

# class ClassA:
#     def method_a(self):
#         print("Method A from ClassA")


# class ClassB:
#     def method_b(self):
#         print("Method B from ClassB")


# class NewClass:
#     def __init__(self):
#         self.class_a = ClassA()
#         self.class_b = ClassB()

#     def method_c(self):
#         print("Method C from NewClass")


# obj = NewClass()
# obj.class_a.method_a()  # Access method from ClassA
# obj.class_b.method_b()  # Access method from ClassB
# obj.method_c()  # Access method from NewClass


#accessing inner class example

# class outer:
#     def __init__(self):
#         print("outer class object creations")
    
#     class Inner:
#         def __init__(self):
#             print("inner class of creation")

#         class New:
#             def __init__(self):
#                 print("New class creation")

#             def m1(self):
#                 print("new class method")

# # Creating an object of the outer class
# o=outer()

# # Creating an object of the Inner class (nested inside outer)
# i=outer.Inner()

# # Creating an object of the New class (nested inside Inner)
# n=outer.Inner.New()

# # Calling method m1 of the New class
# n.m1()




