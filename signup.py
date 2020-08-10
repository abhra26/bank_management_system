
def signup():
    import accounts as acnt
    print(''' Please fill up the following details correctly :''')
    first_name = input("Enter first name:")
    last_name = input("Enter last name: ")
    name = first_name + ' ' + last_name
    dob = input("enter date of birth:")
    email = input("enter email id:")
    gender = input("enter gender(M/F/O):")
    phone = int(input("enter phone number:"))
    address = input("enter address:")
    city = input("enter city:")
    state = input("enter state:")
    aadhar = input("enter aadhar:")
    zip_code = int(input("enter zip code:"))
    passwd = int(input("set your 4-digit passcode:"))
    con = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = con.cursor()
    cur.execute("SELECT accno FROM users;")
    lis = cur.fetchall()
    try:
        accno = lis[-1][0] + 1

    except:
        accno = 1

    acnt.addto_users(accno, passwd, first_name, last_name, dob, email, phone, address, city, state, aadhar, zip_code,
                     gender)
    acnt.create_table_individual(accno)

    print(f''' Your account details are:
                     Acoount number : {accno}

                     Passcode       : {passwd}

                     Account in the
                     name of        : {name}
                 Please remember these details. Thank you for signing uo
                 You may login now by going back to our home page.''')