
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
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    custids = get_allcustid()
    if custid in custids:
        cur.execute(f'''UPDATE users SET status = 'blocked'
            WHERE custid = '{custid}';
            ''')
        conection.commit()
        description = f'customer id {custid} blocked due to security reasons'
        txn.add_req_transac(description,custid)
        return True
    else:
        return False

def block_accntid(custid,accntid):
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    accntids = get_allaccntid()
    if accntid in accntids:
        cur.execute(f'''UPDATE users SET status = 'blocked'
                WHERE accntid = {accntid};
                ''')
        description = f'Account id {accntid} blocked for security reasons'
        txn.add_req_transac(description,custid,accntid)
        conection.commit()
        return True
    else:
        return False

def open_cust(custid):
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    custids = get_allcustid()
    if custid in custids:
        cur.execute(f'''UPDATE users SET status = 'open'
            WHERE custid = '{custid}';
            ''')
        conection.commit()
        description = f'customer id {custid} opened'
        txn.add_req_transac(description,custid)
        return True
    else:
        return False

def open_accntid(custid,accntid):
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    accntids = get_allaccntid()
    if accntid in accntids:
        cur.execute(f'''UPDATE users SET status = 'open'
                WHERE accntid = {accntid};
                ''')
        description = f'Account id {accntid} opened'
        txn.add_req_transac(description,custid,accntid)
        conection.commit()
        return True
    else:
        return False

def get_email(cardno='NA',custid='NA'):
    import cardlog as cl
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    try:
        accntid = cl.get_accntid(cardno)
        cur.execute(f'''SELECT email FROM users WHERE accntid={accntid};''')
        result = cur.fetchall()[0][0]
        return result
    except:
        cur.execute(f'''SELECT email FROM users WHERE custid='{custid}';''')
        result = cur.fetchall()[0][0]
        return result

def get_name(custid):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''SELECT name FROM users WHERE custid = '{custid}';''')
    result = cur.fetchone()[0]
    return result

# def addto_spouse_credit_card_appl(cardno,custid,name,dob,aadhar,income,card_type,card_company,occupation):
#     conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
#     cur = conection.cursor()
#     cur.execute(f'''INSERT INTO card_applications VALUES
#     ('{custid}',{accntid},'{name}','{dob}',{phone},{aadhar},{income},'{card_type}','{card_company}','{occupation}');''')
#     conection.commit()

def addto_spouse_credit_card_appl(custid,accntid,name,dob,phone,aadhar,income,card_type,card_company,occupation):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO card_applications VALUES
    ('{custid}',{accntid},'{name}','{dob}',{phone},{aadhar},{income},'{card_type}','{card_company}','{occupation}');''')
    conection.commit()

def addto_spouse_card(cardno,name,dob,aadhar,occupation,income,custid):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO spouse_credit_cards VALUES
        ({cardno},'{name}','{dob}',{aadhar},'{occupation}',{income},'{custid}');''')
    conection.commit()



def get_allcustid():
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute('''SELECT DISTINCT custid FROM users;''')
    out = cur.fetchall()
    result = []
    for i in out:
        for j in i:
            result.append(j)
    return result

def get_allaccntid():
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute('''SELECT accntid FROM users;''')
    out = cur.fetchall()
    result = []
    for i in out:
        for j in i:
            result.append(j)
    return result

def has_wife(cust):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''SELECT custid FROM spouse_credit_cards;''')
    out = cur.fetchall()
    fi = []
    for i in out:
        for j in i:
            fi.append(j)
    cur.execute(f'''SELECT custid FROM card_applications;''')
    out2 = cur.fetchall()
    fi2 = []
    for i in out2:
        for j in i:
            fi2.append(j)

    if str(cust) in fi+fi2:
        return True
    else:
        return False

def delete_accnt(custid,accntid):
    import cardlog as cl
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    if has_wife(custid):
        if accntid in get_allaccntid():
            cur.execute(f''' DELETE FROM acnttype WHERE accntid = {accntid};
            ''')
            conection.commit()
            if cl.has_card(accntid):
                cardno = cl.get_cardno(accntid)
                for i in cardno:
                    try:
                        cur.execute(f''' DELETE FROM cardlog WHERE cardno = {i};
                        ''')
                        conection.commit()
                        description = f"cardno: {i} deleted"
                        txn.add_req_transac(description,custid,accntid,i)
                    except:
                        cur.execute(f''' DELETE FROM spouse_credit_cards WHERE cardno = {i};
                                                ''')
                        cur.execute(f''' DELETE FROM cardlog WHERE cardno = {i};
                                                ''')
                        conection.commit()
                        description = f"cardno: {i} deleted"
                        txn.add_req_transac(description, custid, accntid, i)
                cur.execute(f'''DELETE FROM acntcard WHERE accntid = {accntid};''')
                conection.commit()
            cur.execute(f'''DELETE FROM creditacnts WHERE accntid = {accntid};''')
            conection.commit()
            cur.execute(f'''DELETE FROM users WHERE accntid = {accntid};''')
            conection.commit()
            description = f"account id: {accntid} deleted"
            txn.add_req_transac(description,custid,accntid)
            return True
        else:
            return False
    else:
        if accntid in get_allaccntid():
            cur.execute(f''' DELETE FROM acnttype WHERE accntid = {accntid};
                ''')
            conection.commit()
            if cl.has_card(accntid):
                cardno = cl.get_cardno(accntid)
                for i in cardno:
                    cur.execute(f''' DELETE FROM cardlog WHERE cardno = {i};
                        ''')
                    conection.commit()
                    description = f"cardno: {i} deleted"
                    txn.add_req_transac(description, custid, accntid, i)
                cur.execute(f'''DELETE FROM acntcard WHERE accntid = {accntid};''')
                conection.commit()
            cur.execute(f'''DELETE FROM creditacnts WHERE accntid = {accntid};''')
            conection.commit()
            cur.execute(f'''DELETE FROM users WHERE accntid = {accntid};''')
            conection.commit()
            description = f"account id: {accntid} deleted"
            txn.add_req_transac(description, custid, accntid)
            return True
        else:
            return False
def delete_cust(custid):
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    if custid in get_allcustid():
        cur.execute(f'''SELECT accntid FROM users WHERE custid = '{custid}';''')
        result = cur.fetchall()
        for i in result:
            for j in i:
                delete_accnt(custid,j)
        description = f"customer:{custid} deleted"
        txn.add_req_transac(description,custid)
        return True
    else:
        return False
def update_users(custid,field,new_data,accntid = 0):
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    field = field.lower()
    if accntid == 0:
        if custid in get_allcustid():
            try:
                cur.execute(f'''UPDATE users SET {field} = '{new_data}' WHERE custid = '{custid}';''')
                conection.commit()
            except:
                cur.execute(f'''UPDATE users SET {field} = {new_data} WHERE custid = '{custid}';''')
                conection.commit()

            description = f"{field} of {custid} has been updated to {new_data}"
            txn.add_req_transac(description,custid)
            return True
        else:
            return False
    else:
        if custid in get_allcustid() and accntid in get_allaccntid():
            try:
                cur.execute(f'''UPDATE users SET {field} = '{new_data}' WHERE accntid = {accntid};''')
                conection.commit()
            except:
                cur.execute(f'''UPDATE users SET {field} = {new_data} WHERE accntid = {accntid};''')
                conection.commit()

            description = f"{field} of {accntid}({custid}) has been updated to {new_data}"
            txn.add_req_transac(description, custid,accntid)
            return True
        else:
            return False

def update_creditacnt(custid,field,new_data,accntid=0):
    import transaction as txn
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    field = field.lower()
    if accntid == 0:
        if custid in get_allcustid():
            try:
                cur.execute(f'''UPDATE creditacnts SET {field} = '{new_data}' WHERE custid = '{custid}';''')
                conection.commit()
            except:
                cur.execute(f'''UPDATE creditacnts SET {field} = {new_data} WHERE custid = '{custid}';''')
                conection.commit()
            description = f"{field} of {custid} has been updated to {new_data}"
            txn.add_req_transac(description, custid)
            return True
        else:
            return False
    else:
        if custid in get_allcustid() and accntid in get_allaccntid():
            try:
                cur.execute(f'''UPDATE creditacnts SET {field} = '{new_data}' WHERE accntid = {accntid};''')
                conection.commit()
            except:
                cur.execute(f'''UPDATE creditacnts SET {field} = {new_data} WHERE accntid = {accntid};''')
                conection.commit()
            description = f"{field} of {accntid, custid} has been updated to {new_data}"
            txn.add_req_transac(description, custid, accntid)
            return True
        else:
            return False
def update_spouse_details(custid,field,new_data):
    import transaction as txn
    d = {"Spouse's Name":"name","Spouse's Aadhar":"aadhar", "Spouse's Occupation":"occupation", "Spouse's Income":"income"}
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    field = field.lower()
    if custid in get_allcustid():
        try:
            cur.execute(f'''UPDATE spouse_credit_cards SET {d[field]} = '{new_data}' WHERE custid = '{custid}';''')
            conection.commit()
        except:
            cur.execute(f'''UPDATE spouse_credit_cards SET {d[field]} = {new_data} WHERE custid = '{custid}';''')
            conection.commit()
        description = f"{field} of {custid} has been updated to {new_data}"
        txn.add_req_transac(description, custid)
        return True
    else:
        return False

def get_details_users(lis,custid):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    result = []
    for i in lis:
        j = i[0:len(i)-1]
        cur.execute(f'''SELECT {j.lower()} FROM users WHERE custid = '{custid}';''')
        output = cur.fetchall()
        result.append(str(output[0][0]))
    return result

# print(get_details_users(["Name:", "DOB:", "Email:", "Mobile:", "Address:", "Aadhar:"],'cstmr1'))

def get_details_credit(lis,custid):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    result = []
    for i in lis:
        j = i[0:len(i)-1]
        cur.execute(f'''SELECT {j.lower()} FROM creditacnts WHERE custid = '{custid}';''')
        output = cur.fetchall()
        result.append(str(output[0][0]))
    return result

def get_details_spouse(lis,custid):
    d = {"Spouse's Name": "name", "Spouse's Aadhar": "aadhar", "Spouse's Occupation": "occupation",
         "Spouse's Income": "income","Credit Card" : "cardno"}
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute('''SELECT custid FROM spouse_credit_cards;''')
    out = cur.fetchall()
    c = []
    for k in out:
        for l in k:
            c.append(l)
    result = []
    if custid in c:
        for i in lis:
            j = i[0:len(i)-1]
            cur.execute(f'''SELECT {j.lower()} FROM spouse_credit_cards WHERE custid = '{custid}';''')
            output = cur.fetchall()
            result.append(str(output[0][0]))
    else:
        for i in lis:
            j = i[0:len(i) - 1]
            cur.execute(f'''SELECT {j.lower()} FROM card_applications WHERE custid = '{custid}';''')
            output = cur.fetchall()
            result.append(str(output[0][0]))

    return result
def get_details_accounts(lis,custid):
    import cardlog as cl
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    accounts = getno_of_acnts(custid)
    result = []
    for i in accounts:
        sub_result = []
        for j in lis:
            j = j.lower()
            if j != 'cardno':
                if j == "type-status":
                    g = j.split('-')
                    cur.execute(f''' SELECT {g[1]} FROM users WHERE accntid = {i};''')
                    out1 = cur.fetchall()[0][0]
                    cur.execute(f''' SELECT {g[0]} FROM acnttype WHERE accntid = {i};''')
                    out = cur.fetchall()[0][0]
                    sub_result += [str(out)+'-'+str(out1)]
                else:
                    try:
                            cur.execute(f''' SELECT {j} FROM acntcard WHERE accntid = {i};''')
                            out = cur.fetchall()[0][0]
                            sub_result+= [str(out)]
                    except:
                            cur.execute(f''' SELECT {j} FROM acnttype WHERE accntid = {i};''')
                            out = cur.fetchall()[0][0]
                            sub_result += [str(out)]
            else:
                if cl.has_card(i):
                    cur.execute(f''' SELECT {j} FROM acntcard WHERE accntid = {i};''')
                    out = cur.fetchall()
                    output = ""
                    for i in out:
                        for j in i:
                            output += str(j)+'\n'+','
                    sub_result += [output]
                else:
                    sub_result+=['N/A']
        result.append(sub_result)
    return result

























    










