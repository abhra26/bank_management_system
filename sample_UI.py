import accounts as acnt
import signup
import sys

print('''
......WELCOME TO VIRTUAL BANK......
published by : @abhraneel, @arijeet
Description : It is a local virtual bank management system set up
              to describe the python-mysql interface. This is our
              submission for the computer project assignment for 
              the accademic session of 2020-21 of class XII. Stay safe and healthy.
              Please do listen our explaination. Thank you
              
XXXXXXXX SPECIFICATIONS XXXXXXXXX

# Developed on : MACBOOK PRO,
                 13inches, 
                 8GB RAM, 
                 512GB internal memory,
                 MACOS mojave, 
                 intel core i5 
                 
#FRONT END : Tkinter
#MIDDLE-WARE: PYTHON
#BACKEND : MYSQL

XXXXXXXX END XXXXXXXXX

........PROGRAM BEGINS FROM HERE.......
''')
print()
print()

print('''
    WELCOME. PLEASE CHOOSE FROM THE FOLLOWING : 
    1. Login
    2.Sign Up
    3. Exit

''')

entry = int(input('enter choice : '))

if entry == 1:
    usr = int(input('enter account number:'))
    passwd = int(input('enter 4-digit passcode :'))
    con = acnt.establish_connection('localhost','root','vishal26','bank')
    cur = con.cursor()
    cur.execute("SELECT accno,passwd FROM users")
    lis = cur.fetchall()
    di = {}
    for i in range(len(lis)):
        di[lis[i][0]] = lis[i][1]

    if usr in di.keys():
        if passwd == di[usr]:
            print('login sucessful')

        else:
            print("Invalid Passcode")

    else:
        print("invalid account number,You may sign up first then try to login")

elif entry == 2:
    signup.signup()

else:

    print("Thank you and have a great day. Bye")
    sys.exit(0)



















