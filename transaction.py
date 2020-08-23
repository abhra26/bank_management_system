

def gen_utid(file):
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
        return num


def gen_tid(accntid,date,time,file="utids"):
    import cardlog as cl
    carddig = str(cl.get_cardno(accntid))[-1:-4:-1]
    utid = str(gen_utid(file))
    return 'txn'+utid+date+time+carddig

def withdraw(amount,accntid):
    import cardlog as cl
    in_balance = cl.get_balance(accntid)
    fi_balance = in_balance - amount
    if fi_balance>0:
        cl.update_balance(cl.get_cardno(accntid),fi_balance)
        return f"transaction successful, balance={cl.get_balance(accntid)}"
    else:
        return f"Insufficient funds, balance={in_balance}"

def deposit(amount,accntid):
    import cardlog as cl
    in_balance = cl.get_balance(accntid)
    fi_balance = in_balance + amount
    cl.update_balance(cl.get_cardno(accntid), fi_balance)
    return f"transaction successful, balance={cl.get_balance(accntid)}"

# print(deposit(1000,2))

def transfer(amount,parent,child):
    import cardlog as cl
    bal1 = cl.get_balance(parent)
    bal2 = cl.get_balance(child)
    nbal1 = bal1-amount
    if nbal1>0:
        bal2 = bal2+nbal1
        cl.update_balance(cl.get_cardno(parent),nbal1)
        cl.update_balance(cl.get_cardno(child),bal2)
        return f"transaction successful. Balance = {nbal1}"
    else:
        return f"insufficient funds. Balance = {bal1}"






