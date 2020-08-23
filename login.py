
import accounts as acnt

def login(usr,passwd):
    import accounts as acnt
    con = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = con.cursor()
    cur.execute("SELECT accntid,passwd FROM users")
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




