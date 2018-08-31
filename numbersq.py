from datetime import date

def age(yob):
    
    today= date.today().year
    age = today- yob
    if (age < 18):
        print('Minor')
    elif (age >= 18 and age < 36):
        print('Youth')
    else:
        print ('elder')


if __name__ == '__main__':
    yob = int(input('Please Enter your year of Birth:'))
    age(yob)