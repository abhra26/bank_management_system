
def signup():
    import accounts as acnt
    import sys
    print(''' Please fill up the following details correctly :''')
    first_name = input("Enter first name:")
    last_name = input("Enter last name: ")
    name = first_name + ' ' + last_name
    dob = input("enter date of birth:")
    email = input("enter email id:")
    gender = input("enter gender(M/F/O):")
    mobile = int(input("enter phone number:"))
    address = input("enter address:")
    city = input("enter city:")
    state = input("enter state:")
    aadhar = input("enter aadhar:")
    zipcode = int(input("enter zip code:"))
    passwd = int(input("set your 4-digit passcode:"))
    con = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = con.cursor()
    cur.execute("SELECT accntid FROM users;")
    lis = cur.fetchall()
    cur.execute("SELECT custid FROM users")
    lis2 = cur.fetchall()
    try:
        accntid = lis[-1][0] + 1
        custid = 'cstmr' + str(int(lis2[-1][0][5:])+1)

    except:
        accntid = 1
        custid = 'cstmr1'

    acnt.addto_users(custid, accntid, passwd, email, mobile, city, state, zipcode, aadhar, gender, name, address, dob)

    ch = int(input(''' Enter type of account:
                                1. Credit
                                2.Debit
                                3.Deposit
                                4.Savings
                                
                                Enter choice : '''))
    if ch == 1:
        business = input("enter business details(company,address) if any, else write 'NA':")
        granin = int(input("enter gross annual income : "))
        if granin < 200000:
            print("gross annual income is low.You are not eligible for a credit account")
            sys.exit()

        profit = int(input("enter averaged profit earned per annum(0 IF NO BUSINESS): "))
        ssc = int(input("enter social security code:"))
        turnover = int(input("enter annual trunover of business(0 IF NO BUSINEES):"))
        debt = 0
        timelimit = 'NA'
        acnt.addto_creditacnts(custid, accntid, business, granin, profit, ssc, turnover, debt, timelimit)




    print(f''' Your account details are:
                     Acoount number : {accntid}

                     Passcode       : {passwd}

                     Account in the
                     name of        : {name}

                     
                 Please remember these details. Thank you for signing uo
                 You may login now by going back to our home page.''')