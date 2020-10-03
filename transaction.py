

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

def gen_tid(accntid,datetime,file="utids"):
    import cardlog as cl
    carddig = str(cl.get_cardno(accntid))[-1:-4:-1]
    utid = str(gen_utid(file))
    return 'txn'+utid+'.'+datetime+'.'+carddig[-1:-4:-1]

def withdraw(amount,cardno):
    import cardlog as cl
    accntid = cl.get_accntid(cardno)
    in_balance = cl.get_balance_card(cardno)
    fi_balance = in_balance - amount
    if fi_balance>0:
        cl.update_balance(cardno,fi_balance)
        description = f'{amount} withdrawn'
        details = add_history(accntid,description,cardno)
        return f"transaction successful,\nbalance={cl.get_balance_card(cardno)}\ntransaction id: {details[0]}\nunique transaction id{details[1]}"
    else:
        return f"Insufficient funds, balance={in_balance}"

def deposit(amount,cardno):
    import cardlog as cl
    accntid = cl.get_accntid(cardno)
    in_balance = cl.get_balance_card(cardno)
    fi_balance = in_balance + amount
    cl.update_balance(cardno, fi_balance)
    description = f'{amount} deposited'
    details = add_history(accntid,description,cardno)
    return f"transaction successful,\nbalance={cl.get_balance_card(cardno)}\ntransaction id: {details[0]}\nunique transaction id {details[1]}"

def transfer(amount,cardno_parent,cardno_child):
    import cardlog as cl
    parent = cl.get_accntid(cardno_parent)
    child = cl.get_accntid(cardno_child)
    bal1 = cl.get_balance_card(cardno_parent)
    bal2 = cl.get_balance_card(cardno_child)
    nbal1 = bal1-amount
    if nbal1>0:
        bal2 = bal2+amount
        cl.update_balance(cardno_parent,nbal1)
        cl.update_balance(cardno_child,bal2)
        description = f'{amount} transfered from {parent} to {child}'
        details = add_history(parent,description,cardno_parent)
        description = f'{amount} transfered to account from {parent}'
        add_history(child,description,cardno_child)
        return f"transaction successful.\nBalance = {nbal1}\ntransaction id: {details[0]}\nunique transaction id: {details[1]}"
    else:
        return f"insufficient funds. Balance = {bal1}"

def add_history(accntid,description,cardno):
    import accounts as acnt
    import datetime as dt
    dame = str(dt.datetime.today())
    lis = dame.split()
    dateime = lis[0]+'.'+lis[-1]
    connection = acnt.establish_connection("localhost","root","vishal26","bank")
    cur = connection.cursor()
    utid = int(gen_utid())
    tid = gen_tid(accntid,dateime)
    details = [tid,utid]
    cur.execute(f'''INSERT INTO transactionlog VALUES
    ('{tid}',{utid},'{lis[0]}','{lis[-1]}','{description}',{cardno});
    ''')
    connection.commit()
    return details

def get_history(tid):
    import accounts as acnt
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
    import accounts as acnt
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
        return final
    except:
        final = [['NA','NA','NA','No transaction made till date']]
        return final













