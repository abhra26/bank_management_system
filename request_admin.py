import accounts as acnt
import transaction as txn

def add_request(custid,request,req_type,accntid = 0):
    connect = acnt.establish_connection("localhost","root","vishal26","bank")
    cur = connect.cursor()
    reqid = txn.gen_rid(custid,accntid)
    cur.execute(f'''INSERT INTO request VALUES
    ('{custid}','{request}','{req_type}','{reqid}');''')
    connect.commit()

def admin_pass(password):
    if password == "admin":
        return True
    else:
        return False
def get_request_others():
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
    connect = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connect.cursor()
    cur.execute(f'''SELECT reqid FROM request WHERE request = '{request}';''')
    return cur.fetchall()[0][0]
def get_custid_req(request):
    connect = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connect.cursor()
    cur.execute(f'''SELECT custid FROM request WHERE request = '{request}';''')
    return cur.fetchall()[0][0]

def delete_request(request):
    connect = acnt.establish_connection("localhost", "root", "vishal26", "bank")
    cur = connect.cursor()
    cur.execute(f'''DELETE FROM request WHERE request = '{request}';''')
    connect.commit()
    return True



