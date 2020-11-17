def login(custid ,passwd):
    '''The function helps in authentication during login'''
    from User_functions import accounts as acnt
    con = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT custid,passwd FROM users")
    lis = cur.fetchall()
    di = {}
    for i in range(len(lis)):
        di[lis[i][0]] = lis[i][1]

    if custid in list(di.keys()):
        if passwd == di[custid]:
            return True

        else:
            return False

    else:
        return False