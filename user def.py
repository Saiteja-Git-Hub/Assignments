#def sai():
    #print('hello')
#sai()
#sai()

#def sai(x):
    #print('the sqrt of {} is {}'.format(x,x**0.5))
#sai(100)
#sai(200)
#sai(300)

#import math
#result=math.sqrt(100)
#print(result)

#def sai(x,y):
    #return x+y
#print('the addition of x,y:',sai(10,20))

#def sai():
    #print('hello')
#sai()
#print(sai())

#def sai(x):
    #return x
#print(sai('hello'))

#def even(x):
    #if x%2==0:
        #print('even')
    #else:
        #print('odd')
#even(2)
#even(5)
#even(6)
#even(7)

#def even(x):
    #for i in x:
        #if i%2==0:
         #print('even')

#Arguments
#positional arg

#def p(name,regno):
    #print(name,regno)
#p('saiteja',228)

#def p(a,b):
    #print(a+b)
    #print(a-b)
#p(100,200)
#p(100,200)

#def p(c,d):
    #print(c*d)
    #print(c/d)
#p(4,6)
#p(4,8)

#keyword arg

#def kw(a,b):
    #print(a+b)
#kw(a=20,b=30)
#kw(b=30,a=20)

#def kw(c,d):
    #print(c-d)
#kw(c=100,d=200)
#kw(d=200,c=100)

#def kw(a,b):
    #print(a-b)
#kw(10,b=20)
#kw(a=10,20)#error

#def kw(c,d):
    #print(c/d)
    #print(c/d)
#kw(c=200,d=100)
#kw(d=100,c=200)

#default arg

#def d(name,msg):
    #print('hello',name,msg)
#d('sai','good mrng')

#def d(name='guest'):
    #print('hello',name,'good mrng')
#d('sai')
#d()

#def d(name='siva',reg=233):
    #print(name,'hello',reg)
#d()
#d('sai')

#variable length arg

#def sum(*n):
    #total=0
    #for x in n:
        #total=total+x
    #print('sum:',total)
#sum()
#sum(10)
#sum(10,20,30)
#sum(10,20,30,40,50)

#def f(arg1,arg2,arg3=4,arg4=8):
    #print(arg1,arg2,arg3,arg4)
#f(3,2,arg3=10,arg4=20)

#def sum(name,*marks):
    #total=0
    #for x in marks:
        #total=total+x
    #print('hello',name,'your total marks:',total)
#sum('sai',10,20,30,40,50)

#anonymous or lambda function

#s=lambda n:n*n
#print('square of 4 is:',s(4))
#print(s(5))
#for i in range(1,11):
    #print('the square of {} is:{}'.format(i,s(i)))

#global variables
#filter
#maps
#reduce
#aliasing

#nested function(function with another function)

#def f1():
    #def inner(a,b):
        #print('the sum:',a+b)
        #print('the avg:',(a+b)/2)
        #print()
    #inner(10,20)
    #inner(30,40)
    #inner(50,60)
    #inner(70,80)
#f1()

#function can return as another function

#def outer():
    #print('outer function is started')
    #def inner():
        #print('inner function is executed')
    #print('outer function returning inner')
    #return inner
#f=outer()
#f=outer---->giving another name to the function(aliasing)
#f()

#function decorator'@'
#def decor(wish):
    #def inner(name):
        #if name=='sai':
            #print('hello sai bad mrng')
        #else:wish(name)
    #return inner

#@decor
#def wish(name):
    #print('hi',name,'good mrng')
#wish('sai')
#wish('kiran')
#wish('ganesh')

#@decor
#def wish(name):
    #print('hi',name,'good mrng')
#wish('sai')
#wish('kiran')
#wish('ganesh')

#def smartdiv(division):
    #def inner(a,b):
        #if b==0:
            #print('cant divide with zero')
        #else:
            #return division(a,b)
    #return inner

#@smartdiv
#def division(a,b):
    #return a/b 
#print(division(10,2))
#print(division(10,5))
#print(division(10,0))



























