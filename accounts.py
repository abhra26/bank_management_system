
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


def addto_users(custid,accntid,passwd,email,mobile,city,state,zipcode,aadhar,gender,name,address,dob):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO users VALUES
    ('{custid}',{accntid},'{passwd}','{email}','{mobile}','{city}','{state}','{zipcode}','{aadhar}','{gender}','{name}','{address}','{dob}');
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







