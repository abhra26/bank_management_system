
def establish_connection(host, user, passwd, database):
    import mysql.connector as cntr
    from mysql.connector import Error
    connection = None
    try:
        connection = cntr.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database
            )

        return connection

    except Error as e:
        return f'An error occured : {e}'


def addto_users(custid,accntid,passwd,email,mobile,city,state,zipcode,aadhar,gender,name,address,dob,status = "open"):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO users VALUES
    ('{custid}',{accntid},'{passwd}','{email}','{mobile}','{city}','{state}','{zipcode}','{aadhar}','{gender}','{name}','{address}','{dob}','{status}');
    ''')
    conection.commit()

def addto_creditacnts(custid,accntid,business,granin,profit,ssc ,turnover,debt,timelimit):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO creditacnts VALUES
        ('{custid}',{accntid},'{business}',{granin},{profit},{ssc},{turnover},{debt},'{timelimit}');
        ''')
    conection.commit()

def addto_acntcard(accntid,cardno,type):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO acntcard VALUES
            ({accntid},{cardno},'{type}');
            ''')
    conection.commit()

def addto_acnttype(accntid,type):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO acnttype VALUES
                ({accntid},'{type}');
                ''')
    conection.commit()

def getno_of_acnts(cust_id):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''SELECT accntid FROM USERS
    WHERE custid = '{cust_id}';
    ''')
    lis = cur.fetchall()
    result = []
    for i in lis:
        for j in i:
            result.append(j)

    return result
def get_status_account(accntid):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''SELECT status FROM USERS
        WHERE accntid = '{accntid}';
        ''')
    txt = cur.fetchall()[0][0]
    return txt
def block_cust(custid):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''UPDATE users SET status = 'blocked'
            WHERE custid = '{custid}';
            ''')
    conection.commit()







    










