# import accounts as acnt
# import sys
#
# con1 = acnt.establish_connection('localhost','root','vishal26','bank')
# con2 = acnt.establish_connection('localhost','root','vishal26','cards')
# cur1 = con1.cursor()
# cur2 = con2.cursor()

def addto_acntcard(accntid,cardno,type):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' INSERT INTO acntcard VALUES
    ({accntid},{cardno},'{type}');''')
    con1.commit()

def generate_creditcard(company,rannum):
    import accounts as acnt
    con2 = acnt.establish_connection('localhost','root','vishal26','cards')
    cur2 = con2.cursor()
    cur2.execute(f"SELECT startnum FROM creditcards WHERE cardname = '{company}';")
    startnum = cur2.fetchall()[0][0]
    cardno = startnum + rannum
    return [cardno,company]

def addto_cardlog(cardno,cvv,status,expirydate,company,balance,cardlimit):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur1 = con1.cursor()
    cur1.execute(f'''INSERT INTO cardlog VALUES
    ({cardno},{cvv},'{status}','{expirydate}','{company}',{balance},{cardlimit});''')
    con1.commit()

def get_cardno(accntid):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur1 = con1.cursor()
    cur1.execute(f' SELECT cardno FROM acntcard WHERE accntid = {accntid}')
    return cur1.fetchall()[0][0]

def get_balance(accntid):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur1 = con1.cursor()
    cur1.execute(f'SELECT cardno FROM acntcard WHERE accntid={accntid}')
    cardno = cur1.fetchall()[0][0]
    cur1.execute(f''' SELECT balance FROM cardlog WHERE cardno = {cardno}''')
    balance = cur1.fetchall()[0][0]
    return balance

def update_balance(cardno,amount):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''UPDATE cardlog SET balance = {amount} WHERE cardno = {cardno}
    ''')
    con1.commit()













