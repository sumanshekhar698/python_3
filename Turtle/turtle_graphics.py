import turtle


def square(length):
    # defaule oriewntation is right 
    rafale=turtle.Turtle()
    print(type(rafale))
    rafale.fd(length)
    rafale.rt(90)
    rafale.fd(length)
    rafale.rt(90)
    rafale.fd(length)
    rafale.rt(90)
    rafale.fd(length)
    rafale.rt(90)

def square_using_forloop(length):
    # defaule oriewntation is right 
    rafale=turtle.Turtle()
    for i in range(4):
        print(i)
        rafale.fd(length)
        rafale.rt(90)


def polygon_of_n_sides(n,length):
    if(n<0):
        print(f'Illegal closed shape of sides {n}')
    elif(n<3):
        print(f"Polygon impossible with sides {n}")
        return
    else:
        angle_of_turn = 360/n
        rafale = turtle.Turtle()
        for i in range(n):
            rafale.fd(length)
            rafale.lt(angle_of_turn)


if __name__ == "__main__":
    print(type(turtle))
    # square_using_forloop(300)
    polygon_of_n_sides(length=2,n=100)#keyword arguments
    # square(400)