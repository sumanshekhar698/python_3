# from distutils.command.build_scripts import first_line_re
# from xmlrpc.client import boolean

# str
simran ="Simran Bhat"
print(len(simran)) #11
print((type(simran))) #<class 'str'>

# float 
a =8.9
print((type(a))) #<class 'float'>

# int 
b = 8
print(type(b)) #<class 'int'>

c= a+b
print(type(c)) #<class 'float'>

# bool
d = True
print(d)
print(type(d)) #<class 'bool'>


b = d #this is possible in Python as everything is object
print(b) #<class 'bool'>

x = 7 + 8j
print(type(x)) #<class 'complex'>

# Examples
first_character = 'X'
print(type(first_character))#<class 'str'> as there is not char data type in python

e = 10
print(type(e)) #<class 'int'>
  
#there is no physical limit for int data type, only limiyt is RAM memory
e = 10000000000000000000000000000000000000000000
print(type(e)) #<class 'int'>