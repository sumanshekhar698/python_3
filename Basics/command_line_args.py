import sys
# To use Command Line Arguments, we use an inbuilt module called sys 

print("Hello")
print(sys.argv[0])#CommandLineArguments.py (the 1st parameter will always be the file name)
print(sys.argv[1])#Python
print(sys.argv[2])#is
print(sys.argv[-1])#with

print(type(sys)) #<class 'module'>
print(type(sys.argv)) #<class 'list'>
print(len(sys.argv)) #9