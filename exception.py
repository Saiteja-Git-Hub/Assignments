#try:
    #print(10/0)
#except BaseException:
    #print('zero can not divided')
    #print(10/2)

#try:
    #print(10/0)
#except ZeroDivisionError:
    #print('zero can not divided')
    #print(10/2)

#nested exception handling

#try:
    #print("outer try block")#
    #try:
        #print("inner try block")#
        #print(50/0)
    #except ZeroDivisionError:
        #print("inner except block")#
    #finally:
        #print("inner finally block")#
    #print("outside the inner block")#
#except ZeroDivisionError:
    #print(40/0)
    #print("outer except block")
#finally:
    #print("outer finally block")#
#print("outside the all block")#
    
#try:
    #print('statement-1')
    #print(10/0)
#except ZeroDivisionError as m:
    #print('type of exception',type(m))
    #print('type of exception',m.__class__)
    #print('exception name',m.__class__.__name__)
    #print('description of exception:',m)
    #print(10/3)
#print('statement-3')

#multiple except blocks

#try:
    #x=int(input('enter first number:'))
    #y=int(input('enter second number:'))
    #print('the result:',x/y)
#except ZeroDivisionError:
    #print('cant divide with zero')
#except ValueError:
    #print('please give int value')

#order is imp(pvm is con top to bottom)

#try:
    #print(10/0)
#except ZeroDivisionError:
    #print('cant divide with zero')
#except ArithmeticError:
    #print('arithmetic error')

#try:
    #print(10/0)
#except ArithmeticError:
    #print('arithmetic error')
#except ZeroDivisionError:
    #print('cant divide with zero')


#class PassException(Exception):
    #def __init__(self,arg):
        #self.msg=arg

#class FailException(Exception):
    #def __init__(self,arg):
        #self.msg=arg

# class ValueError(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#try:
    #marks=int(input("enter you total marks: "))
#except ValueError:
    #print("please enter the vaild number")
#if marks>=50:
    #raise PassException("congrats you cleared this semester ")
#elif marks <50:
    #raise FailException("sorry better luck next time")


#single except block with multiple handling errors

#try:
    #x=int(input('enter any number:'))
    #y=int(input('enter any number:'))
    #print(x/y)
#except(ZeroDivisionError,ValueError)as m:
    #print('raised exception:',m.__class__.__name__)
    #print('description of exception:',m)
    #print('please provide valid input')

#default except Block(must be in last)

#try:
    #x=int(input('enter any number:'))
    #y=int(input('enter any number:'))
    #print(x/y)
#except ZeroDivisionError:
    #print('cant divide with zero')
#except:
    #print('default except:please provide valid input')

#with finally block(it always exicuted at any senario)

#try:
    #print(10/0)
#except ZeroDivisionError:
    #print(20/2)
#finally:
    #print('finally')
#print('end')

#exception not matched(AT)

#try:
    #print('try')
    #print(10/0)
#except ValueError:
    #print('error')
#finally:
    #print('finally')
#print('end')

#exit from finally

#import os
#try:
    #print('try')
    #os._exit(0)
#except:
    #print('default')
#finally:
    #print('finally')

#try:
    #print('try')
    #print(10/0)
    #print('stoped')
#except ZeroDivisionError:
    #print(10/2)
#finally:
    #print(20/2)
#print('final')

#x=10
#if x>10:
    #print('true')
#else:
    #print('false')

#for x in range(10):
    #if x>5:
      #break
    #print(x)

#with using else(try,except,else,finally)

#try:
    #print('try')
#except:
    #print('except')
#else:
    #print('else') #if there is no exception in try it will excecuted
#finally:
    #print('finally')





    






