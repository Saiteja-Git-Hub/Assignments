#break#
#for i in range(10):
    #if i==7:
        #print('execution is done and break the loop')
        #break
    #print(i)
#print('out side the loop')
#.........................#
#cart=[10,20,30,600,40,50,60]
#for item in cart:
    #if item>500:
        #print('place this order,proof must be required')
        #break
    #print('processing the items:',item)
#continue#
#for i in range(10):
    #if i%2==0:
        #continue
    #print(i)
#.........................#
#cart=[10,20,30,600,700,400,300]
#for item in cart:
    #if item>500:
        #print('skip the product')
        #continue
    #print('items:',item)
#...........................#
l=[10,20,30,0,40,0,50,60]
for x in l:
    if x==0:
        print('division with zero is not possible')
        continue
    print('100/{}={}'.format(x,100//x))
