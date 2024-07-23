#Area of circle=pir^2
def area(radius,pi=3.14):
    print('radius:',radius)
    print('pi value:',pi)
    result = pi*radius*radius
    return result
def main():
        #positional argument
        # output_1 = area(10,12)
        # print('area of circle=',output_1)
        #keyword argument
        output_2 =area(pi=3,radius=12)
        print('Area of circle:',output_2)
        output_2 =area(radius=12)
        print('Area of circle:',output_2)
if __name__=="__main__":
    main()