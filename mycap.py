#MY CAPTAIN ASSIGNMENT


#Search for usage of negative numbers as Index

'''l1=[1,2,44,5,66,46,87,90]
print(l1[-1])           #Output: 90
print(l1[-3])  '''         #Output: 46
#negative numbers are used to access the value from last



#Assignment 1.1
#Practise comparison and Assignment  operators

'''#Assignment operators =,+=,-=,*=,/=,**=,&=,|=,...
a=4
a+=5        #a=4+5
print(a)        #Output:9

b=6
b*=7        #b=6*7
print(b)        #Output:42

c=8
c**=2       #c=8^2
print(c)        #Output:64

d=5
d<<=5       #d=5<<2
print(d)        #Output:160'''


#Comparison operators <,>,<=,>=,==,!=
'''x=12
y=14
print(x<y)      #output:True
print(x!=y)#not equal to    #Output:True
print(x==y)            #Output:False
print(x>=y)         #Output: False'''


#2.Practise If and else statement with following sentence
#If it snows I will go out else I will not
#If it rains frogs I will dance

'''snow=0
if snow==1:
    print("I will go Out")
else:   
    print("I will not go out")          #output:I will not go out
    
 
print("If it is snowing outside give number 1 otherwise give 0") 

#or   
snow=int(input("Is it snowing outside:"))
if snow==1:
    print("I will go Out")
else:   
    print("I will not go out")'''
    
'''rain=1
if rain==1:
    print("Frogs will dance")
else:   
    print("Frogs will not dance")          #output:Frogs will dance
    
 
print("If it is raining outside give number 1 otherwise give 0") 

#or   
rain=int(input("Is it raining outside:"))
if rain==1:
    print("Frogs will dance")
else:   
    print("Frogs will not dance")'''
    
    
#Assignments 
#Why do we have the name float

""" A floating point number is a representation of a number which includes
both integer part and fractional part
It consists of two parts called Float and exponent
For eg. We have a number 256 we call it a float but the magnitude of the number
is decided by the exponent it can be 25.6 or 2.56 or 0.00256 so it floats or adjust 
the needs"""

#Use terminal to open Apps
# To Open a File
 

#To open a app
'''c:\Users\Dell>
c:\Users\Dell>cd Downloads     #Output:c:\Users\Dell\Downloads>
c:\Users\Dell\Downloads>whatsapp        #opens whatsapp Application'''




#Arithmetic Operators 
#+,-,*,/,%,**,//
'''
a=26
b=5
print(a+b) #Addition operator ,31
print(a-b)  #Subtraction operator,21
print(a*b)  #Multiplication operator,130
print(a/b)  #Division operator,5.2
print(a%b)  #Modulus operator,1
print(a**b)  #Exponentiation ,11881376
print(a//b)  #Floor Division ,5'''

#Area of circle
'''import math
a=float(input("input the radius of the circle:"))
area= math.pi*a*a
print("The area of the circle with radius",a,"is",area)'''

#Python program to accept a filename from the user and print the extension
'''import os
a=input("filename:")s
split_up=os.path.splitext(a)
file_extension=split_up[1]
print("The extension of the file is:" ,file_extension)'''
'''a,b=(input("Filename:")).split(".")
if b=="py":
    print("python")
elif b=="c":
    print("c prg file")
else:
    print("not python or c or c++ file")'''





#Search for usage of negative numbers as Index

'''l1=[1,2,44,5,66,46,87,90]
print(l1[-1])           #Output: 90
print(l1[-3])  '''         #Output: 46
#negative numbers are used to access the value from last

#To create a set
a=set()         #creates an empty set

#Methods or functions of list
l=[1,4,6,7,8,9]
#sort,append,extend,index,len,clear,insert,count,pop,remove,reverse,copy

#Methods/Functions of list
#capitalize,casefold,center,count,endswith,startswith,format,index,isdigit,replace


#Methods or Functions of Dictionary
#clear,copy,get,keys,pop,popitem,update,values,items

#To create a calculator
'''print("SIMPLE CALCULATOR")
print(""" 1.Addition
            2.Subtraction
            3.Multiplication
            4.Division""")
n=int(input("Enter the operation you would like to perform:"))
a=int(input("first number:"))
b=int(input("second number:"))
def add():
    res=a+b
    print(a,"+",b,"=",res)
def sub():
    res=a-b
    print(a,"-",b,"=",res)
def mul():
    res=a*b
    print(a,"*",b,"=",res)
def div():
    res=a/b
    print(a,"/",b,"=",res)

if n==1:
    add()
if n==2:
    sub()
if n==3:
    mul()
if n==4:
    div()'''
    
    



   
        #Arithmetic Operators 
#+,-,*,/,%,**,//
'''
a=26
b=5
print(a+b) #Addition operator ,31
print(a-b)  #Subtraction operator,21
print(a*b)  #Multiplication operator,130
print(a/b)  #Division operator,5.2
print(a%b)  #Modulus operator,1
print(a**b)  #Exponentiation ,11881376
print(a//b)  #Floor Division ,5'''



#Area of circle
'''import math
a=float(input("input the radius of the circle:"))
area= math.pi*a*a
print("The area of the circle with radius",a,"is",area)'''




#Python program to accept a filename from the user and print the extension
'''import os
a=input("filename:")
split_up=os.path.splitext(a)
file_extension=split_up[1]
print("The extension of the file is:" ,file_extension)'''
#or

'''a,b=(input("Filename:")).split(".")
if b=="py":
    print("python")
elif b=="c":
    print("c prg file")
else:
    print("not python or c or c++ file")'''




#Search for usage of negative numbers as Index

'''l1=[1,2,44,5,66,46,87,90]
print(l1[-1])           #Output: 90
print(l1[-3])  '''         #Output: 46
#negative numbers are used to access the value from last




#To create a set
a=set()         #creates an empty set



#Methods or functions of list
'''l=[1,4,6,7,8,9]
l2=[4,5,1]
#sort,append,extend,index,len,clear,insert,count,pop,remove,reverse,copy
#indexing
print(l[3])         #Output=7
#Slicing
print(l[0:4])       #Output=[1,4,6,7,8]
#append
print(l.append(76)) #Output=[1,4,6,7,8,9,76]
#insert
print(l.insert(2,56)) #Output=[1,4,56,6,7,8,9,76]
#len
print(len(l))         #Output=8
#remove
print(remove(6))      #Output=[1,4,56,7,8,9,76]
#min,max
print(min(l),max(l))  #output=1 76
#sorted
print(sorted(l))    #prints the elements in ascending order
#sorted for descending order of elements
print(sorted(l,reverse=True))
#comparison and concatenation
print(l2>l1)
print(l1+l2)'''




#Methods/Functions of strings
#capitalize,casefold,center,count,endswith,startswith,format,index,isdigit,replace


#Methods or Functions of Dictionary
#clear,copy,get,keys,pop,popitem,update,values,items
dict={1:"python",2:"university",3:"wisdom",4:"myCaptain"}
'''print(dict.get(2))
print(dict.keys())university            
print(dict.values())
print(dict.items())
print(dict.pop(1))
print(dict.clear())'''
'''Output:university
dict_keys([1, 2, 3, 4])
dict_values(['python', 'university', 'wisdom', 'myCaptain'])
dict_items([(1, 'python'), (2, 'university'), (3, 'wisdom'), (4, 'myCaptain')])
python
None'''




#To create a calculator
'''print("SIMPLE CALCULATOR")
print(""" 1.Addition
            2.Subtraction
            3.Multiplication
            4.Division""")
n=int(input("Enter the operation you would like to perform:"))
a=int(input("first number:"))
b=int(input("second number:"))
def add():
    res=a+b
    print(a,"+",b,"=",res)
def sub():
    res=a-b
    print(a,"-",b,"=",res)
def mul():
    res=a*b
    print(a,"*",b,"=",res)
def div():
    res=a/b
    print(a,"/",b,"=",res)

if n==1:
    add()
if n==2:
    sub()
if n==3:
    mul()
if n==4:
    div()'''
    
#using "for loop " to create an infinite loop
'''for _ in 
infinity generator():
pass'''

'''def infinity_generator:
    while True:
        yield
for _ in
infinity_generator():
    pass'''
    
    
    
    
# Step function  in "for loop"
#increment values by 2 in the range instead of 1
'''for i in range(0,25,2):
    print(i)'''
    
    
    
#To add elements to a tuple
tup=(1,2,55,4,67,81)
'''tup=list(tup)
# can use append or insert
tup.append(75)
tup=tuple(tup)
print(tup)'''
#using concatenation
'''tup2=(75,64,94)
print(tup+tup2)'''

#most frequent and prints letters in decreasing order of frequency
'''a="mississippi"
m=0
i=0
s=0
p=0
for j in a :
    if j=="m":  
        m+=1
    elif j=="i":
        i+=1
    elif j=="s":
        s+=1
    else :
        p+=1
print("i=",i)
print("m=",m)
print("s=",s)
print("p=",p)'''

#or
def most_frequent(string):
    d=dict()
    for i in string:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
a=input("Enter a word:")
print(most_frequent(a))
















