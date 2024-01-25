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

