

def gen_utid(file = 'utids'):
    import random
    fl = open(file,'r+')
    utids = fl.read()
    num = random.randint(100,999)
    if str(num) in utids or str(num)+'\n' in utids:
        fl.close()
        gen_utid(file)
    else:
        fl.write(str(num)+'\n')
        fl.close()
        return str(num)

def gen_tid(cardno,datetime,file="utids"):
    carddig = str(cardno)[-1:-4:-1]
    utid = str(gen_utid(file))
    return 'txn'+utid+'.'+datetime+'.'+carddig[-1:-4:-1]
# print(gen_tid(5412088017153251,"2020-10-3.12.00.00.00"))



def withdraw(amount,cardno):
    from User_functions.card_function import cardlog as cl
    from User_functions.emailserver import otp_email_sender_yagmail as email
    from User_functions import accounts as acnt
    accntid = cl.get_accntid(cardno)
    cards = cl.get_cardno(accntid)
    cards.remove(cardno)
    in_balance = cl.get_balance_card(cardno)
    fi_balance = in_balance - amount
    if fi_balance>0:
        cl.update_balance(cardno,fi_balance)
        description = f'{amount} withdrawn'
        details = add_history(description,cardno)
        email.transacttion_mail(acnt.get_email(cardno),accntid,details[0],cardno,amount,"withdrawn")
        if len(cards) !=0:
            for card in cards:
                cl.update_balance(card,fi_balance)
        return f"transaction successful,\nbalance={cl.get_balance_card(cardno)}\ntransaction id: {details[0]}\nunique transaction id{details[1]}"
    else:
        return f"Insufficient funds, balance={in_balance}"

def deposit(amount,cardno):
    from User_functions.card_function import cardlog as cl
    from User_functions.emailserver import otp_email_sender_yagmail as email
    from User_functions import accounts as acnt
    accntid = cl.get_accntid(cardno)
    cards = cl.get_cardno(accntid)
    cards.remove(cardno)
    in_balance = cl.get_balance_card(cardno)
    fi_balance = in_balance + amount
    cl.update_balance(cardno, fi_balance)
    description = f'{amount} deposited'
    details = add_history(description,cardno)
    email.transacttion_mail(acnt.get_email(cardno), accntid, details[0],cardno,amount,"deposited")
    if len(cards) != 0:
        for card in cards:
            cl.update_balance(card,fi_balance)
    return f"transaction successful,\nbalance={cl.get_balance_card(cardno)}\ntransaction id: {details[0]}\nunique transaction id {details[1]}"

def transfer(amount,cardno_parent,child):
    from User_functions.card_function import cardlog as cl
    from User_functions.emailserver import otp_email_sender_yagmail as email
    from User_functions import accounts as acnt
    parent = cl.get_accntid(cardno_parent)
    cards_p = cl.get_cardno(parent)
    cards_p.remove(cardno_parent)
    cardno_child = cl.get_cardno(child)
    bal1 = cl.get_balance_card(cardno_parent)
    bal2 = cl.get_balance_card(cardno_child)
    nbal1 = bal1-amount
    if nbal1>0:
        bal2 = bal2+amount
        if len(cards_p) != 0:
            for card in cards_p:
                cl.update_balance(card,nbal1)
        cl.update_balance(cardno_parent,nbal1)
        for card in cardno_child:
            cl.update_balance(card,bal2)
        description = f'{amount} transfered from {parent} to {child}'
        details = add_history(description,cardno_parent)
        description = f'{amount} transfered to account from {parent}'
        add_history(description,cardno_child[0])
        email.transacttion_mail(acnt.get_email(cardno_parent), parent, details[0],cardno_parent,amount,"transfered",child)
        return f"transaction successful.\nBalance = {nbal1}\ntransaction id: {details[0]}\nunique transaction id: {details[1]}"
    else:
        return f"insufficient funds. Balance = {bal1}"

def add_history(description,cardno):
    from User_functions import accounts as acnt
    import datetime as dt
    dame = str(dt.datetime.today())
    lis = dame.split()
    dateime = lis[0]+'.'+lis[-1]
    connection = acnt.establish_connection("localhost","root","vishal26","bank")
    cur = connection.cursor()
    utid = int(gen_utid())
    tid = gen_tid(cardno,dateime)
    details = [tid,utid]
    cur.execute(f'''INSERT INTO transactionlog VALUES
    ('{tid}',{utid},'{lis[0]}','{lis[-1]}','{description}',{cardno});
    ''')
    connection.commit()
    return details

def get_history(tid):
    from User_functions import accounts as acnt
    connection = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connection.cursor()
    try:
        cur.execute(f'''SELECT description,'on',date,'at',time FROM transactionlog
        WHERE tid = '{tid}';
        ''')
        out = cur.fetchall()[0]
        fin = ''
        for i in range(len(out)):
            fin += out[i]+' '

        return fin
    except:
        return f'{tid} is an invalid transaction id'

# print(get_history('txn883.2020-09-09.19:33:34.451760.155'))

def ministatement(cardno):
    from User_functions import accounts as acnt
    connection = acnt.establish_connection('localhost','root','vishal26','bank')
    cur = connection.cursor()
    cur.execute(f'''SELECT tid,date,time,description FROM transactionlog
        WHERE cardno = {cardno}; 
        ''')
    result = cur.fetchall()
    final = []
    try:
        for i in result:
            final.append(list(i))
        final.reverse()
        return final[:15]
    except:
        final = [['NA','NA','NA','No transaction made till date']]
        return final

def gen_urid(file = 'urids'):
    import random
    fl = open(file,'r+')
    urids = fl.read()
    num = random.randint(100,999)
    if str(num) in urids or str(num)+'\n' in urids:
        fl.close()
        gen_urid(file)
    else:
        fl.write(str(num)+'\n')
        fl.close()
        return str(num)

def gen_rid(custid,accntid=0,file="urids"):
    import datetime as dt
    dame = str(dt.datetime.today())
    lis = dame.split()
    urid = gen_urid(file)
    dateime = lis[0] + '.' + lis[-1]
    return 'req' + urid + '.' + dateime + '.' + custid + '.' + str(accntid)

def add_req_transac(description,custid,accntid=0,cardno = 0):
    from User_functions import accounts as acnt
    import datetime as dt
    dame = str(dt.datetime.today())
    lis = dame.split()
    connection = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = connection.cursor()
    rid = gen_rid(custid,accntid)
    cur.execute(f'''INSERT INTO transactionlog VALUES
    ('{rid}',{int(rid[3:6])},'{lis[0]}','{lis[-1]}','{description}',{cardno});''')
    connection.commit()

def requeststatement(custid):
    from User_functions import accounts as acnt
    d = {}
    connection = acnt.establish_connection('localhost','root','vishal26','bank')
    cur = connection.cursor()
    cur.execute(f'''SELECT reqid,request FROM request
        WHERE custid = '{custid}' AND req_type = 'card_application'; 
        ''')
    result = cur.fetchall()
    try:
        for i in result:
            request = i[0] + ':' + ' ' + i[-1]
            d[request] = 0
    except:
        d = {'no card applications submitted':0}

    return d
def delete_request_requesttab(reqid):
    from User_functions import accounts as acnt
    connection = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = connection.cursor()
    cur.execute(f'''DELETE FROM request WHERE reqid = '{reqid}'; 
            ''')
    connection.commit()


# print(requeststatement('cstmr1'))












