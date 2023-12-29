#handling binary data

#f1=open('pythonex.jpg','rb')
#f2=open('pythonex.jpg','wb')
#d=f1.read()
#f2.write(d)
#f1.close()
#f2.close()
#print()

# handling csv file (comma seprated values)

#import csv

#with open("emp.csv",'w',newline='') as a:
    #w=csv.writer(a)
    #w.writerow(["emp_id","emp_name","emp_phn","total marks","pass marks"])
    #n=int(input("enter number of employee to entry details:"))
    #for i in range(1,n+1):
        #print(i," EMPLOYEE DEATILS ")
        #eid=int(input("enter employee no :"))
        #ename=input("enter the emp name :")
        #ephn=int(input("enter the emp phn :"))
        #totalmarks=int(input("enter pass marks:"))
        #passmarks=int(input("enter total marks:"))

    #w.writerow([eid,ename,ephn,totalmarks,passmarks])
    #print("total emp data written to csv file ")

#creating zip file

#f1=open('hero.text','w')
#f2=open('director.text','w')

#from zipfile import *

#f=ZipFile('files.zip','w',ZIP_DEFLATED)
#f.write('hero.text')
#f.write('director.text')
#f.write('emp.csv')
#f.close()
#print('zip file created')

#un-zipping the file

#f=ZipFile('files.zip','r',ZIP_STORED)
#names=f.namelist()
#for name in names:
    #print('file name:',name)
    #print('content of the file')
    #f=open(name,'r')
    #print(f.read())
    #f.close()
    #print()

#import os
#cwd=os.getcwd()
#print('cwd',cwd)          
#cwd=os.mkdir('sai/abc2')
#cwd=os.mkdir('sai/abc3')
#cwd=os.mkdir('sai/abc4')
#wd=os.makedirs('sa/99/77/666')

#os.removedirs('ABC/1/2/3/4')
#os.removedirs('sai/abc1')




