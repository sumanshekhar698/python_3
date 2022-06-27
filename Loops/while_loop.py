
def swap_a_number(a,b):
    c = a
    a = b
    b = c
    return a,b # returning multiple arguments in form of tuple

#dynamic swapping
def swap_a_number_dynamic(a,b):
    print(f'BEFORE : a = {a} b = {b}')
    a , b = b , a#Dynamic Internal Pythn swap
    print(f'AFTER : a = {a} b = {b}')

# while loop 
def factorial(n):
    result = 1
    while(n>1):
        result *=n
        n-=1
    return result

#for loop and range fn
def play_with_range():
    for i in range(-1,11):#start and stop-1
        print(i,end=" ")
    print()
    for i in range(-1,11,2):#start, stop-1 and steps
        print(i,end=" ")
    print()
    for i in range(11,-4,-2):#start, stop-1 and reverse steps
        print(i,end=" ")
    print()

if __name__ == "__main__":
    ans=factorial(10)
    print(ans)

    play_with_range()
    
    a = 8
    b = 9

    swapped_number = swap_a_number(a,b)
    print(id(swapped_number))#prints unique ID of the object
    print(type(swapped_number))#<class 'tuple'>
    print(swapped_number)

    a,b = swapped_number#dynamic unpacking of tuple
    print(f'a = {a} b = {b}')

    swap_a_number_dynamic(a,b)