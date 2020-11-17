
def addto_acntcard(accntid,cardno,type):
    '''The function adds data to acntcard table of database bank'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' INSERT INTO acntcard VALUES
    ({accntid},{cardno},'{type}');''')
    con1.commit()

def generate_creditcard(company):
    '''The function generates and returns a creditcard'''
    from User_functions import accounts as acnt
    from User_functions.card_function import card_no_gen as cg
    con2 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur2 = con2.cursor()
    cur2.execute('''SELECT cardno FROM cardlog;''')
    out = cur2.fetchall()
    cards = []
    for i in out:
        for j in i:
            cards.append(j)
    new_cardno = cg.generate_card(company,cards)
    cvv = cg.cvv()
    expiry = cg.expiry()
    return [new_cardno,cvv,expiry]



def addto_cardlog(cardno,cvv,expirydate,company,pin,balance=200000,status="open",cardlimit=200000):
    '''The function adds data to cardlog table of database bank'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur1 = con1.cursor()
    cur1.execute(f'''INSERT INTO cardlog VALUES
    ({cardno},{cvv},'{status}','{expirydate}','{company}',{balance},{cardlimit},{pin});''')
    con1.commit()

def get_cardno(accntid):
    '''The function returns the cards of an account'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur1 = con1.cursor()
    cur1.execute(f' SELECT cardno FROM acntcard WHERE accntid = {accntid}')
    result = cur1.fetchall()
    final = []
    for i  in result:
        for j in i:
            final.append(j)
    return final

def get_balance(accntid):
    '''The function returns the balance of an account'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur1 = con1.cursor()
    cur1.execute(f'''SELECT cardno FROM acntcard WHERE accntid = {accntid}''')
    cardno = cur1.fetchall()[0][0]
    cur1.execute(f''' SELECT balance FROM cardlog WHERE cardno = {cardno}''')
    balance = cur1.fetchall()[0][0]
    return balance
def get_balance_card(cardno):
    '''The function returns the balance of a card'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' SELECT balance FROM cardlog WHERE cardno = {cardno};''')
    balance = cur1.fetchall()[0][0]
    return balance


def update_balance(cardno,amount):
    '''The function updates the balance of a card'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''UPDATE cardlog SET balance = {amount} WHERE cardno = {cardno}
    ''')
    con1.commit()

def check_details(card_number, expiry_date, cvv, card_type):
    '''The function checks the validity of the credentials entered during transaction'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''SELECT cardno,expirydate,cvv,company FROM cardlog
    WHERE cardno = {card_number};
        ''')
    result = list(cur1.fetchall()[0])
    c = 0
    data = [card_number,expiry_date,cvv,card_type]
    if result == data:
        # print(result)
        return True
    else:
        # print(result)
        return False

def get_accntid(cardno):
    '''The function returns the account id linked to a card'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''SELECT accntid FROM acntcard
    WHERE cardno = {cardno};
           ''')
    result = cur1.fetchall()[0][0]
    return result

def get_limit(cardno):
    '''The function returns the limit of a card'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' SELECT cardlimit FROM cardlog WHERE cardno = {cardno}''')
    cardlimit = cur1.fetchall()[0][0]
    return cardlimit
def get_card_status(cardno):
    '''The function returns the card status(block/open) of a card'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' SELECT status FROM cardlog WHERE cardno = {cardno}''')
    status = cur1.fetchall()[0][0]
    return status
def has_card(acntid):
    '''The function returns whether a account has a card or not'''
    from User_functions import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''SELECT cardno FROM acntcard WHERE accntid = {acntid}''')
    result = cur1.fetchall()
    if len(result) == 0:
        return False
    else:
        return True
def block_card(custid,accntid,cardno):
    '''The function blocks a card'''
    from User_functions import accounts as acnt
    from User_functions import transaction as txn
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''UPDATE cardlog SET status = "blocked" WHERE cardno = {cardno}''')
    description = f'Card blocked due to security reasons'
    txn.add_req_transac(description,custid,accntid,cardno)
    con1.commit()

def get_allcards():
    '''The function returns all cards in database bank'''
    from User_functions import accounts as acnt
    connection = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = connection.cursor()
    cur.execute('''SELECT cardno FROM acntcard;
    ''')
    result = cur.fetchall()
    lis = []
    for i in result:
        for j in i:
            lis.append(j)
    return lis


def card_request(custid,accntid,visa_master,type_card,spouse = "no"):
    '''The function add and returns request id regarding card application'''
    from admin_functions import request_admin as r
    if spouse == "no":
        request = f"Application submitted for {type_card} card on account(id):{accntid},card company:{visa_master}"
        reqid = r.add_request(custid,request,"card_application",accntid)
    else:
        request = f"Application submitted for {type_card} card,for spouse too, on account(id):{accntid},card company:{visa_master}."
        reqid = r.add_request(custid,request,"card_application")
    return reqid
























