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
    result = cur1.fetchall()
    final = []
    for i  in result:
        for j in i:
            final.append(j)
    return final

def get_balance(accntid):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost','root','vishal26','bank')
    cur1 = con1.cursor()
    cur1.execute(f'''SELECT cardno FROM acntcard WHERE accntid = {accntid}''')
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

def check_details(card_number, expiry_date, cvv, card_type):
    import accounts as acnt
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
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''SELECT accntid FROM acntcard
    WHERE cardno = {cardno};
           ''')
    result = cur1.fetchall()[0][0]
    return result



# print(check_details(5412088017153251,'13-10-2030',890,'mastercard'))

# print(get_accntid(5412088017153251))


def get_balance_card(cardno):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' SELECT balance FROM cardlog WHERE cardno = {cardno}''')
    balance = cur1.fetchall()[0][0]
    return balance
def get_limit(cardno):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' SELECT cardlimit FROM cardlog WHERE cardno = {cardno}''')
    cardlimit = cur1.fetchall()[0][0]
    return cardlimit
def get_card_status(cardno):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f''' SELECT status FROM cardlog WHERE cardno = {cardno}''')
    status = cur1.fetchall()[0][0]
    return status
def has_card(acntid):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''SELECT cardno FROM acntcard WHERE accntid = {acntid}''')
    result = cur1.fetchall()
    if len(result) == 0:
        return False
    else:
        return True
def block_card(cardno):
    import accounts as acnt
    con1 = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur1 = con1.cursor()
    cur1.execute(f'''UPDATE cardlog SET status = "blocked" WHERE cardno = {cardno}''')
    con1.commit()















