import datetime
today = datetime.date.today()
year = today.year
print(year)
try:
    yob = int(input("Enter your year of birth: "))
    age = year-yob
finally:
    print("program is over")
    if(age<18):
        raise Exception(f'The age should be greater than 18 and your age is {age}')
    print(age)
