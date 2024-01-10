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
