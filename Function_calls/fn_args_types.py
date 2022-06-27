def power(base, exponent=1):#default arguments
    print(base**exponent)

def show_student_data (*details):
    print(type(details))# tuple is the type for var args
    for i in details:
        print(i,end=" ")#end =" " parameter prevents changing of line while printing 
        #and adds a space between each printing operation

def show_details_student (**details):
    print(type(details))# dictionary
    for key,value in details.items():
        print(f'STUDENT ROLL: {key} | STUDENT NAME: {value} ')

if __name__ == "__main__":
    show_student_data("Simarn", 1,"Suman",89)#vargs
    print()#to change the line
    list_of_data = ["Simarn", 1,"Suman",89]
    show_student_data(*list_of_data)#dynamic unpacking
    print()#to change the line

    #kwargs
    # details_of_student = {1:"Suman" , 2 :"Amy" , 8 :'Simran', 3:"Satya"}#dictionary
    # show_details_student(first ='Python', mid ='is', last='Fun')#dynamic unpacking


    power(2)#default args (exponent=1)
    power(2,10)#positional args
    power(exponent=10, base=2)#keyword args