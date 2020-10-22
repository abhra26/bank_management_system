import yagmail, random

def otp_mail(receiver_email):
    n=str(random.randint(10000,99999))
    s=''
    for i in n:
        s=s+i+"\u0332"
    sender_email= "testdevelop12@gmail.com"
    subject="Verification code"
    password="good_work7"
    yag=yagmail.SMTP({sender_email:"Continental Bank"},password=password)
    contents=f"Respected Customer,\n\nYour otp verification code for your transaction process is {s}.\nPlease do not share this code with anyone.\nHave a great day.\nThank You for choosing Continental Bank.\n\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email,subject,contents)
    return int(n)


# otp_mail("kunj7dgupta@gmail.com")

def register_mail(receiver_email,custid,accntid):
    sender_email= "testdevelop12@gmail.com"
    subject="New service"
    password="good_work7"
    yag=yagmail.SMTP({sender_email:"Continental Bank"},password=password)
    contents=f"Respected Customer,\n\nYour registration was successful.\nThe customer id to your new service is {custid},\nYour accountid is {accntid}.\nPlease do not share these details with anyone.\nHave a great day.\nThank You for choosing Continental Bank.\n\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email,subject,contents)

# register_mail("saikatsahoo1402@yahoo.co.in","cstmr1",1)

def transacttion_mail(receiver_email,accntid,tid,prim_cardno,ammount,mode,sec_accnt = "N/A"):
    import datetime as dt
    from User_functions.card_function import cardlog as cl
    dame = str(dt.datetime.today())
    lis = dame.split()
    sender_email= "testdevelop12@gmail.com"
    subject="Transaction made"
    password="good_work7"
    yag=yagmail.SMTP({sender_email:"Continental Bank"},password=password)
    prim_cardno = str(prim_cardno)
    digits = prim_cardno[len(prim_cardno)-3:]
    balance = cl.get_balance_card(prim_cardno)
    if mode == "transfered":
        contents=f"Respected Customer,\n\nYour A/C {accntid} was accessed for carrying out a transaction.\nRs.{ammount} was {mode} from card {digits} to A/C {sec_accnt} on {lis[0]} at {lis[1]}.\nLimit available = Rs.{balance}.\nYour transaction id is {tid}.\nHave a great day.\nThank You for choosing Continental Bank.\n\nRegards,\nCustomer Care\nContinental Bank"
    else:
        contents = f"Respected Customer,\n\nYour A/C {accntid} was accessed for carrying out a transaction.\nRs.{ammount} was {mode} from card {digits} on {lis[0]} at {lis[1]}.\nLimit available = Rs.{balance}.\nYour transaction id is {tid}.\nHave a great day.\nThank You for choosing Continental Bank.\n\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email,subject,contents)


# transacttion_mail("abhraneel2003@gmail.com",1,"txn956.2020-10-01.15:34:17.545006.251",5412088017153251,5000,"withdrawn")

def status_email(receiver_email,object,cardno = 0):
    sender_email = "testdevelop12@gmail.com"
    subject = "Transaction made"
    password = "good_work7"
    yag = yagmail.SMTP({sender_email: "Continental Bank"}, password=password)
    if cardno == 0:
        contents = f"Respected Customer,\n\nSUSPICIOUS ACTIVITY has been noticed on your {object.upper()},due to which it has been BLOCKED(vide:Security Policy).\nPlease contact customer care for detailed information\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"
    else:
        cardno = str(cardno)
        digits = cardno[len(cardno)-3:]
        contents = f"Respected Customer,\n\nSUSPICIOUS ACTIVITY has been noticed on your {object.upper()}:{digits},due to which it has been BLOCKED(vide:Security Policy).\nPlease contact customer care for detailed information\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email, subject, contents)
# status_email("abhraneel2003@gmail.com","card",5412088017153251)
def request_complete_email(receiver_email,req,desc):
    from admin_functions import request_admin as r
    reqid = r.get_request_id(req)
    sender_email = "testdevelop12@gmail.com"
    subject = "Response to your Request"
    password = "good_work7"
    yag = yagmail.SMTP({sender_email: "Continental Bank"}, password=password)
    contents = f"Respected Customer,\n\nResponding to your request placed vide:{reqid},\n{desc}.\nPlease contact customer care for more details,if required.\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email, subject, contents)

def request_complete_email_card(receiver_email,reqid,desc):
    sender_email = "testdevelop12@gmail.com"
    subject = "Response to your Request"
    password = "good_work7"
    yag = yagmail.SMTP({sender_email: "Continental Bank"}, password=password)
    contents = f"Respected Customer,\n\nResponding to your request placed vide:{reqid},\n{desc}.\nPlease contact customer care for more details,if required.\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email, subject, contents)

def general_mail(receiver_email,contents):
    sender_email = "testdevelop12@gmail.com"
    subject = " "
    password = "good_work7"
    yag = yagmail.SMTP({sender_email: "Continental Bank"}, password=password)
    contents = f'Respected Customer,\n{contents}.\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"'
    yag.send(receiver_email, subject, contents)

def card_application_mail(receiver_email,custid,accntid,requestid):
    sender_email = "testdevelop12@gmail.com"
    subject = "Card application submitted"
    password = "good_work7"
    yag = yagmail.SMTP({sender_email: "Continental Bank"}, password=password)
    contents = f"Your application for a new card on:-\ncustomer id: {custid},accntid:{accntid}\nhas been succesfully submitted.\nYour resquest id is:{requestid}.Please keep this id for further use.\nHave a great day."
    contents = f'Respected Customer,\n{contents}.\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"'
    yag.send(receiver_email, subject, contents)

def card_assign_mail(receiver_email,cardno,accntid,custid,cvv,expiry,balance,pin,cardcom,cred_deb):
    sender_email = "testdevelop12@gmail.com"
    subject = f"new transaction card"
    password = "good_work7"
    yag = yagmail.SMTP({sender_email: "Continental Bank"}, password=password)
    pin = 'XX'+str(pin)[2:]
    contents = f"Your application for a new card on:-\ncustomer id: {custid},accntid:{accntid} has been approved.\nThe details of your card are as below\nCardno: {cardno}\nCVV: {cvv}\nExpires on: {expiry}\nCompany-type: {cardcom}-{cred_deb}\nPin: {pin}\nLimit: {balance}.Please keep the details for further use.\nDo not share with any other external agencies or entities.\nHave a great day."
    contents = f'Respected Customer,\n{contents}.\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"'
    yag.send(receiver_email, subject, contents)




'''Instruction:
1)To use yagmail module u need to install it:
type "pip install yagmail" in your command prompt
2)Need an active internet connection to run this program'''