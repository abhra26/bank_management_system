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
    contents=f"Respected Customer,\n\nYour customer id is {custid},\nYour accountid is {accntid}.\nPlease do not share these details with anyone.\nHave a great day.\nThank You for choosing Continental Bank.\n\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email,subject,contents)

# register_mail("kunj7dgupta@gmail.com","cstmr1",1)

def transacttion_mail(receiver_email,accntid,tid):
    import datetime as dt
    dame = str(dt.datetime.today())
    lis = dame.split()
    sender_email= "testdevelop12@gmail.com"
    subject="Transaction made"
    password="good_work7"
    yag=yagmail.SMTP({sender_email:"Continental Bank"},password=password)
    contents=f"Respected Customer,\n\nYour account {accntid} was accessed for carrying out a transaction on {lis[0]} at {lis[1]}.\nYour transaction id is {tid}.\nHave a great day.\nThank You for choosing Continental Bank.\n\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email,subject,contents)


# transacttion_mail("kunj7dgupta@gmail.com.com",1,"txn956.2020-10-01.15:34:17.545006.251","2020-10-03","20:00:00")

def status_email(receiver_email,object):
    sender_email = "testdevelop12@gmail.com"
    subject = "Transaction made"
    password = "good_work7"
    yag = yagmail.SMTP({sender_email: "Continental Bank"}, password=password)
    contents = f"Respected Customer,\n\nYour {object} has been blocked for security reasons.\nPlease contact customer care for more details\n\nThank you\nRegards,\nCustomer Care\nContinental Bank"
    yag.send(receiver_email, subject, contents)




'''Instruction:
1)To use yagmail module u need to install it:
type "pip install yagmail" in your command prompt
2)Need an active internet connection to run this program'''