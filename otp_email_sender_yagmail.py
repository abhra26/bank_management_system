import yagmail, random

def otp(receiver_email):
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




'''Instruction:
1)To use yagmail module u need to install it:
type "pip install yagmail" in your command prompt
2)Need an active internet connection to run this program'''