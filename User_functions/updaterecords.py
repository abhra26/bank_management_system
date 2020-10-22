from User_functions import accounts as acnt


def update_usr_rec(acntid,field):
    connection = acnt.establish_connection('localhost','root','vishal26','bank')
    cur = connection.cursor()
    num_fields = ['mobile','zipcode','aadhar']
    if field in num_fields:
        data = int(input("enter new data:"))
        cur.execute(f'UPDATE users SET {field} = {data} WHERE accntid = {acntid}')
        connection.commit()
        return 'successfully updated data'

    else:
        data = input("enter new data:")
        cur.execute(f'UPDATE users SET {field} = "{data}" WHERE accntid = {acntid}')
        connection.commit()
        return 'successfully updated data'

def update_creditacnt_rec(acntid,field):
    connection = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = connection.cursor()
    txt_fields = ['business']
    if field in txt_fields:
        data = int(input("enter new data:"))
        cur.execute(f'UPDATE creditacnts SET {field} = "{data}" WHERE accntid = {acntid}')
        connection.commit()
        return 'successfully updated data'

    else:
        data = input("enter new data:")
        cur.execute(f'UPDATE creditacnts SET {field} = {data} WHERE accntid = {acntid}')
        connection.commit()
        return 'successfully updated data'






