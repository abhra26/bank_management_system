def signup(name,dob,email,gender,mobile,address,city,state,aadhar,zipcode,passwd,variable,cust_id):
    '''This function adds the details of customers to users depending on the condition
    where new customer or not'''
    from User_functions import accounts as acnt
    lis = get_custid_accntid()
    if variable == 'new_cust':
        acnt.addto_users(lis[0],lis[1], passwd, email, mobile, city, state, zipcode, aadhar, gender, name, address, dob)
        return lis
    else:
        acnt.addto_users(cust_id,lis[1], passwd, email, mobile, city, state, zipcode, aadhar, gender, name, address,dob)
        lis[0] = cust_id
        return lis



def get_custid_accntid():
    '''The funtion genereates new customer id and account id for registering customer'''
    from User_functions import accounts as acnt
    con = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = con.cursor()
    cur.execute("SELECT accntid FROM users;")
    lis = cur.fetchall()
    cur.execute("SELECT DISTINCT custid FROM users")
    lis2 = cur.fetchall()
    try:
        accntid = lis[-1][0] + 1
        custid = 'cstmr' + str(int(lis2[-1][0][5:]) + 1)

    except:
        accntid = 1
        custid = 'cstmr1'
    return [custid,accntid]

def eligibility_credit(income):
    '''The function checks the eligibility of a customer for a credit account'''
    if income>200000:
        return True
    else:
        return False