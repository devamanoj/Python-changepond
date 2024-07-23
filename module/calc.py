import arithmatic
print('choose the operators')
print('1.Addition\n2.Subtraction\n3.Multiplication')
select=int(input('select 1/2/3'))
def main():
    num1 = int(input('Enter 1 st number:'))
    num2 = int(input('Enter 2 nd number:'))

    if(select==1):
        ans = arithmatic.addition(num1,num2)
        print(f"Addition {num1} and {num2}:",ans)
    elif(select==2):
        ans = arithmatic.subtraction(num1,num2)
        print(f"Subtraction {num1} and {num2}:",ans)
    elif(select==3):
        ans = arithmatic.multiplication(num1,num2)
        print(f"Multiplication {num1} and {num2}:",ans)
    else:
        print('choose 1/2/3')
if __name__=="__main__":
        main()