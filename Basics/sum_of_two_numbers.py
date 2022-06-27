# Global Variables
a=20
b=80
product = a*b
power = a**2
# print(f'sum = {a + b}') #100
# print(power) #400

# def keyword is used to define functions in python 
def add(a,b):
    # local variables
    c = 9
    print(__name__)#Stores the name of current file(module) 
    print(a+b)

# print(__name__) #__main__
# The below line will prevent from automatic execution while importing in other modules
if __name__ == "__main__":
    add(5,5)
    print(f'the evaluation of {a}^{2} is {power}') #the evaluation of a=20^2 =400
    # If we try to concatenate a String with a differne data type , we will get 'TypeError'
    print(type(__name__)) #<class 'str'>
    print(__name__) #__main__

    # for i in range(-4,10):
    #     print(i)