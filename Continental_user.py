##IMPORTING MODULES

from tkinter import *
from PIL import ImageTk, Image
from User_functions import login as lg, signup as sg
import captcha_project as cp
from tkinter import messagebox
import sys
from User_functions.emailserver import otp_email_sender_yagmail as mail

ID_info = ""
ID_info_initial = []
volatile = 0
Password = 0
variable = "new_cust"
lis = []
accntid = 0
wrong_login = 0
wrong_credentials = 0
wrong_otp = 0
card_number_initial = []

def intro():
    global image_f
    global login_register
    login_register = Tk()
    login_register.title("The Continental")
    login_register.iconbitmap("Icon.ico")
    login_register.geometry("540x640")

    image = Image.open("Continental.png")
    image = image.resize((520, 100), Image.ANTIALIAS)
    image_f = ImageTk.PhotoImage(image)
    image_g = image_f
    logo = Label(login_register, image=image_g).grid(row=0, column=0, columnspan=3)

    Butt1 = Button(login_register, text="LOGIN", command=login_page, height=5, width=50, bg="#B4B4B4").grid(row=1,
                                                                                                            column=1)
    gap_a = Label(login_register, text="", height=3).grid(row=2, column=0)
    Butt2 = Button(login_register, text="REGISTER", command= lambda : account_selection(variable), height=5, width=50, bg="#B4B4B4").grid(
        row=3, column=1)
    gap_b = Label(login_register, text="", height=3).grid(row=4, column=0)
    Butt3 = Button(login_register, text="CUSTOMER CARE", command=cust_care_page, height=5, width=50, bg="#B4B4B4").grid(
        row=5, column=1)
    gap_c = Label(login_register, text="", height=3).grid(row=6, column=0)
    Butt4 = Button(login_register, text="EXIT", command=lambda: back(login_register), height=5, width=50,
                   bg="#B4B4B4").grid(row=7, column=1)

    login_register.mainloop()

def login_page():
    global image_f
    global ID
    global Pass
    global login_screen
    global volatile
    volatile = 0
    ID = StringVar()
    Pass = StringVar()
    login_screen = Toplevel()
    login_screen.title("The Continental")
    login_screen.iconbitmap("Icon.ico")
    login_screen.geometry("860x550")

    logo = Label(login_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(login_screen, text="Enter Login Details", padx=50, pady=50)
    frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Login Details

    label1 = Label(frame, font=("Calibri", 22), text="CustomerID: ").grid(row=0, column=0)
    label2 = Label(frame, font=("Calibri", 22), text="Password: ").grid(row=2, column=0)
    Gap1 = Label(frame, text=" ").grid(row=1, column=2)
    global entry1
    global entry2
    entry1 = Entry(frame, font=("Calibri", 22), textvariable=ID, width=35)
    entry1.grid(row=0, column=1)
    entry2 = Entry(frame, font=("Calibri", 22), textvariable=Pass, width=35, show="*")
    entry2.grid(row=2, column=1)

    Gap2 = Label(frame, text=" ").grid(row=3, column=2)
    Button_login = Button(frame, font=("Calibri", 22), text="Login", bg="#B4B4B4", command=login, width=15).grid(row=4,
                                                                                                                 column=1)
    Gap3 = Label(frame, text=" ").grid(row=5, column=2)

    Gap3 = Label(login_screen, text=" ").grid(row=1, column=2)

    Button_exit = Button(login_screen, text="Back", highlightbackground="#B4B4B4", command=lambda: back(login_screen)).grid(row=6,
                                                                                                           column=2,
                                                                                                           sticky=E)
def login():
    global ID_info
    global entry1
    global entry2
    global account_list
    from User_functions import accounts as acnt
    global login_screen
    global volatile
    global ID_info_initial
    ID_info = ID.get()
    ID_info_initial.append(ID_info)
    account_list = acnt.getno_of_acnts(ID_info)
    try:
        status = acnt.get_status_account(account_list[0])
        name = acnt.get_name(ID_info)
        if status == 'open':
            if check_login():
                message = messagebox.showinfo("LOGGED IN", f"Welcome {name}.", icon="info")
                if message == "ok":
                    login_register.destroy()
                    accounts()
            else:
                message = messagebox.showerror("ERROR!", "Login Unsuccessful. \nTry Again")
                if message == "ok":
                    entry2.delete(0, END)
        else:
            error = messagebox.showerror("ALERT!",
                                     f"Your customer id is {status}\n Please contact customer care for more details")
            if error == 'ok':
                sys.exit(0)
            else:
                pass
    except:
        message = messagebox.showerror("ERROR!", "Login Unsuccessful. \nTry Again")
        if message == 'ok':
            pass
        else:
            pass

def check_login():
    global ID_info
    global Password
    global wrong_login
    from User_functions import accounts as acnt
    global login_register
    global ID_info_initial
    ID_info = str(ID.get())
    Password = int(Pass.get())
    try:
        if lg.login(ID_info,Password):
            return True
        elif ID_info_initial[wrong_login]==ID_info:
            wrong_login+=1
            if wrong_login == 4:
                acnt.block_cust(ID_info)
                mail.status_email(acnt.get_email(custid=ID_info),'customer id')
                error = messagebox.showerror("ALERT!",
                            "You have entered the login details wrong 4 times\n YOUR ACCOUNT HAS BEEN BLOCKED\n Please contact customer care for more details")
                wrong_login = 0
                ID_info_initial = []

            else:
                return False
        else:
            wrong_login = 1
            return False
    except:
        return False

def account_selection(variable):
    global image_f
    global login_register
    global screen1

    screen1 = Toplevel()
    screen1.title("The Continental")
    screen1.iconbitmap("Icon.ico")
    screen1.geometry("530x455")

    image = Image.open("Continental.png")
    image = image.resize((520, 100), Image.ANTIALIAS)
    image_f = ImageTk.PhotoImage(image)
    logo = Label(screen1, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(screen1, text="Choose Account Type", padx=50, pady=50)
    frame.grid(row=1, column=0, padx=10, pady=10)

    global choice
    choice = StringVar()
    choice.set("CREDIT")

    Radiobutton(frame, text="CREDIT", font=("Calibri", 22), variable=choice, value="CREDIT").grid(row=1, column=1)
    Radiobutton(frame, text="DEBIT", font=("Calibri", 22), variable=choice, value="DEBIT").grid(row=2, column=1)
    Radiobutton(frame, text="SAVINGS", font=("Calibri", 22), variable=choice, value="SAVINGS").grid(row=3, column=1)
    Butt_next = Button(frame, text="NEXT", command=lambda: next_page(screen1), highlightbackground="#B4B4B4").grid(row=4, column=1)

    if variable == "logged_in":
        Butt_exit = Button(screen1, text="EXIT", command=lambda: back(account_screen), highlightbackground="#B4B4B4").grid(row=5,
                                                                                                          column=0,
                                                                                                          sticky=W)
        Butt_back = Button(screen1, text="BACK", command=lambda: back(screen1), highlightbackground="#B4B4B4").grid(row=5, column=0,
                                                                                                   sticky=E)
    else:
        Butt_exit = Button(screen1, text="EXIT", command=lambda: back(login_register), highlightbackground="#B4B4B4").grid(row=5,
                                                                                                          column=0,
                                                                                                          sticky=W)
        Butt_back = Button(screen1, text="BACK", command=lambda: back(screen1), highlightbackground="#B4B4B4").grid(row=5, column=0,
                                                                                                   sticky=E)
def credit_page_form():
    global image_f
    global incomeamt
    global business_address
    global ssno
    global profitpa
    global credit_screen

    incomeamt = IntVar()
    business_address = StringVar()
    ssno = IntVar()
    profitpa = IntVar()

    credit_screen = Toplevel()
    credit_screen.title("The Continental")
    credit_screen.iconbitmap("Icon.ico")
    credit_screen.geometry("850x630")

    logo = Label(credit_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(credit_screen, text="Enter The Necessary details for Credit Account", padx=50, pady=50)
    frame.grid(row=1, column=0, padx=10, pady=10)

    # Labels and Inputs

    label_income = Label(frame, font=("Calibri", 20), text="Income: RS.\n(Per Annum)", height=2).grid(row=0, column=0)
    label_businessaddress = Label(frame, font=("Calibri", 20), text="Business/Work Address: ", height=2).grid(row=1,
                                                                                                              column=0)
    label_socialsecno = Label(frame, font=("Calibri", 20), text="Social Security : \nNumber", height=2).grid(row=2,
                                                                                                             column=0)
    label_profitpa = Label(frame, font=("Calibri", 20), text="Profit  :  \n(Per Annum)", height=2).grid(row=3, column=0)

    input_income = Entry(frame, font=("Calibri", 18), textvariable=incomeamt, width=35)
    input_businessaddress = Entry(frame, font=("Calibri", 18), textvariable=business_address, width=35)
    input_socialsecno = Entry(frame, font=("Calibri", 18), textvariable=ssno, width=35)
    input_profitpa = Entry(frame, font=("Calibri", 18), textvariable=profitpa, width=35)

    # Grid System

    input_income.grid(row=0, column=1)
    input_income.delete(0, END)
    input_businessaddress.grid(row=1, column=1)
    input_socialsecno.grid(row=2, column=1)
    input_socialsecno.delete(0, END)
    input_profitpa.grid(row=3, column=1)
    input_profitpa.delete(0, END)

    button_eligibility = Button(frame, font=("Calibri", 22), text="Check Eligibility", highlightbackground="#B4B4B4",
                                command=lambda: check_eligible(credit_screen), width=15).grid(row=4, column=1)
    Butt_exit = Button(credit_screen, text="EXIT", command=lambda: back(login_register), highlightbackground="#B4B4B4").grid(row=5,column=0,sticky=W)

    Butt_back = Button(credit_screen, text="BACK", command=lambda: back(credit_screen), highlightbackground="#B4B4B4").grid(row=5,column=0,sticky=E)


def register_page():
    global image_f
    global f_name
    global l_name
    global bday
    global mailID
    global password
    global sex
    global number
    global ad
    global cityID
    global stateID
    global aadharID
    global pincode
    global register_screen


    f_name = StringVar()
    l_name = StringVar()
    bday = StringVar()
    mailID = StringVar()
    password = StringVar()

    sex = StringVar()
    sex.set("(Choose Gender)")

    number = IntVar()
    ad = StringVar()
    cityID = StringVar()
    stateID = StringVar()
    aadharID = IntVar()
    pincode = IntVar()

    li = ["Male", "Female", "other"]

    register_screen = Toplevel()
    register_screen.title("The Continental")
    register_screen.iconbitmap("Icon.ico")
    register_screen.geometry("820x720")

    logo = Label(register_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(register_screen, text="Enter Necessary Details to Register", padx=50, pady=50)
    frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Labels

    label_firstname = Label(frame, font=("Calibri", 18), text="First Name: ").grid(row=0, column=0)
    label_lastname = Label(frame, font=("Calibri", 18), text="Last Name: ").grid(row=1, column=0)
    label_dob = Label(frame, font=("Calibri", 18), text="DOB(YYYY-MM-DD): ").grid(row=2, column=0)
    label_email = Label(frame, font=("Calibri", 18), text="Email: ").grid(row=3, column=0)
    label_passwd = Label(frame, font=("Calibri", 18), text="Passwd: ").grid(row=4, column=0)
    label_gender = Label(frame, font=("Calibri", 18), text="Gender: ").grid(row=5, column=0)
    label_mobile = Label(frame, font=("Calibri", 18), text="Mobile: ").grid(row=6, column=0)
    label_address = Label(frame, font=("Calibri", 18), text="Address: ").grid(row=7, column=0)
    label_city = Label(frame, font=("Calibri", 18), text="City: ").grid(row=8, column=0)
    label_state = Label(frame, font=("Calibri", 18), text="State: ").grid(row=9, column=0)
    label_aadhar = Label(frame, font=("Calibri", 18), text="AadharID: ").grid(row=10, column=0)
    label_zipcode = Label(frame, font=("Calibri", 18), text="Zipcode: ").grid(row=11, column=0)

    # Input Fields

    input_firstname = Entry(frame, font=("Calibri", 18), textvariable=f_name, width=35)
    input_lastname = Entry(frame, font=("Calibri", 18), textvariable=l_name, width=35)
    input_dob = Entry(frame, font=("Calibri", 18), textvariable=bday, width=35)
    input_email = Entry(frame, font=("Calibri", 18), textvariable=mailID, width=35)
    input_passwd = Entry(frame, font=("Calibri", 18), textvariable=password, show="*", width=35)
    input_gender = OptionMenu(frame, sex, *li)
    input_mobile = Entry(frame, font=("Calibri", 18), textvariable=number, width=35)
    input_address = Entry(frame, font=("Calibri", 18), textvariable=ad, width=35)
    input_city = Entry(frame, font=("Calibri", 18), textvariable=cityID, width=35)
    input_state = Entry(frame, font=("Calibri", 18), textvariable=stateID, width=35)
    input_aadhar = Entry(frame, font=("Calibri", 18), textvariable=aadharID, width=35)
    input_zipcode = Entry(frame, font=("Calibri", 18), textvariable=pincode, width=35)

    # Gridding Input Fields

    input_firstname.grid(row=0, column=1)
    input_lastname.grid(row=1, column=1)
    input_dob.grid(row=2, column=1)
    input_email.grid(row=3, column=1)
    input_passwd.grid(row=4, column=1)
    input_gender.grid(row=5, column=1, sticky=W)
    input_mobile.grid(row=6, column=1)
    input_mobile.delete(0, END)
    input_address.grid(row=7, column=1)
    input_city.grid(row=8, column=1)
    input_state.grid(row=9, column=1)
    input_aadhar.grid(row=10, column=1)
    input_aadhar.delete(0, END)
    input_zipcode.grid(row=11, column=1)
    input_zipcode.delete(0, END)

    # Register Button

    Button_register = Button(frame, font=("Calibri", 22), text="Register", highlightbackground="#B4B4B4",
                             command=lambda: register(register_screen), width=15).grid(row=12, column=1)
    Gap4 = Label(register_screen, text=" ").grid(row=14, column=2)
    Button_back = Button(register_screen, text="Back", highlightbackground="#B4B4B4", command=lambda: back(register_screen)).grid(row=14,
                                                                                                                 column=2,
                                                                                                                 sticky=E)
    Button_exit = Button(register_screen, text="Exit", highlightbackground="#B4B4B4", command=lambda: back(login_register)).grid(row=14,
                                                                                                                column=0,
                                                                                                                sticky=W)
##REGISTRATION PROCESS AND CONFIRMATION

def register(screen):
    screen.destroy()
    captcha_page("register","na","na",screen)

def accounts():
    from User_functions import accounts as acnt
    global account_screen
    global ID_info
    account_screen = Tk()
    account_screen.title("The Continental")
    account_screen.iconbitmap("Icon.ico")
    account_list = acnt.getno_of_acnts(ID_info)

    n = len(account_list)
    n = n + 2
    image = Image.open("Continental.png")
    image = image.resize((520, 100), Image.ANTIALIAS)
    image_f = ImageTk.PhotoImage(image)

    logo = Label(account_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(account_screen, text="Select Account", padx=250, pady=50)
    frame.grid(row=1, column=0, padx=80, pady=20)

    for i in range(len(account_list)):
        status = acnt.get_status_account(int(account_list[i]))
        if status == "blocked":
            bg = "red"
        else:
            bg = "green"
        button_account = Button(frame, font=("Calibri", 14), text=str(account_list[i]), highlightbackground = bg,
                                command=lambda a=i: get_account(account_list[a]), width = 5,height = 2).grid(row=i, column=1, padx=10,
                                                                                       pady=10)
    if len(account_list) < 10:
        button_add_ac = Button(frame, font=("Calibri", 8), text="Add Account", bg="#B4B4B4",
                               command=lambda: next_page(account_screen)).grid(row=n, column=1)

    button_exit = Button(account_screen, text="EXIT", bg="#B4B4B4", command=lambda: back(account_screen)).grid(
        row=n + 1, column=1, sticky=E, padx=10, pady=10)

    account_screen.mainloop()

def get_account(ac_no):
    global image_f
    global menu
    global accntid
    from User_functions import accounts as acnt
    accntid = ac_no
    status = acnt.get_status_account(accntid)

    if status == "blocked":
        message = messagebox.showerror("ALERT",f"Your account is currently {status}\n Please contact customer care for more details")
    else:
        account_screen.destroy()

        menu = Tk()
        menu.title("The Continental")
        menu.iconbitmap("Icon.ico")

        image = Image.open("Continental.png")
        image = image.resize((520, 100), Image.ANTIALIAS)
        image_f = ImageTk.PhotoImage(image)
        image_g = image_f
        logo = Label(menu, image=image_g).grid(row=0, column=0, columnspan=3)

        frame = LabelFrame(menu, text="Account Number: " + str(ac_no))
        frame.grid(row=1, column=0, padx=80, pady=20)

        button_deposit = Button(frame, font=("Calibri", 18), text="Deposit", bg="#B4B4B4",
                                command=lambda: deposit_withdraw_transfer(mode="deposit"), padx=76).grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=40,
                                                                                                         pady=40)
        button_mnstment = Button(frame, font=("Calibri", 18), text="Mini Statement", bg="#B4B4B4",
                                 command=lambda: statement_page(ac_no), padx=45).grid(row=0, column=1, padx=40, pady=40)
        button_withdraw = Button(frame, font=("Calibri", 18), text="Withdraw", bg="#B4B4B4",
                                 command=deposit_withdraw_transfer, padx=60).grid(row=1, column=0, padx=40, pady=40)
        button_transfer = Button(frame, font=("Calibri", 18), text="Transfer", bg="#B4B4B4",
                                 command=lambda: deposit_withdraw_transfer(mode="transfer"), padx=80).grid(row=1,
                                                                                                           column=1,
                                                                                                           padx=40,
                                                                                                           pady=40,
                                                                                                           columnspan=1)
        button_balance = Button(frame, font=("Calibri", 18), text="Check Balance", bg="#B4B4B4", command=lambda : balance_page(accntid),
                                padx=45).grid(row=2, column=0, columnspan=1, padx=40, pady=40)
        button_apply = Button(frame, font=("Calibri", 18), text="Apply For Card", bg="#B4B4B4",
                              command=lambda: card_type_page(ac_no), padx=45).grid(row=2, column=1, columnspan=1,
                                                                                   padx=40, pady=40)

        button_back = Button(menu, font=("Calibri", 10), text="Back", bg="#B4B4B4", command=lambda: back(menu)).grid(
            row=4, column=1, padx=20, pady=10, sticky=E)
        button_exit = Button(menu, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                             command=lambda: back(menu, value="exit")).grid(row=4, column=0, padx=20, pady=10, sticky=W)

        menu.mainloop()

def back(screen, value="back"):
    global credit_screen
    global register_screen
    global login_register
    global screen1
    global login_screen
    global menu
    global deposit_withdraw_transfer_page
    global statement_screen
    global card_type_screen
    global cust_care_screen
    global account_IDno
    global ID_info
    global captcha_screen
    global card_page
    global company_screen
    global card_typo

    if screen == credit_screen or screen == register_screen:
        warning = messagebox.askquestion("Confirm Form Resubmission!",
                                         "Turning back will take you to Account Selection Page!\n Do you wish to proceed ?")
        if warning == 'yes':
            account_selection(variable)
            screen.destroy()
        else:
            pass
    elif screen == login_register or screen == account_screen:
        warning = messagebox.askquestion("WARNING!", "Are you sure You want to Exit?")
        if warning == 'yes':
            screen.destroy()
        else:
            pass
    elif screen == screen1 or screen == login_screen or screen == deposit_withdraw_transfer_page or screen == statement_screen or screen == cust_care_screen or screen == card_type_screen:
        screen.destroy()

    elif screen == menu:
        if value == "exit":
            warning = messagebox.askquestion("WARNING!", "Are you sure You want to Exit?")
            if warning == 'yes':
                screen.destroy()
            else:
                pass
        else:
            screen.destroy()
            accounts()

    elif screen == amount_screen:
        warning = messagebox.askquestion("Confirm Form Resubmission!",
                                         "Turning back will take you to back to Menu!\n Do you wish to proceed ?")
        if warning == 'yes':
            screen.destroy()
        else:
            pass
    elif screen == company_screen:
        screen.destroy()
        card_type_page(account_IDno)
    elif screen == captcha_screen:
        if value == "register":
            warning = messagebox.askquestion("Confirm Form Resubmission!",
                                             "Turning back will take you to Account Selection Page!\n Do you wish to proceed ?")
            if warning == 'yes':
                account_selection(variable)
                screen.destroy()
            else:
                pass
        elif value == "card_application":
            screen.destroy()
            card_company(card_typo)

    elif screen == card_page:
        screen.destroy()
        card_type_page(account_IDno)

def deposit_withdraw_transfer(mode="withdraw"):
    global image_f
    global c_no
    global expiry
    global c_vv
    global typo
    global deposit_withdraw_transfer_page
    global entry_a
    global entry_b
    global entry_c
    global entry_d
    global receiver_ac
    global entry_receiver
    global accntid
    from User_functions.card_function import cardlog as cl

    if cl.has_card(accntid):
        c_no = IntVar()
        expiry = StringVar()
        c_vv = IntVar()
        li = ["MASTER", "VISA"]
        typo = StringVar()
        typo.set("(Choose Type)")
        receiver_ac = IntVar()

        deposit_withdraw_transfer_page = Toplevel()
        deposit_withdraw_transfer_page.title("The Continental")
        deposit_withdraw_transfer_page.iconbitmap("Icon.ico")
        deposit_withdraw_transfer_page.geometry("800x600")

        image = Image.open("Continental.png")
        image = image.resize((520, 100), Image.ANTIALIAS)
        image_f = ImageTk.PhotoImage(image)
        logo = Label(deposit_withdraw_transfer_page, image=image_f).grid(row=0, column=0, columnspan=3)

        frame = LabelFrame(deposit_withdraw_transfer_page, text=mode.upper())
        frame.grid(row=1, column=0, padx=80, pady=20)

        n = 0
        if mode == "transfer":
            n = 1
            label_receiver = Label(frame, font=("Calibri", 18), text="Receiver's Acc. ID: ").grid(row=0, column=0,
                                                                                                  pady=15,
                                                                                                  padx=50)
            entry_receiver = Entry(frame, font=("Calibri", 18), textvariable=receiver_ac, width=25)
            entry_receiver.grid(row=0, column=1, padx=50)
            entry_receiver.delete(0, END)

        label1 = Label(frame, font=("Calibri", 18), text="Card Number: ").grid(row=n, column=0, pady=15, padx=50)
        label2 = Label(frame, font=("Calibri", 18), text="Expiry Date: ").grid(row=n + 1, column=0, pady=15)
        label3 = Label(frame, font=("Calibri", 18), text="CVV: ").grid(row=n + 2, column=0, pady=15)
        label4 = Label(frame, font=("Calibri", 18), text="Type: ").grid(row=n + 3, column=0, pady=15)

        entry_a = Entry(frame, font=("Calibri", 18), textvariable=c_no, width=25)
        entry_a.delete(0, END)
        entry_b = Entry(frame, font=("Calibri", 18), textvariable=expiry, width=25)
        entry_c = Entry(frame, font=("Calibri", 18), textvariable=c_vv, show="*", width=25)
        entry_c.delete(0, END)
        entry_d = OptionMenu(frame, typo, *li)

        entry_a.grid(row=n, column=1, padx=50)
        entry_b.grid(row=n + 1, column=1)
        entry_c.grid(row=n + 2, column=1)
        entry_d.grid(row=n + 3, column=1)

        enter = Button(frame, font=("Calibri", 18), text="ENTER", command=lambda: check_card(mode), highlightbackground="#B4B4B4",
                       padx=35).grid(row=n + 4, column=1, pady=30, sticky=W)
        button_back = Button(deposit_withdraw_transfer_page, font=("Calibri", 10), text="Back", highlightbackground="#B4B4B4",
                             command=lambda: back(deposit_withdraw_transfer_page)).grid(row=n + 5, column=0, padx=50,
                                                                                        pady=10, sticky=E)
        button_exit = Button(deposit_withdraw_transfer_page, font=("Calibri", 10), text="Exit", highlightbackground="#B4B4B4",
                             command=lambda: back(menu, value="exit")).grid(row=n + 5, column=0, padx=20, pady=10,
                                                                            sticky=W)
    else:
        message = messagebox.showinfo("ERROR!","You do  not have a transaction card\nPlease do apply for one by contacting Customer Care")
        if message == "ok":
            pass

def amount_page(mode):
    global image_f
    global entry_amt
    global amount_screen
    global amt_value
    amt_value = IntVar()

    deposit_withdraw_transfer_page.destroy()

    amount_screen = Toplevel()
    amount_screen.title("The Continental")
    amount_screen.iconbitmap("Icon.ico")

    logo = Label(amount_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(amount_screen, text=mode.upper())
    frame.grid(row=1, column=0, padx=80, pady=20)

    label1 = Label(frame, font=("Calibri", 20), text="Enter Amount(in rupees): ").grid(row=0, column=0, pady=15,
                                                                                       padx=50, columnspan=3)
    entry_amt = Entry(frame, font=("Calibri", 18), textvariable=amt_value)
    entry_amt.grid(row=1, column=1, columnspan=3, sticky=W + E, padx=20, pady=10)
    entry_amt.delete(0, END)

    button_1 = Button(frame, font=("Calibri", 16), text="1", command=lambda: insert("1"), highlightbackground="#B4B4B4", padx=55,
                      pady=10).grid(row=2, column=1, pady=1, padx=1, columnspan=1)
    button_2 = Button(frame, font=("Calibri", 16), text="2", command=lambda: insert("2"), highlightbackground="#B4B4B4", padx=52,
                      pady=10).grid(row=2, column=2, pady=1, padx=1, columnspan=1)
    button_3 = Button(frame, font=("Calibri", 16), text="3", command=lambda: insert("3"), highlightbackground="#B4B4B4", padx=60,
                      pady=10).grid(row=2, column=3, pady=1, padx=1, columnspan=1)
    button_4 = Button(frame, font=("Calibri", 16), text="4", command=lambda: insert("4"), highlightbackground="#B4B4B4", padx=55,
                      pady=10).grid(row=3, column=1, pady=1, padx=1, columnspan=1)
    button_5 = Button(frame, font=("Calibri", 16), text="5", command=lambda: insert("5"), highlightbackground="#B4B4B4", padx=52,
                      pady=10).grid(row=3, column=2, pady=1, padx=1, columnspan=1)
    button_6 = Button(frame, font=("Calibri", 16), text="6", command=lambda: insert("6"), highlightbackground="#B4B4B4", padx=60,
                      pady=10).grid(row=3, column=3, pady=1, padx=1, columnspan=1)
    button_7 = Button(frame, font=("Calibri", 16), text="7", command=lambda: insert("7"), highlightbackground="#B4B4B4", padx=55,
                      pady=10).grid(row=4, column=1, pady=1, padx=1, columnspan=1)
    button_8 = Button(frame, font=("Calibri", 16), text="8", command=lambda: insert("8"), highlightbackground="#B4B4B4", padx=52,
                      pady=10).grid(row=4, column=2, pady=1, padx=1, columnspan=1)
    button_9 = Button(frame, font=("Calibri", 16), text="9", command=lambda: insert("9"), highlightbackground="#B4B4B4", padx=60,
                      pady=10).grid(row=4, column=3, pady=1, padx=1, columnspan=1)
    button_0 = Button(frame, font=("Calibri", 16), text="0", command=lambda: insert("0"), highlightbackground="#B4B4B4", padx=55,
                      pady=10).grid(row=5, column=1, pady=1, padx=1, columnspan=1)
    button_00 = Button(frame, font=("Calibri", 16), text="00", command=lambda: insert("00"), highlightbackground="#B4B4B4", padx=45,
                       pady=10).grid(row=5, column=2, pady=1, padx=1, columnspan=1)
    button_clear = Button(frame, font=("Calibri", 16), text="Clear", command=lambda: entry_amt.delete(0, END),
                          highlightbackground="#B4B4B4", padx=45, pady=10).grid(row=5, column=3, pady=1, padx=1, columnspan=1)

    enter = Button(frame, font=("Calibri", 18), text="ENTER", command=lambda: withdraw_or_deposit_value(mode),
                   highlightbackground="#B4B4B4", padx=35).grid(row=6, column=2, pady=30)
    button_back = Button(frame, font=("Calibri", 10), text="Back", highlightbackground="#B4B4B4",
                         command=lambda: back(amount_screen)).grid(row=7, column=0, padx=50, pady=20, sticky=E)
    button_exit = Button(frame, font=("Calibri", 10), text="Exit", highlightbackground="#B4B4B4",
                         command=lambda: back(menu, value="exit")).grid(row=7, column=4, padx=20, pady=20, sticky=W)

def insert(value):
    string = entry_amt.get()
    entry_amt.delete(0, END)
    entry_amt.insert(0, string + value)

def withdraw_or_deposit_value(mode):
    global c_no
    global expiry
    global c_vv
    global typo
    global amt_value
    global receiver_ac
    from User_functions.card_function import cardlog as cl

    card_number = int(c_no.get())  # int
    expiry_date = expiry.get()  # string
    cvv = int(c_vv.get())  # int
    if typo.get() in ['MASTER','master','Master']:
        card_type = 'mastercard'
    else:
        card_type = 'visa'
    amount = int(amt_value.get())  # int

    receiver_ac_id = 0
    if mode == "transfer":
        receiver_ac_id = receiver_ac.get()

    ##YOUR JOB
    cardlimit = cl.get_limit(card_number)
    status = cl.get_card_status(card_number)
    if status == "open":
        if amount>cardlimit:
            message = messagebox.showinfo("ALERT!",f"You are exceeding {mode} limit.\nYou can {mode} only till Rs.{cardlimit}\n Try again")
            if message == 'ok':
                amount_screen.destroy()
                amount_page(mode)
        else:
            question = messagebox.askquestion("ALERT!",
                                      "Your process to " + mode + " needs OTP Verification!\nDo you wish to proceed ?")
            if question == "yes":
                amount_screen.destroy()
                otp_page(amount, card_number,receiver_ac_id,mode)
            else:
                pass
    else:
        message = messagebox.showinfo("ALERT",f'Your card is {status}\nPlease contact admin for more details')
        if message == 'ok':
            amount_screen.destroy()
            # amount_page(mode)

def check_card(mode="withdraw"):
    global c_no
    global expiry
    global c_vv
    global typo
    global entry_a
    global entry_b
    global entry_c
    global typo
    global receiver_ac
    global entry_receiver
    from User_functions.card_function import cardlog as cl
    global menu
    global card_number_initial

    receiver_ac_id = 0
    if mode == "transfer":
        receiver_ac_id = receiver_ac.get()

    card_number = int(c_no.get())
    card_number_initial.append(card_number)
    status = cl.get_card_status(card_number)
    if status == 'blocked':
        error = messagebox.showinfo("ERROR!",f"Your card status is{status}\nPlease contact customer care for more details")


    else:
        expiry_date = str(expiry.get())
        cvv = int(c_vv.get())
        if typo.get() in ['VISA', 'visa', 'Visa']:
            card_type = "visa"
        else:
            card_type = "mastercard"

        output = confirm_card(card_number, expiry_date, cvv, card_type, receiver_ac_id)

        if output == True:
            success = messagebox.showinfo("SUCCESS!", "Your credentials have matched!\nClick OK to proceed")
            if success == "ok":
                deposit_withdraw_transfer_page.destroy()
                amount_page(mode)
        else:
            error = messagebox.showerror("ERROR!", "Your credentials did not match!\nTry Again")
            if error == "ok":
                entry_a.delete(0, END)
                entry_b.delete(0, END)
                entry_c.delete(0, END)
                if mode == "transfer":
                    entry_receiver.delete(0, END)
                typo.set("(Choose Type)")

def confirm_card(card_number, expiry_date, cvv, card_type,reciever_ac_id=0):
    from User_functions.card_function import cardlog as cl
    global wrong_credentials
    from User_functions import accounts as acnt
    global card_number_initial
    if cl.check_details(card_number,expiry_date,cvv,card_type):
        card_number_initial = []
        return True  # USE YOUR CONFIRMATION PROGRAM HERE
    else:
        if card_number_initial[wrong_credentials] == card_number:
            wrong_credentials+=1
            if wrong_credentials == 4:
                cl.block_card(ID_info,accntid,card_number)
                mail.status_email(acnt.get_email(card_number),"card",card_number)
                error = messagebox.showerror("ALERT!",
                                         "Your have entered the credentials wrong 4 times\nYOUR CARD IS BLOCKED\nPlease contact customer care for more details")
                wrong_credentials = 0
                card_number_initial = []
                if error == 'ok':
                    sys.exit(0)
        else:
            wrong_credentials = 1
            return False

def statement_page(ac_no):
    from User_functions import transaction as txn
    from User_functions.card_function import cardlog as cl
    global image_f
    global statement_screen

    lst = [["Transaction ID", "Date", "Time", "Action"]]


    if cl.has_card(accntid):
        cardno = cl.get_cardno(ac_no)

        lst2 = []
        for i in cardno:
            lst2+=txn.ministatement(i)
    else:
        lst2 = [['NA', 'NA', 'NA', 'No transaction made till date']]

    for i in range(len(lst2)):
        lst.append(lst2[i])

    total_rows = len(lst)
    total_columns = len(lst[0])

    statement_screen = Toplevel()
    statement_screen.title("The Continental")
    statement_screen.iconbitmap("Icon.ico")

    logo = Label(statement_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(statement_screen, text="MINI STATEMENT")
    frame.grid(row=1, column=0, padx=30, pady=20)

    label = Label(frame, text="     ").grid(row=0, column=0)
    for i in range(total_rows):
        for j in range(total_columns):
            tab = Entry(frame, width=35,
                        font=('Arial', 16, 'bold'))

            tab.grid(row=i + 1, column=j + 1)
            tab.insert(END, lst[i][j])
            tab.config(state="disabled")

    label = Label(frame, text="     ").grid(row=i + 2, column=j + 2)
    button_back = Button(statement_screen, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(statement_screen)).grid(row=i + 3, column=0, padx=50, pady=20, sticky=E)
    button_exit = Button(statement_screen, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(menu, value="exit")).grid(row=i + 3, column=0, padx=20, pady=20, sticky=W)


def otp_page(amount, card_number, receiver_ac_id, mode):
    global otp_screen
    global image_f
    from User_functions import accounts as acnt

    otp = mail.otp_mail(acnt.get_email(card_number))
    otp_screen = Toplevel()
    otp_screen.title("The Continental")
    otp_screen.iconbitmap("Icon.ico")

    logo = Label(otp_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(otp_screen, text="OTP VERIFICATION")
    frame.grid(row=1, column=0, padx=80, pady=20)

    otp_value = IntVar()

    label1 = Label(frame, font=("Calibri", 20), text="Enter Sent OTP: ").grid(row=0, column=0, pady=15, padx=50,
                                                                              columnspan=3)

    entry_otp = Entry(frame, font=("Calibri", 18), textvariable=otp_value)
    entry_otp.grid(row=1, column=0, padx=20, pady=10)
    entry_otp.delete(0, END)

    button_enter = Button(frame, font=("Calibri", 18), text="ENTER", highlightbackground="#B4B4B4",
                          command=lambda: check_otp(otp, otp_value.get(), amount, card_number, receiver_ac_id,
                                                    mode)).grid(row=2, column=0, padx=20, pady=50)

def check_otp(generated, entered, amount, card_number,reciever_ac_id, mode):
    from User_functions import transaction as txn
    if generated == entered:
        success = messagebox.showinfo("Success!",
                                      "OTP Verification Complete!\nYour Transaction is being processed.\nClick OK to return to confirm finally")
        if success == "ok":
            if mode == "withdraw":
                result = txn.withdraw(amount,card_number)
            elif mode == 'deposit':
                result = txn.deposit(amount,card_number)
            else:
                result = txn.transfer(amount,card_number,reciever_ac_id)

            success2 = messagebox.showinfo("success!",result)
            if success2 == "ok":
                otp_screen.destroy()
    else:
        error = messagebox.showerror("ERROR!", "OTP Verification Failed!\n Otp Did not match.\nPlease Try Again")
        otp_screen.destroy()

def balance_page(accntid):
    from User_functions.card_function import cardlog as cl
    try:
        balance = cl.get_balance(accntid)
        message = messagebox.showinfo("BALANCE",f"Your current balance is{balance}")
        if message == "ok":
            pass
        else:
            pass
    except:
        message = messagebox.showinfo("ERROR!",
                                      "You do  not have a transaction card\nPlease do apply for one by contacting Customer Care")
        if message == "ok":
            pass

def cust_care_page():
    global image_f
    global cust_care_screen

    cust_care_screen = Toplevel()
    cust_care_screen.title("The Continental")
    cust_care_screen.iconbitmap("Icon.ico")

    logo = Label(cust_care_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(cust_care_screen, text="REQUEST")
    frame.grid(row=1, column=0, padx=80, pady=20)

    request_type = StringVar()
    request_type.set("(Choose Type)")

    li = ["service status", "update records", "others"]

    label = Label(frame, font=("Calibri", 20), text="Enter your Customer ID: ").grid(row=0, column=0, pady=15, padx=50,
                                                                                     sticky=W)
    label = Label(frame, font=("Calibri", 20), text="Request Type: ").grid(row=1, column=0, columnspan=2, pady=15,
                                                                           padx=50, sticky=W)
    label = Label(frame, font=("Calibri", 20), text="Please type your report/complain here: ").grid(row=2, column=0,
                                                                                                    columnspan=2,
                                                                                                    pady=15, padx=50,
                                                                                                    sticky=W)

    entry_id = Entry(frame, font=("Calibri", 18), width=30)
    entry_id.grid(row=0, column=0, padx=20, pady=10, columnspan=2, sticky=E)

    entry_type = OptionMenu(frame, request_type, *li)
    entry_type.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

    text_field = Text(frame, font=("Calibri", 18), width=60, height=5)
    text_field.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    button_enter = Button(frame, font=("Calibri", 16), text="ENTER", bg="#B4B4B4",
                          command=lambda: process_request(entry_id.get(), text_field.get("1.0", "end-1c"),
                                                          request_type.get()), width=20).grid(row=3, column=0,
                                                                                              columnspan=1, padx=20,
                                                                                              pady=20, sticky=E)
    button_back = Button(frame, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(cust_care_screen)).grid(row=4, column=2, padx=20, pady=20, sticky=E)
    button_exit = Button(frame, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(login_register)).grid(row=4, column=0, padx=20, pady=20, sticky=W)


def process_request(cust_id, request, request_type):
    global cust_care_screen
    from admin_functions import request_admin as r
    print(cust_id, request, request_type)
    ##SAVE YOUR REQUEST FROM HERE
    r.add_request(cust_id,request,request_type)

    success = messagebox.showinfo("Success!", "Your Request/Complain has been recorded!\nClick OK to return to Menu")
    if success == "ok":
        cust_care_screen.destroy()

def card_type_page(ac_no):
    global image_f
    global menu
    global card_type_screen
    global account_IDno

    account_IDno = ac_no

    card_type_screen = Toplevel()
    card_type_screen.title("The Continental")
    card_type_screen.iconbitmap("Icon.ico")
    card_type_screen.geometry("530x455")

    logo = Label(card_type_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(card_type_screen, text="Choose Card Type", padx=50, pady=50)
    frame.grid(row=1, column=0, padx=110, pady=10)

    global card_type_choice
    card_type_choice = StringVar()
    card_type_choice.set("CREDIT")

    Radiobutton(frame, text="CREDIT", font=("Calibri", 22), variable=card_type_choice, value="CREDIT").grid(row=1,
                                                                                                            column=1)
    Radiobutton(frame, text="DEBIT", font=("Calibri", 22), variable=card_type_choice, value="DEBIT").grid(row=2,
                                                                                                          column=1)
    Butt_next = Button(frame, text="NEXT",
                       command=lambda: next_page(card_type_screen, card_type=card_type_choice.get()),
                       bg="#B4B4B4").grid(row=3, column=1)

    Butt_exit = Button(card_type_screen, text="EXIT", command=lambda: back(menu, value="exit"), bg="#B4B4B4").grid(
        row=4, column=0, sticky=W)
    Butt_back = Button(card_type_screen, text="BACK", command=lambda: back(card_type_screen), bg="#B4B4B4").grid(row=4,
                                                                                                                 column=0,
                                                                                                                 sticky=E)
def check_eligible(screen):
    import User_functions.signup as sg
    global incomeamt
    global business_address
    global ssno
    global profitpa

    ##YOUR VALUES TO ADD IN DATABSE AND CHECK ELIGILITY, YOUR WORK HERE

    income = int(incomeamt.get())  # int
    work_address = business_address.get()
    security_number = int(ssno.get()) # int
    profit = int(profitpa.get())  # int
    try:
        if sg.eligibility_credit(income):

            success = messagebox.showinfo("SUCCESS!","Good News!\n You are eligible for a credit account!\nClick Ok to go to next page")

            if success == "ok":
                screen.destroy()
                register_page()
        else:
            success = messagebox.showinfo("OOPS!",
                                       "You are not eligible for a credit account!\nClick Ok to go to previous page")
            if success == "ok":
                screen.destroy()
    except:
        error = messagebox.showerror("ERROE!","Please cheack if you have entered your details properly, or not.")
        if error == 'ok':
            pass
        else:
            pass

def next_page(screen, card_type="CREDIT"):
    if screen == screen1:
        global actype  ##THE VARIABLE FOR YOUR ACCOUNT TYPE USE THIS TO ADD TO SQL
        global choice
        actype = choice.get()
        if actype == "SAVINGS" or actype == "DEBIT":
            screen.destroy()
            register_page()
        else:
            screen.destroy()
            credit_page_form()

    elif screen == account_screen:
        global variable
        variable = "logged_in"
        account_selection(variable)

    elif screen == card_type_screen:
        if card_type == "CREDIT":
            screen.destroy()
            credit_card_application_form(card_type)
        else:
            screen.destroy()
            card_company(card_type)

def credit_card_application_form(card_type):
    global image_f
    global card_page
    global fn
    global ln
    global dob_wife
    global phone_wife
    global aadhar_wife
    global occupation
    global income_wife

    fn = StringVar()
    ln = StringVar()
    dob_wife = StringVar()
    phone_wife = StringVar()
    aadhar_wife = StringVar()
    occupation = StringVar()
    income_wife = StringVar()

    question_box = messagebox.askquestion("Option", "Would you like an additional card for your spouse ?")
    if question_box == "yes":

        card_page = Toplevel()
        card_page.title("The Continental")
        card_page.iconbitmap("Icon.ico")

        logo = Label(card_page, image=image_f).grid(row=0, column=0, columnspan=3)

        frame = LabelFrame(card_page, text="Fill in the Details", padx=50, pady=50)
        frame.grid(row=1, column=0, padx=110, pady=10)

        label_1 = Label(frame, font=("Calibri", 18), text="First Name: ").grid(row=0, column=0)
        label_2 = Label(frame, font=("Calibri", 18), text="Last Name: ").grid(row=1, column=0)
        label_3 = Label(frame, font=("Calibri", 18), text="DOB(YYYY-MM-DD): ").grid(row=2, column=0)
        label_4 = Label(frame, font=("Calibri", 18), text="Phone: ").grid(row=3, column=0)
        label_5 = Label(frame, font=("Calibri", 18), text="Aadhar ID: ").grid(row=4, column=0)
        label_6 = Label(frame, font=("Calibri", 18), text="Occupation: ").grid(row=5, column=0)
        label_7 = Label(frame, font=("Calibri", 18), text="Income: ").grid(row=6, column=0)

        f1 = Entry(frame, font=("Calibri", 18), textvariable=fn, width=35)
        f2 = Entry(frame, font=("Calibri", 18), textvariable=ln, width=35)
        f3 = Entry(frame, font=("Calibri", 18), textvariable=dob_wife, width=35)
        f4 = Entry(frame, font=("Calibri", 18), textvariable=phone_wife, width=35)
        f5 = Entry(frame, font=("Calibri", 18), textvariable=aadhar_wife, width=35)
        f6 = Entry(frame, font=("Calibri", 18), textvariable=occupation, width=35)
        f7 = Entry(frame, font=("Calibri", 18), textvariable=income_wife, width=35)

        f1.grid(row=0, column=1, pady=5)
        f2.grid(row=1, column=1, pady=5)
        f3.grid(row=2, column=1, pady=5)
        f4.grid(row=3, column=1, pady=5)
        f5.grid(row=4, column=1, pady=5)
        f6.grid(row=5, column=1, pady=5)
        f7.grid(row=6, column=1, pady=5)

        Button_enter = Button(frame, text="ENTER", font=("Calibri", 18), bg="#B4B4B4",
                              command= lambda : card_company_switch(card_type)).grid(row=7, column=1, pady=25)

        Button_back = Button(card_page, text="Back", bg="#B4B4B4", command=lambda: back(card_page)).grid(row=14,
                                                                                                         column=8,
                                                                                                         sticky=E,
                                                                                                         padx=50,
                                                                                                         pady=25)
        Button_exit = Button(card_page, text="Exit", bg="#B4B4B4", command=lambda: back(menu, value="exit")).grid(row=8,
                                                                                                                  column=0,
                                                                                                                  sticky=W,
                                                                                                                  padx=50,
                                                                                                                  pady=25)

    else:
        card_company(card_type)

def card_company_switch(card_type):
    card_page.destroy()
    card_company(card_type)

def card_company(card_type):
    global image_f
    global menu
    global company_screen
    global card_typo

    card_typo = card_type

    company_screen = Toplevel()
    company_screen.title("The Continental")
    company_screen.iconbitmap("Icon.ico")
    company_screen.geometry("530x455")

    logo = Label(company_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(company_screen, text="COMPANY", padx=50, pady=50)
    frame.grid(row=1, column=0, padx=110, pady=10)

    global visa_master
    visa_master = StringVar()
    visa_master.set("VISA")

    Radiobutton(frame, text="MASTERCARD", font=("Calibri", 22), variable=visa_master, value="MASTERCARD").grid(row=1,
                                                                                                               column=1)
    Radiobutton(frame, text="VISA", font=("Calibri", 22), variable=visa_master, value="VISA").grid(row=2, column=1)
    Butt_next = Button(frame, text="NEXT", command=lambda: store_cardtype(visa_master.get(), card_type),
                       bg="#B4B4B4").grid(row=3, column=1)

    Butt_exit = Button(company_screen, text="EXIT", command=lambda: back(menu, value="exit"), bg="#B4B4B4").grid(row=4,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
    Butt_back = Button(company_screen, text="BACK", command=lambda: back(company_screen), bg="#B4B4B4").grid(row=4,
                                                                                                             column=0,
                                                                                                             sticky=E)
def store_cardtype(card, card_type):
    global type_card
    global visa_master
    global company_screen
    type_card = card_type  ##VARIABLE FOR CARD TYPE TAKEN

    visa_master = card  ##VARIABLE FOR EITHER CREDIT OR DEBIT CARD
    print(card_type)
    print(card)
    company_screen.destroy()
    captcha_page("card_application",visa_master,type_card)

def captcha_page(form,visa_master,type_card,screen = 'NA'):
    global image_f
    global captcha_screen
    global image_cp
    global image_refresh

    captcha_screen = Toplevel()
    captcha_screen.title("The Continental")
    captcha_screen.iconbitmap("Icon.ico")

    logo = Label(captcha_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(captcha_screen, text="ROBOT VERIFICATION", padx=50, pady=50)
    frame.grid(row=1, column=0, padx=110, pady=10)

    captcha_code = cp.create_captcha()

    image_captcha = Image.open("pic.png")
    image_captcha = image_captcha.resize((300, 104), Image.ANTIALIAS)
    image_cp = ImageTk.PhotoImage(image_captcha)

    captcha_label = Label(frame, image=image_cp).grid(row=0, column=1, columnspan=2)

    label = Label(frame, font=("Calibri", 20), text="Enter: ").grid(row=1, column=0, padx=15)

    entry_code = Entry(frame, font=("Calibri", 18))
    entry_code.grid(row=1, column=1, columnspan=1)

    image_refresh = Image.open("refresh.png")
    image_refresh = ImageTk.PhotoImage(image_refresh)

    refresh_button = Button(frame, image=image_refresh, command=lambda: refresh_captcha(form,visa_master,type_card,screen), bg="#B4B4B4").grid(row=1,
                                                                                                                  column=2)

    Butt_enter = Button(frame, font=("Calibri", 16), text="ENTER",
                        command=lambda: check_captcha(form, captcha_code, entry_code.get(),visa_master,type_card,screen), bg="#B4B4B4").grid(row=3,
                                                                                                                column=1)

    Butt_back = Button(captcha_screen, text="BACK", command=lambda: back(captcha_screen, value=form),
                       bg="#B4B4B4").grid(row=4, column=0, sticky=E, padx=50, pady=25)
    print(captcha_code)

def refresh_captcha(form,visa_master,type_card,screen = 'NA'):
    global captcha_screen
    captcha_screen.destroy()
    captcha_page(form,visa_master,type_card,screen)

def check_captcha(form, gen_code, entry_code,visa_master,type_card,screen = 'NA'):
    from User_functions.card_function import cardlog as cl
    global ID_info
    import User_functions.emailserver.otp_email_sender_yagmail as mail
    from User_functions import accounts as acnt

    if gen_code == entry_code:
        if form == "register":
            global variable
            global choice
            global incomeamt
            global business_address
            global ssno
            global profitpa
            global f_name
            global l_name
            global bday
            global mailID
            global password
            global sex
            global number
            global ad
            global cityID
            global stateID
            global aadharID
            global pincode
            global ID_info
            global Password
            # global lis

            ##DATAS FOR DATABASE MANAGEMENT
            try:
                name = f_name.get() + " " + l_name.get()
                dob = bday.get()
                email = mailID.get()
                passwd = password.get()
                if sex.get() in ['male', 'Male']:
                    gender = 'M'
                elif sex.get() in ['female', 'Female']:
                    gender = 'F'
                else:
                    gender = 'O'
                mobile = number.get()  # int
                address = ad.get()
                city = cityID.get()
                state = stateID.get()
                aadhar = int(aadharID.get())  # int
                zipcode = int(pincode.get())  # int
                ##You use your function for SQL anywhere here
                if variable == "new_cust":
                    lis = sg.signup(name, dob, email, gender, mobile, address, city, state, aadhar, zipcode, passwd,
                                    variable, 'cstmr')
                else:
                    ID_info = ID.get()
                    Password = Pass.get()
                    lis = sg.signup(name, dob, email, gender, mobile, address, city, state, aadhar, zipcode, Password,
                                    variable, ID_info)
                acntype = choice.get()
                if acntype == "CREDIT":
                    income = int(incomeamt.get())  # int
                    work_address = business_address.get()
                    security_number = int(ssno.get())  # int
                    profit = int(profitpa.get())  # int
                    acnt.addto_creditacnts(lis[0], lis[1], work_address, income, profit, security_number,
                                           income + profit,
                                           0, 'NA')
                    acnt.addto_acnttype(lis[1], "Credit")

                elif acntype == "DEBIT":
                    acnt.addto_acnttype(lis[1], "Debit")
                else:
                    acnt.addto_acnttype(lis[1], "Savings")
                ##Last Lines
                mail.register_mail(str(email), lis[0], lis[1])
                success = messagebox.showinfo("SUCCESS!",
                                              f"Registration Successful! You can now Login \n Your Customer ID is {lis[0]} \n Your account id is {lis[1]}")
                if success == "ok":
                    screen.destroy()
                    captcha_screen.destroy()
            except:
                error = messagebox.showerror("ERROR 404!", "REGISTRATION FAILED")
                sys.exit(0)


        elif form == "card_application":
            if type_card == "DEBIT":
                reqid = cl.card_request(ID_info,accntid,visa_master,type_card)
                mail.card_application_mail(acnt.get_email(custid=ID_info),ID_info,accntid,reqid)
                success = messagebox.showinfo("Robot Verification Complete!", "Your card application has been submitted succesfully ! ")

                if success == "ok":
                    captcha_screen.destroy()
            else:
                global card_page
                global fn
                global ln
                global dob_wife
                global phone_wife
                global aadhar_wife
                global occupation
                global income_wife
                from User_functions import accounts as acnt

                try:
                    wife_name = fn.get() + " " + ln.get()
                    dob = dob_wife.get()  ##FOR THE TIME BEING I HAVE STORED THE VARIABLES OF THE WIFE HERE
                    phone = int(phone_wife.get())  ##YOU CAN MAKE THEM GLOBAL AND THEN USE THESE VARIABLES AFTER THE CAPTCHA VERIFICATION
                    aadhar = int(aadhar_wife.get())
                    job = occupation.get()
                    income = int(income_wife.get())
                    reqid = cl.card_request(ID_info, accntid, visa_master, type_card, "yes")
                    acnt.addto_spouse_credit_card_appl(ID_info, accntid, wife_name, dob, phone, aadhar, income,
                                                       type_card, visa_master, job)
                    mail.card_application_mail(acnt.get_email(custid=ID_info), ID_info, accntid, reqid)
                    success = messagebox.showinfo("Robot Verification Complete!",
                                                  "Your card application has been submitted succesfully ! ")

                    if success == "ok":
                        captcha_screen.destroy()
                except:
                    reqid = cl.card_request(ID_info, accntid, visa_master, type_card)
                    mail.card_application_mail(acnt.get_email(custid=ID_info), ID_info, accntid, reqid)
                    success = messagebox.showinfo("Robot Verification Complete!",
                                                  "Your card application has been submitted succesfully ! ")

                    if success == "ok":
                        captcha_screen.destroy()




    else:
        error = messagebox.showerror("Error!", "Invalid Captcha, Try again")
        refresh_captcha(form,visa_master,type_card,screen)


##FUNCTION EXECUTION
login_register = None
register_screen = None
credit_screen = None
screen1 = None
account_screen = None
menu = None
account_list = []
deposit_withdraw_transfer_page = None
amount_screen = None
statement_screen = None
cust_care_screen = None
card_type_screen = None
login_screen = None
captcha_screen = None
company_screen = None
card_page = None

intro()

