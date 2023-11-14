#1 to one..........................

number=int(input('enter value:'))
if number==1:
    print('one')

#finding big value .................

a=int(input('enter first number:'))
b=int(input('enter secound number:'))
if a>b:
    print('biggest number:',a)
else:
    print('biggest number:,b')
print('i find this')

#searching number between 1 and 100..............

n=int(input('enter the number:'))
if n>1 and n<100:
    print('the number {} is in between 1 and 100'.format(n))
else:
    print('the number {} is not in between 1 and 100'.format(n))
