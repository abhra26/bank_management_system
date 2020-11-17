from User_functions import transaction as txn, accounts as acnt


def add_request(custid,request,req_type,accntid = 0):
    '''The function adds a request to the request table'''
    connect = acnt.establish_connection("localhost","root","vishal26","bank")
    cur = connect.cursor()
    reqid = txn.gen_rid(custid,accntid)
    cur.execute(f'''INSERT INTO request VALUES
    ('{custid}','{request}','{req_type}','{reqid}');''')
    connect.commit()
    return reqid

def admin_pass(password):
    '''The function helps in authentication during login'''
    if password == "admin":
        return True
    else:
        return False
def get_request_others():
    '''The function returns some general requests placed by customers'''
    connect = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connect.cursor()
    result =[]
    cur.execute(f'''SELECT request FROM request WHERE req_type = 'others';''')
    output = cur.fetchall()
    for i in output:
        for j in i:
            result.append(j)
    return result

def get_request_id(request):
    '''The function returns the request id of a request '''
    connect = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connect.cursor()
    cur.execute(f'''SELECT reqid FROM request WHERE request = '{request}';''')
    return cur.fetchall()[0][0]
def get_custid_req(request):
    '''The function returns the customer id linked with the request placed'''
    connect = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connect.cursor()
    cur.execute(f'''SELECT custid FROM request WHERE request = '{request}';''')
    return cur.fetchall()[0][0]

def delete_request(request):
    '''The function deletes the completed requests from the request table in database bank'''
    connect = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connect.cursor()
    cur.execute(f'''DELETE FROM request WHERE request = '{request}';''')
    connect.commit()
    return True



