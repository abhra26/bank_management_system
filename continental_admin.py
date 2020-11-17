from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk



def admin_login():
    global image_f
    global login_page
    login_page = Tk()
    login_page.title("The Continental")
    login_page.iconbitmap("Icon.ico")

    image = Image.open("Continental.png")
    image = image.resize((520, 100), Image.ANTIALIAS)
    image_f = ImageTk.PhotoImage(image)
    image_g = image_f
    logo = Label(login_page, image=image_g).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(login_page, text="Admin's Page")
    frame.grid(row=1, column=0, padx=100, pady=50)

    gap = Label(frame, text="", height=3).grid(row=0, column=0)
    label_a = Label(frame, font=("Calibri", 22), text="Enter Password: ").grid(row=1, column=0, padx=50, pady=10)

    entry_pass = Entry(frame, font=("Calibri", 22), width=20, show="*")
    entry_pass.grid(row=2, column=0, padx=50, pady=20)

    Butt1 = Button(frame, text="ENTER", command=lambda: check_admin_login(entry_pass.get(), entry_pass), height=2,
                   width=15, bg="#B4B4B4").grid(row=3, column=0, pady=20)

    Butt2 = Button(frame, text="EXIT", command=lambda: back(login_page), height=2, width=15, bg="#B4B4B4").grid(row=4,
                                                                                                                column=0,
                                                                                                                pady=20)

    gap = Label(frame, text="", height=7).grid(row=5, column=0)

    login_page.mainloop()


def check_admin_login(password, entry):
    global login_page
    from admin_functions import request_admin as r

    if r.admin_pass(password):
        success = messagebox.showinfo("Logged In!", "Welcome Admin.")
        if success == "ok":
            login_page.destroy()
            home_page()

    else:
        error = messagebox.showerror("Error!", "Invalid Password.\nTry again.")
        if error == "ok":
            entry.delete(0, END)


def home_page():
    global image_f
    global home_screen

    home_screen = Tk()
    home_screen.title("The Continental")
    home_screen.iconbitmap("Icon.ico")

    image = Image.open("Continental.png")
    image = image.resize((520, 100), Image.ANTIALIAS)
    image_f = ImageTk.PhotoImage(image)
    image_g = image_f
    logo = Label(home_screen, image=image_g).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(home_screen, text="HOME")
    frame.grid(row=1, column=0, padx=80, pady=20)

    button_status = Button(frame, font=("Calibri", 18), text="Service Status", bg="#B4B4B4",
                           command=service_status_page, padx=76).grid(row=0, column=0, padx=40, pady=40)
    button_updatedata = Button(frame, font=("Calibri", 18), text="Update Records", bg="#B4B4B4",
                               command=update_records_page, padx=80).grid(row=0, column=1, padx=40, pady=40)
    button_cardapp = Button(frame, font=("Calibri", 18), text="Card Application", bg="#B4B4B4",
                            command=card_application_page, padx=60).grid(row=1, column=0, padx=40, pady=40)
    button_custdetails = Button(frame, font=("Calibri", 18), text="Customer Details", bg="#B4B4B4",
                                command=cust_details_page, padx=76).grid(row=1, column=1, padx=40, pady=40,
                                                                         columnspan=1)
    button_others = Button(frame, font=("Calibri", 18), text="Others", bg="#B4B4B4", command=others_page,
                           padx=120).grid(row=2, column=0, padx=40, pady=40, columnspan=1)
    button_email = Button(frame, font=("Calibri", 18), text="Email", bg="#B4B4B4", command=dm_cust, padx=120).grid(
        row=2, column=1, padx=40, pady=40, columnspan=1)
    button_assn = Button(frame, font=("Calibri", 18), text="Assign Card", bg="#B4B4B4", command=card_assn_page,
                         padx=80).grid(row=3, column=1, columnspan=1, padx=40, pady=40)

    button_history = Button(frame, font=("Calibri", 18), text="History", bg="#B4B4B4", command=history_page,
                            padx=120).grid(row=3, column=0, padx=40, pady=40, columnspan=1)

    button_back = Button(home_screen, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(home_screen)).grid(row=4, column=1, padx=20, pady=10, sticky=E)
    button_exit = Button(home_screen, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=4, column=0, padx=20, pady=10,
                                                                               sticky=W)

    home_screen.mainloop()


def service_status_page():
    global image_f
    global service_status_screen

    service_status_screen = Toplevel()
    service_status_screen.title("The Continental")
    service_status_screen.iconbitmap("Icon.ico")

    image = Image.open("Continental.png")
    image = image.resize((520, 100), Image.ANTIALIAS)
    image_f = ImageTk.PhotoImage(image)
    logo = Label(service_status_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(service_status_screen, text="SERVICE STATUS")
    frame.grid(row=1, column=0, padx=80, pady=20)

    label1 = Label(frame, font=("Calibri", 18), text="Cust ID: ").grid(row=0, column=0, pady=15, padx=50)
    label2 = Label(frame, font=("Calibri", 18), text="Account ID: ").grid(row=1, column=0, pady=15)

    entry_1 = Entry(frame, font=("Calibri", 18), width=25)
    entry_2 = Entry(frame, font=("Calibri", 18), width=25)

    entry_1.grid(row=0, column=1, padx=50)
    entry_2.grid(row=1, column=1)

    button_block = Button(frame, font=("Calibri", 16), text="Block", bg="#B4B4B4",
                          command=lambda: block_user(entry_1.get(), entry_2.get(), entry_1, entry_2)).grid(row=2,
                                                                                                           column=0,
                                                                                                           padx=50,
                                                                                                           pady=10,
                                                                                                           sticky=E)
    button_open = Button(frame, font=("Calibri", 16), text="Open", bg="#B4B4B4",
                         command=lambda: open_user(entry_1.get(), entry_2.get(), entry_1, entry_2)).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=20,
                                                                                                         pady=10,
                                                                                                         sticky=E)
    button_delete = Button(frame, font=("Calibri", 16), text="Delete", bg="#B4B4B4",
                            command=lambda: delete_user(entry_1.get(), entry_2.get(), entry_1, entry_2)).grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=20,
                                                                                                          pady=10,
                                                                                                          columnspan=2)

    button_back = Button(service_status_screen, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(service_status_screen)).grid(row=5, column=0, padx=50, pady=10, sticky=E)
    button_exit = Button(service_status_screen, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=5, column=0, padx=20, pady=10,
                                                                               sticky=W)


def block_user(cust_id, acc_id, entry_1, entry_2):
    from User_functions import accounts as acnt
    custID = cust_id
    if acc_id == '':
        acc_id = 0
    accID = int(acc_id)
    if accID != 0:
        if acnt.block_accntid(custID,accID):
            message = messagebox.showinfo("SUCCESS!", f"{accID} blocked.")
        else:
            message = messagebox.showinfo("404!", "Cannot find account id\nPlease check again.")

    else:
        if acnt.block_cust(custID):
            message = messagebox.showinfo("SUCCESS!", f"{custID} blocked.")
        else:
            message = messagebox.showinfo("404!", "Cannot find customer id\nPlease check again.")


    entry_1.delete(0, END)
    entry_2.delete(0, END)


def open_user(cust_id, acc_id, entry_1, entry_2):
    from User_functions import accounts as acnt
    custID = cust_id
    if acc_id == '':
        acc_id = 0
    accID = int(acc_id)
    if accID != 0:
        if acnt.open_accntid(custID,accID):
            message = messagebox.showinfo("SUCCESS!", f"{accID} opened.")
        else:
            message = messagebox.showinfo("404!", "Cannot find account id\nPlease check again.")

    else:
        if acnt.open_cust(custID):
            message = messagebox.showinfo("SUCCESS!", f"{custID} opened.")
        else:
            message = messagebox.showinfo("404!", "Cannot find customer id\nPlease check again.")

    entry_1.delete(0, END)
    entry_2.delete(0, END)


def delete_user(cust_id, acc_id, entry_1, entry_2):
    from User_functions import accounts as acnt
    custID = cust_id
    if acc_id == '':
        acc_id = 0
    accID = int(acc_id)
    if accID != 0:
        val = acnt.delete_accnt(custID,accID)
        if val:
            message = messagebox.showinfo("SUCCESS!", f"{accID} Deleted.")
        else:
            message = messagebox.showinfo("404!", "Cannot find account id\nPlease check again.")
    else:
        val2 = acnt.delete_cust(custID)
        if val2:
            message = messagebox.showinfo("SUCCESS!", f"{custID} deleted.")
        else:
            message = messagebox.showinfo("404!", "Cannot find customer id\nPlease check again.")


    entry_1.delete(0, END)
    entry_2.delete(0, END)


def card_application_page():
    global image_f
    global card_app_screen

    card_app_screen = Toplevel()
    card_app_screen.title("The Continental")
    card_app_screen.iconbitmap("Icon.ico")

    logo = Label(card_app_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(card_app_screen, text="CARD APPLICATION")
    frame.grid(row=1, column=0, padx=80, pady=20)

    label1 = Label(frame, font=("Calibri", 18), text="Cust ID: ").grid(row=0, column=0, pady=50, padx=10)

    entry_id = Entry(frame, font=("Calibri", 18))
    entry_id.grid(row=0, column=1, pady=30, padx=30)

    Butt1 = Button(frame, text="ENTER", command=lambda: switch_screen(entry_id.get()), height=2, width=15,
                   bg="#B4B4B4").grid(row=1, column=1, pady=60)

    button_back = Button(frame, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(card_app_screen)).grid(row=3, column=1, padx=20, pady=10, sticky=E)
    button_exit = Button(frame, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=3, column=0, padx=20, pady=10,
                                                                               sticky=W)


def switch_screen(cust):
    from User_functions import transaction as txn

    li = txn.requeststatement(cust)  ##GET ME THE REQUESTS IN THIS LI DICTIONARY
    request_page(li, cust)
    card_app_screen.destroy()


def request_page(li, cust):
    global requests_screen
    global image_f

    requests_screen = Toplevel()
    requests_screen.title("The Continental")
    requests_screen.iconbitmap("Icon.ico")

    logo = Label(requests_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(requests_screen, text="CARD APPLICATION CUST: " + cust)
    frame.grid(row=1, column=0, padx=80, pady=20)

    n = 0
    if len(li) == 0:
        label = Label(frame, font=("Calibri", 16), text="(No Pending Requests)").grid(row=0, column=0, pady=50, padx=10)
    for i in li:
        li[i] = IntVar()
        c = Checkbutton(frame, font=("Arial Black", 14), text=i, variable=li[i], onvalue=1, offvalue=0)
        c.deselect()
        c.grid(row=n, column=0, padx=20, pady=7)
        n = n + 1

    if len(li) != 0:
        butt = Button(frame, text="Done", font=("Calibri", 16), bg="#B4B4B4",
                      command=lambda: edit_request_page(li, cust)).grid(row=n, column=0, padx=20, pady=30, sticky=E)

    button_back = Button(frame, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(requests_screen)).grid(row=n + 1, column=1, padx=20, pady=10, sticky=E)
    button_exit = Button(frame, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=n + 1, column=0, padx=20, pady=10,
                                                                               sticky=W)


def edit_request_page(li, cust):
    global requests_screen
    info = messagebox.askquestion("CONFIRM!", "Do you confirm to Mark them as Done?")
    if info == "yes":
        d = {}
        l_checked = []
        l_notchecked = []
        for i in li:
            try:
                if li[i].get() == 0:
                    d[i] = int(li[i].get())
                    l_notchecked.append(i)
                else:
                    l_checked.append(i)
            except:
                if li[i] == 0:
                    d[i] = int(li[i])
                    l_notchecked.append(i)
                else:
                    l_checked.append(i)

        requests_screen.destroy()
        change_requests(cust, l_checked, l_notchecked)
        request_page(d, cust)

    else:
        pass


def change_requests(cust, l_checked, l_notchecked):
    from User_functions import transaction as txn
    from User_functions.emailserver import otp_email_sender_yagmail as mail
    from User_functions import accounts as acnt
    for i in l_checked:
        lis = i.split()
        s = lis[0]
        reqid = s[0:(len(s)-1)]
        lis2 = reqid.split('.')
        mail.request_complete_email_card(acnt.get_email(custid=cust),reqid,'We have sent you a mail containing the details your new transaction card.\nIF NOT RECIEVED WITHIN 24HRS PLEASE CONTACT CUSTOMER CARE IMMEDIATELY.')
        txn.delete_request_requesttab(reqid)
        desc = f'Card assigned to customer id: {cust},account: {lis2[-1]}'
        txn.add_req_transac(desc,cust,lis2[-1])


def update_records_page():
    global update_screen
    global image_f

    update_screen = Toplevel()
    update_screen.title("The Continental")
    update_screen.iconbitmap("Icon.ico")

    logo = Label(update_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(update_screen, text="UPDATE")
    frame.grid(row=1, column=0, padx=80, pady=20)

    label1 = Label(frame, font=("Calibri", 18), text="Cust ID: ").grid(row=0, column=0, pady=15, padx=10)
    label2 = Label(frame, font=("Calibri", 18), text="Accnt ID: ").grid(row=1, column=0, pady=15, padx=10)
    label3 = Label(frame, font=("Calibri", 18), text="Field: ").grid(row=2, column=0, pady=15, padx=10)
    label4 = Label(frame, font=("Calibri", 18), text="New Data: ").grid(row=3, column=0, pady=15, padx=10)

    entry_1 = Entry(frame, font=("Calibri", 18))
    entry_1.grid(row=0, column=1, pady=15, padx=30)

    entry_2 = Entry(frame, font=("Calibri", 18))
    entry_2.grid(row=1, column=1, pady=15, padx=30)

    li = ["Name", "DOB", "Email", "Passwd", "Mobile", "Address", "City", "State", "Zipcode", "Aadhar",
          "Business", "ssn", "Profit", "Spouse's Name",
          "Spouse's Mobile", "Spouse's Aadhar", "Spouse's Occupation", "Spouse's Income"]

    variable = StringVar(frame)

    w = ttk.Combobox(frame, textvariable=variable, values=li)
    variable.set("(Choose Field)")
    w.grid(row=2, column=1, pady=15, padx=30)

    text_field = Text(frame, font=("Calibri", 18), width=30, height=2)
    text_field.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

    butt = Button(frame, text="Done", font=("Calibri", 16), bg="#B4B4B4",
                  command=lambda: update_process(entry_1.get(), entry_2.get(), variable.get(),
                                                 text_field.get("1.0", "end-1c"))).grid(row=5, column=1, padx=20,
                                                                                        pady=30, sticky=W)

    button_back = Button(update_screen, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(update_screen)).grid(row=6, column=0, padx=20, pady=10, sticky=E)
    button_exit = Button(update_screen, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=6, column=0, padx=20, pady=10,
                                                                               sticky=W)


def update_process(cust, acc, field, new_data):
    from User_functions import accounts as acnt
    global update_screen
    from User_functions.emailserver import otp_email_sender_yagmail as mail

    cust_id = str(cust)
    if acc == '':
        ac_id = 0
    else:
        ac_id = int(acc)
    info = messagebox.askquestion("Confirm!", "Do you Confirm and Wish to proceed?")
    if info == "yes":
        if field in ["Name", "DOB", "Email", "Passwd", "Mobile", "Address", "City", "State", "Zipcode", "Aadhar"]:
            result = acnt.update_users(cust_id,field,new_data,ac_id)
            if result:
                content = f"Your {field} has been unpdated to {new_data}"
                mail.general_mail(acnt.get_email(custid = cust_id),content)
                success = messagebox.showinfo("Success!",
                                              "The Data for Customer_ID: " + cust + "\nAccount_ID: " + acc + "\nField: " + field + "\n\nHas been changed")
                if success == "ok":
                    update_screen.destroy()
            else:
                error = messagebox.showinfo("404!","Data not matched, please check again")

        elif field in ["Business", "ssn", "Profit"]:
            result = acnt.update_creditacnt(cust_id,field,new_data,ac_id)
            if result:
                content = f"Your {field} has been unpdated to {new_data}"
                mail.general_mail(acnt.get_email(custid=cust_id), content)
                success = messagebox.showinfo("Success!",
                                              "The Data for Customer_ID: " + cust + "\nAccount_ID: " + acc + "\nField: " + field + "\n\nHas been changed")
                if success == "ok":
                    update_screen.destroy()
            else:
                error = messagebox.showinfo("404!","Data not matched, please check again")
        else:
            result = acnt.update_spouse_details(cust_id,field,new_data)
            if result:
                content = f"Your {field} has been unpdated to {new_data}"
                mail.general_mail(acnt.get_email(custid=cust_id), content)
                success = messagebox.showinfo("Success!",
                                              "The Data for Customer_ID: " + cust + "\nAccount_ID: " + acc + "\nField: " + field + "\n\nHas been changed")
                if success == "ok":
                    update_screen.destroy()
            else:
                error = messagebox.showinfo("404!", "Data not matched, please check again")


    else:
        pass


####CREATING A CLASS TO GET A SCROLLABLE FRAME EVERYWHERE
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, width = 800, height = 480)
        scrollbar1 = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar2 = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar1.set)
        canvas.configure(xscrollcommand=scrollbar2.set)

        canvas.grid(row=0,column=0)
        scrollbar1.grid(row=0, column=100, rowspan=100, sticky='ns')
        scrollbar2.grid(row=100,columnspan=100, sticky='we')

def cust_details_page():
    global cust_screen
    global image_f

    cust_screen = Toplevel()
    cust_screen.title("The Continental")
    cust_screen.iconbitmap("Icon.ico")

    logo = Label(cust_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(cust_screen, text="ENTER CUSTOMER ID")
    frame.grid(row=1, column=0, padx=80, pady=20)

    label1 = Label(frame, font=("Calibri", 18), text="Cust ID: ").grid(row=0, column=0, pady=50, padx=10)

    entry_id = Entry(frame, font=("Calibri", 18))
    entry_id.grid(row=0, column=1, pady=30, padx=30)

    Butt1 = Button(frame, text="ENTER", command=lambda: show_cust_details(entry_id.get()), height=2, width=15,
                   bg="#B4B4B4").grid(row=1, column=1, pady=60)

    button_back = Button(frame, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(cust_screen)).grid(row=3, column=1, padx=20, pady=10, sticky=E)
    button_exit = Button(frame, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=3, column=0, padx=20, pady=10,
                                                                               sticky=W)


def show_cust_details(cust):
    global cust_screen
    global image_f
    global details_screen
    from User_functions import accounts as acnt

    cust_screen.destroy()

    try:
        details_screen = Toplevel()
        details_screen.title("The Continental")
        details_screen.iconbitmap("Icon.ico")

        logo = Label(details_screen, image=image_f).grid(row=0, column=0, columnspan=3)

        frame = LabelFrame(details_screen, text="DETAILS OF CUST_ID: " + cust)
        frame.grid(row=1, column=0, padx=80, pady=20)
        frame_s = ScrollableFrame(frame)

        li = ["Name:", "DOB:","Gender:","Email:", "Mobile:", "Address:", "Aadhar:","Status:"]

        gen_details = acnt.get_details_users(li, str(cust))  ##FILL THE GENERAL DETAILS IN THIS LIST

        d = {}

        for i in range(len(li)):
            d[li[i]] = gen_details[i]

        n = 1

        ttk.Label(frame_s.scrollable_frame, font=("Arial Black", 20, "underline"), text="GENERAL DETAILS ").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 columnspan=2,
                                                                                                                 pady=10,
                                                                                                                 padx=5,
                                                                                                                 sticky=W)

        for j in d:
            ttk.Label(frame_s.scrollable_frame, font=("Calibri", 12), text=j).grid(row=n, column=0, pady=3, padx=5,
                                                                                   sticky=W)
            ttk.Label(frame_s.scrollable_frame, font=("Calibri", 12), text=d[j]).grid(row=n, column=1, pady=3, padx=5,
                                                                                      sticky=W)
            n += 1

        if has_credit(cust) == True:
            ttk.Label(frame_s.scrollable_frame, font=("Arial Black", 20, "underline"),
                      text="CREDIT ACCOUNT DETAILS ").grid(
                row=n, column=0, columnspan=2, pady=10, padx=5, sticky=W)
            n += 1

            l2 = ["Business:", "SSN:", "Profit:", "Turnover:"]

            cred_details = acnt.get_details_credit(l2, str(cust))  ##GET THE CREDIT DETAILS IN THIS LIST

            d2 = {}
            for k in range(len(l2)):
                d2[l2[k]] = cred_details[k]

            for m in d2:
                ttk.Label(frame_s.scrollable_frame, font=("Calibri", 12), text=m).grid(row=n, column=0, pady=3, padx=5,
                                                                                       sticky=W)
                ttk.Label(frame_s.scrollable_frame, font=("Calibri", 12), text=d2[m]).grid(row=n, column=1, pady=3,
                                                                                           padx=5,
                                                                                           sticky=W)
                n += 1

        if has_wife(cust) == True:
            ttk.Label(frame_s.scrollable_frame, font=("Arial Black", 20, "underline"), text="SPOUSE DETAILS ").grid(
                row=n,
                column=0,
                columnspan=2,
                pady=10,
                padx=5,
                sticky=W)
            n += 1

            try:
                l3 = ["Name:", "DOB:", "Aadhar:", "Occupation:", "Income:", "Cardno:"]
                wife_details = acnt.get_details_spouse(l3, str(cust))  ##GET THE WIFE DETAILS IN THIS LIST
            except:
                l3 = ["Name:", "DOB:", "Aadhar:", "Occupation:", "Income:"]
                wife_details = acnt.get_details_spouse(l3, str(cust))

            d3 = {}
            for k in range(len(l3)):
                d3[l3[k]] = wife_details[k]

            for m in d3:
                ttk.Label(frame_s.scrollable_frame, font=("Calibri", 12), text=m).grid(row=n, column=0, pady=3, padx=5,
                                                                                       sticky=W)
                ttk.Label(frame_s.scrollable_frame, font=("Calibri", 12), text=d3[m]).grid(row=n, column=1, pady=3,
                                                                                           padx=5,
                                                                                           sticky=W)
                n += 1

        ttk.Label(frame_s.scrollable_frame, font=("Arial Black", 20, "underline"), text="ACCOUNTS ").grid(row=n,
                                                                                                          column=0,
                                                                                                          columnspan=2,
                                                                                                          pady=10,
                                                                                                          padx=5,
                                                                                                          sticky=W)
        n += 1
        lst = [["AccntID", "Type-status", "CardNo"]]

        lst2 = acnt.get_details_accounts(lst[0], str(cust))

        for i in range(len(lst2)):
            lst.append(lst2[i])

        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):
                tab = Entry(frame_s.scrollable_frame, width=50,
                            font=('Calibri', 14, 'bold'))

                tab.grid(row=n, column=j, columnspan=1, sticky=W)
                tab.insert(END, lst[i][j])
                tab.config(state="disabled")
            n += 1
        ttk.Label(frame_s.scrollable_frame, text=" ").grid(row=n, column=0, columnspan=2, pady=10, padx=5, sticky=W)
        ttk.Label(frame_s.scrollable_frame, text=" ").grid(row=n + 1, column=0, columnspan=2, pady=10, padx=5, sticky=W)
        ttk.Label(frame_s.scrollable_frame, text=" ").grid(row=n + 2, column=0, columnspan=2, pady=10, padx=5, sticky=W)
        ttk.Label(frame_s.scrollable_frame, text=" ").grid(row=n + 3, column=0, columnspan=2, pady=10, padx=5, sticky=W)
        ttk.Label(frame_s.scrollable_frame, text=" ").grid(row=n + 4, column=0, columnspan=2, pady=10, padx=5, sticky=W)

        button_back = Button(details_screen, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                             command=lambda: back(details_screen)).grid(row=n + 6, column=1, padx=20, pady=10, sticky=E)
        button_exit = Button(details_screen, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                             command=lambda: back(home_screen, value="exit")).grid(row=n + 6, column=0, padx=20,
                                                                                   pady=10,
                                                                                   sticky=W)

        frame_s.grid(row=1, column=0, padx=80, pady=20)

    except:
        error = messagebox.showerror("404!","Customer not found")
        if error == 'ok':
            back(details_screen)





def has_credit(cust):
    from User_functions import accounts as acnt
    conection = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''SELECT custid FROM creditacnts;''')
    out = cur.fetchall()
    fi = []
    for i in out:
        for j in i:
            fi.append(j)
    if str(cust) in fi:
        return True
    else:
        return False


def has_wife(cust):
    from User_functions import accounts as acnt
    conection = acnt.establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''SELECT custid FROM spouse_credit_cards;''')
    out = cur.fetchall()
    fi = []
    for i in out:
        for j in i:
            fi.append(j)
    cur.execute(f'''SELECT custid FROM card_applications;''')
    out2 = cur.fetchall()
    fi2 = []
    for i in out2:
        for j in i:
            fi2.append(j)

    if str(cust) in fi+fi2:
        return True
    else:
        return False


def others_page():
    # Sitka Subheading
    global others_screen
    global image_f
    from admin_functions import request_admin as r

    others_screen = Toplevel()
    others_screen.title("The Continental")
    others_screen.iconbitmap("Icon.ico")

    logo = Label(others_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(others_screen, text="OTHER")
    frame.grid(row=1, column=0, padx=80, pady=20)

    cust_list = r.get_request_others()
    if cust_list == []:
        cust_list = ['NO REQUESTS :)']
    else:
        pass

    global cnide
    cnide = 0

    global labelcnide
    labelcnide = Label(frame, font=("Calibri", 24, "bold"),
                       text="Query: " + str(cnide + 1) + "\n" + str(cust_list[cnide]))
    labelcnide.grid(row=0, column=0, pady=50, padx=80)

    Butt_reply = Button(frame, font=("Calibri", 16, "bold"), text="REPLY", command=lambda: reply_page(cnide, cust_list),
                        height=1, width=13, bg="#B4B4B4").grid(row=1, column=0, pady=30)
    Butt1 = Button(frame, text="NEXT", command=lambda: show_next(cust_list, cnide + 1, frame), height=2, width=15,
                   bg="#B4B4B4").grid(row=2, column=0, pady=10)
    Butt2 = Button(frame, text="PREV", command=lambda: show_next(cust_list, cnide - 1, frame), height=2, width=15,
                   bg="#B4B4B4").grid(row=3, column=0, pady=10)

    button_back = Button(others_screen, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                         command=lambda: back(others_screen)).grid(row=3, column=1, padx=20, pady=10, sticky=E)
    button_exit = Button(others_screen, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=3, column=0, padx=20, pady=10,
                                                                               sticky=W)


def show_next(cust_list, n, frame):
    if (n + 1) > len(cust_list) or n < 0:
        pass
    else:
        global labelcnide
        labelcnide.destroy()
        labelcnide = Label(frame, font=("Calibri", 24, "bold"), text="Query: " + str(n + 1) + "\n" + str(cust_list[n]))
        labelcnide.grid(row=0, column=0, pady=80, padx=50)

        global cnide
        cnide = n


def reply_page(n, cust_list):
    if cust_list == ['NO REQUESTS :)']:
        messagebox.showinfo(None,cust_list[0])
    else:
        global reply_screen
        global image_f
        global others_screen

        others_screen.destroy()

        request = cust_list[n]  ##YOUR REQUEST AS A STRING TO GET YOUR CUST ID

        reply_screen = Toplevel()
        reply_screen.title("The Continental")
        reply_screen.iconbitmap("Icon.ico")

        logo = Label(reply_screen, image=image_f).grid(row=0, column=0, columnspan=3)

        frame = LabelFrame(reply_screen, text="REPLY")
        frame.grid(row=1, column=0, padx=80, pady=20)

        label_f = Label(frame, font=("Calibri", 18, "bold"), text="Text: ").grid(row=0, column=0, pady=30)
        text_field = Text(frame, font=("Calibri", 16), width=60, height=5)
        text_field.grid(row=0, column=1, columnspan=2, padx=20, pady=10)

        Butt1 = Button(frame, text="DONE", command=lambda: send_reply(request, text_field.get("1.0", "end-1c")),
                       height=2,
                       width=15, bg="#B4B4B4").grid(row=2, column=1, pady=10, sticky=E)

        button_back = Button(reply_screen, font=("Calibri", 10), text="Back", bg="#B4B4B4",
                             command=lambda: back(reply_screen)).grid(row=4, column=1, padx=20, pady=10, sticky=E)




def send_reply(request, reply):  ## YORU NEEDED PARAMETERS
    global reply_screen
    from admin_functions import request_admin as r
    from User_functions.emailserver import otp_email_sender_yagmail as mail
    from User_functions import transaction as txn
    from User_functions import accounts as acnt
    message = messagebox.askquestion("Confirm", "Do you wish to proceed ?")

    if message == "yes":
        custid = r.get_custid_req(request)
        emailid = acnt.get_email(custid=custid)
        mail.request_complete_email(emailid,request,reply)
        txn.add_req_transac(f"request {r.get_request_id(request)} completed",custid)
        if r.delete_request(request):
            suc = messagebox.showinfo("Reply Sent",
                                  "Your reply has been sent to the customer.\nClick OK to proceed back to Others")
            if suc == "ok":
                reply_screen.destroy()
                others_page()
    else:
        pass


def dm_cust():
    global image_f
    global dm_screen

    dm_screen = Toplevel()
    dm_screen.title("The Continental")
    dm_screen.iconbitmap("Icon.ico")

    logo = Label(dm_screen, image=image_f).grid(row=0, column=0, columnspan=3)

    frame = LabelFrame(dm_screen, text="REQUEST")
    frame.grid(row=1, column=0, padx=80, pady=20)

    label = Label(frame, font=("Calibri", 20), text="Customer ID: ").grid(row=0, column=0, pady=15, padx=50, sticky=W)
    label = Label(frame, font=("Calibri", 20), text="Text: ").grid(row=1, column=0, columnspan=2, pady=15, padx=50,
                                                                   sticky=W)

    entry_id = Entry(frame, font=("Calibri", 18), width=30)
    entry_id.grid(row=0, column=0, padx=20, pady=10, columnspan=2, sticky=E)

    text_field = Text(frame, font=("Calibri", 18), width=60, height=5)
    text_field.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    button_enter = Button(frame, font=("Calibri", 16), text="EMAIL", bg="#B4B4B4",
                          command=lambda: process_dm(entry_id.get(), text_field.get("1.0", "end-1c")), width=20).grid(
        row=3, column=0, columnspan=1, padx=20, pady=20, sticky=E)
    button_back = Button(frame, font=("Calibri", 10), text="Back", bg="#B4B4B4", command=lambda: back(dm_screen)).grid(
        row=4, column=2, padx=20, pady=20, sticky=E)
    button_exit = Button(frame, font=("Calibri", 10), text="Exit", bg="#B4B4B4",
                         command=lambda: back(home_screen, value="exit")).grid(row=4, column=0, padx=20, pady=20,
                                                                              sticky=W)


def process_dm(cust_id, text):
    global dm_screen
    from User_functions import accounts as acnt
    from User_functions.emailserver import otp_email_sender_yagmail as mail
    print(cust_id, text)
    ##SAVE YOUR REQUEST FROM HERE

    question = messagebox.askquestion("Confirm!", "Do you wish to proceed ?")
    if question == "yes":
        receiver_mail = acnt.get_email(custid=cust_id)
        mail.general_mail(receiver_mail,text)
        success = messagebox.showinfo("Success!", "Your Text has been sent to " + str(cust_id))
        if success == "ok":
            dm_screen.destroy()
    else:
        pass


def card_assn_page():
    global assn_screen
    global image_f

    assn_screen = Toplevel()
    assn_screen.title("The Continental")
    assn_screen.iconbitmap("Icon.ico")

    logo = Label(assn_screen, image=image_f).grid(row=0,column=0,columnspan=3)

    frame = LabelFrame(assn_screen, text = "UPDATE")
    frame.grid(row=1, column=0, padx=80, pady=20)


    label1 = Label(frame, font=("Calibri",18), text = "Cust ID: ").grid(row=0, column=0,pady=15,padx=10)
    label2 = Label(frame, font=("Calibri",18), text = "Accnt ID: ").grid(row=2, column=0,pady=15,padx=10)
    label3 = Label(frame, font=("Calibri",18), text = "Card institution: ").grid(row=3, column=0,pady=15,padx=10)
    label4 = Label(frame, font=("Calibri",18), text = "Transaction Type: ").grid(row=4, column=0,pady=15,padx=10)

    entry_1 = Entry(frame, font=("Calibri",18))
    entry_1.grid(row = 0, column =1, pady=15, padx=30)

    entry_2 = Entry(frame, font=("Calibri",18))
    entry_2.grid(row = 2, column =1, pady=15, padx=30)

    l1 = ["User", "Spouse", "Both"]

    variable = StringVar()

    w = OptionMenu(frame, variable, *l1)
    variable.set("(Account Holder)")
    w.grid(row = 1, column =1, pady=15, padx=30)

    card_var = StringVar()

    l2 = ["Master", "Visa"]
    x = OptionMenu(frame, card_var, *l2)
    card_var.set("(Choose)")
    x.grid(row = 3, column =1, pady=15, padx=30)

    cd = StringVar()

    l3 = ["Credit", "Debit"]
    y = OptionMenu(frame, cd, *l3)
    cd.set(" (Choose) ")
    y.grid(row = 4, column =1, pady=15, padx=30)


    butt = Button(frame, text = "Assign",font=("Calibri",16), bg = "#B4B4B4", command =lambda: assn_card(entry_1.get(), entry_2.get(), variable.get(), card_var.get(), cd.get())).grid(row=5, column =1,padx=20,pady=30,sticky =W)

    button_back = Button(assn_screen, font=("Calibri",10), text = "Back", bg="#B4B4B4", command =lambda: back(assn_screen)).grid(row = 6, column=0, padx=20, pady=10, sticky= E)
    button_exit = Button(assn_screen, font=("Calibri",10), text = "Exit", bg="#B4B4B4", command =lambda: back(home_screen, value="exit")).grid(row = 6, column=0, padx=20, pady=10, sticky= W)

def assn_card(cust, accnt, holder, card_com, cred_deb):
    global assn_screen
    from User_functions import accounts as acnt
    from User_functions.card_function import cardlog as cl
    from User_functions.emailserver import otp_email_sender_yagmail as mail
    import random

    try:
        card = cl.get_cardno(accnt)[0]
        balance = cl.get_balance_card(int(card))
    except:
        balance = 200000
    if card_com in ['Visa','visa','VISA']:
        card_com = 'visa'
    else:
        card_com = 'mastercard'
    question = messagebox.askquestion("Confirm!", "Do you wish to proceed ?")
    if question == "yes":
        if holder in ["user","USER","User"]:
            details = cl.generate_creditcard(card_com)
            pin = random.randint(1000,9999)
            acnt.addto_acntcard(int(accnt),details[0],cred_deb)
            cl.addto_cardlog(details[0],details[1],details[2],card_com,pin,balance)
            mail.card_assign_mail(acnt.get_email(custid=cust),details[0],accnt,cust,details[1],details[2],balance,pin,card_com,cred_deb)
            success = messagebox.showinfo("Success!", "Card Successfully Assigned!")
            if success == "ok":
                assn_screen.destroy()
        elif holder in ["Both","BOTH","Both"]:
            details = cl.generate_creditcard(card_com)
            pin = random.randint(1000, 9999)
            acnt.addto_acntcard(int(accnt), details[0], cred_deb)
            cl.addto_cardlog(details[0], details[1], details[2], card_com,pin,balance)
            mail.card_assign_mail(acnt.get_email(custid=cust), details[0], accnt, cust, details[1], details[2], balance,
                                  pin, card_com, cred_deb)
            details = cl.generate_creditcard(card_com)
            pin = random.randint(1000, 9999)
            acnt.addto_acntcard(int(accnt), details[0], cred_deb,)
            cl.addto_cardlog(details[0], details[1], details[2], card_com,pin,balance)
            spouse = acnt.get_details_spouse(['name:','dob:','aadhar:','income:','occupation:'],cust)
            acnt.addto_spouse_card(details[0],spouse[0],spouse[1],spouse[2],spouse[4],spouse[3],cust)
            mail.card_assign_mail(acnt.get_email(custid=cust), details[0], accnt, cust, details[1], details[2], balance,
                                  pin, card_com, cred_deb)
        else:
            details = cl.generate_creditcard(card_com)
            pin = random.randint(1000, 9999)
            acnt.addto_acntcard(int(accnt), details[0], cred_deb)
            cl.addto_cardlog(details[0], details[1], details[2], card_com,pin,balance)
            spouse = acnt.get_details_spouse(['name:', 'dob:', 'aadhar:', 'income:', 'occupation:'], cust)
            acnt.addto_spouse_card(details[0], spouse[0], spouse[1], spouse[2], spouse[4], spouse[3], cust)
            mail.card_assign_mail(acnt.get_email(custid=cust), details[0], accnt, cust, details[1], details[2], balance,
                                  pin, card_com, cred_deb)

        success = messagebox.showinfo("Success!", "Card Successfully Assigned!")
        if success == "ok":
            assn_screen.destroy()
    else:
        pass

def history_page():
    global cust_screen_hist
    global image_f

    cust_screen_hist = Toplevel()
    cust_screen_hist.title("The Continental")
    cust_screen_hist.iconbitmap("Icon.ico")

    logo = Label(cust_screen_hist, image=image_f).grid(row=0,column=0,columnspan=3)

    frame = LabelFrame(cust_screen_hist, text = "ENTER CUSTOMER ID")
    frame.grid(row=1, column=0, padx=80, pady=20)

    label1 = Label(frame, font=("Calibri",18), text = "Cust ID: ").grid(row=0, column=0,pady=50,padx=10)

    entry_id = Entry(frame, font=("Calibri",18))
    entry_id.grid(row = 0, column =1, pady=30, padx=30)

    Butt1 = Button(frame, text= "ENTER" ,command =lambda: get_hist_factor(entry_id.get()),  height=2, width = 15, bg ="#B4B4B4").grid(row=1,column=1, pady= 60)

    button_back = Button(frame, font=("Calibri",10), text = "Back", bg="#B4B4B4", command =lambda: back(cust_screen_hist)).grid(row = 3, column=1, padx=20, pady=10, sticky= E)
    button_exit = Button(frame, font=("Calibri",10), text = "Exit", bg="#B4B4B4", command =lambda: back(home_screen, value="exit")).grid(row = 3, column=0, padx=20, pady=10, sticky= W)

def get_hist_factor(cust_id):
    global factor_screen
    global image_f
    global cust_screen_hist

    cust_screen_hist.destroy()

    factor_screen = Toplevel()
    factor_screen.title("The Continental")
    factor_screen.iconbitmap("Icon.ico")

    logo = Label(factor_screen, image=image_f).grid(row=0,column=0,columnspan=3)

    frame = LabelFrame(factor_screen, text = "Enter Necessary factors for User History")
    frame.grid(row=1, column=0, padx=80, pady=20)

    li=["DATE","TIME"]
    typo = StringVar()
    typo.set("(Choose Type)")

    label1 = Label(frame, font=("Calibri",18), text = "SORT BY \n Factor: ").grid(row=0, column=0,pady=25,padx=10)

    entry_id = Entry(frame, font=("Calibri",18))
    entry_id.grid(row = 1, column =0,columnspan=2, pady=30, padx=30)
    entry_d = OptionMenu(frame, typo, *li)
    entry_d.grid(row=0,column=1)

    Butt1 = Button(frame, text= "OK" ,command =lambda: show_hist(cust_id, typo.get(), entry_id.get()),  height=2, width = 15, bg ="#B4B4B4").grid(row=2,column=0,columnspan=2, pady= 60)

    button_back = Button(frame, font=("Calibri",10), text = "Back", bg="#B4B4B4", command =lambda: back(factor_screen)).grid(row = 3, column=1, padx=20, pady=10, sticky= E)
    button_exit = Button(frame, font=("Calibri",10), text = "Exit", bg="#B4B4B4", command =lambda: back(home_screen, value="exit")).grid(row = 3, column=0, padx=20, pady=10, sticky= W)

class ScrollableFrame02(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, width = 600, height = 300)
        scrollbar1 = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar2 = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar1.set)
        canvas.configure(xscrollcommand=scrollbar2.set)

        canvas.grid(row=0,column=0)
        scrollbar1.grid(row=0, column=100, rowspan=100, sticky='ns')
        scrollbar2.grid(row=100,columnspan=100, sticky='we')



def show_hist(cust_id, factor, extra_field_data):
    global factor_screen
    global image_f
    global show_hist_screen
    from User_functions import transaction as tx

    factor_screen.destroy()

    show_hist_screen = Toplevel()
    show_hist_screen.title("The Continental")
    show_hist_screen.iconbitmap("Icon.ico")

    logo = Label(show_hist_screen, image=image_f).grid(row=0,column=0,columnspan=3)


    frame = LabelFrame(show_hist_screen, text = "HISTORY OF CUST: "+ cust_id)
    frame.grid(row=1, column=0, padx=80, pady=20)
    frame_s = ScrollableFrame02(frame)

    lst = [["Request ID", "Day", "Date", "Time", "Description"]]

    lst2 = tx.get_history(cust_id,factor,extra_field_data)

    for i in range(len(lst2)):
        lst.append(lst2[i])

    total_rows = len(lst)
    total_columns = len(lst[0])



    for i in range(total_rows):
        for j in range(total_columns):

            tab = Entry(frame_s.scrollable_frame , width=35,
                           font=('Calibri',14,'bold'))

            tab.grid(row=i, column=j,columnspan=1,sticky=W)
            tab.insert(END, lst[i][j])
            tab.config(state = "disabled")

    frame_s.grid(row=0, column=0,padx=20, pady=20)
    button_back = Button(frame, font=("Calibri",10), text = "Back", bg="#B4B4B4", command =lambda: back(show_hist_screen)).grid(row = total_rows+1, column=1, padx=20, pady=10, sticky= E)
    button_exit = Button(frame, font=("Calibri",10), text = "Exit", bg="#B4B4B4", command =lambda: back(home_screen, value="exit")).grid(row = total_rows+1, column=0, padx=20, pady=10, sticky= W)


def back(screen, value = "back"):
    global login_page
    global home_screen
    global service_status_screen
    global card_app_screen
    global update_screen
    global cust_screen
    global details_screen
    global reply_screen
    global dm_screen
    global cust_screen_hist
    global factor_screen
    global show_hist_screen

    if screen == login_page:
        warning = messagebox.askquestion("WARNING!", "Are you sure You want to Exit ? ?")
        if warning =='yes':
            screen.destroy()
        else:
            pass

    elif screen == home_screen:
        if value == "exit":
            warning = messagebox.askquestion("WARNING!", "Are you sure You want to Exit ? ?")
            if warning =='yes':
                screen.destroy()
            else:
                pass
        else:
            warning = messagebox.askquestion("WARNING!", "You will be logged out!\nDo you still wish to proceed?")
            if warning =='yes':
                screen.destroy()
                admin_login()
            else:
                pass

    elif screen == service_status_screen or screen == card_app_screen or screen == update_screen or screen == cust_screen or screen == others_screen or screen == dm_screen or screen == cust_screen_hist:
        screen.destroy()

    elif screen == requests_screen:
        screen.destroy()
        card_application_page()

    elif screen == details_screen:
        screen.destroy()
        cust_details_page()

    elif screen == reply_screen:
        screen.destroy()
        others_page()
    elif screen == factor_screen:
        screen.destroy()
        history_page()
    elif screen == show_hist_screen:
        warning = messagebox.askquestion("WARNING!", "You will be taken back to Menu.\nDo you confirm ?")
        if warning =='yes':
            screen.destroy()
        else:
            pass
    else:
        screen.destroy()


login_page = None
home_screen = None
service_status_screen = None
card_app_screen = None
requests_screen = None
update_screen= None
cust_screen = None
cust_screen_hist = None
details_screen = None
others_screen = None
reply_screen = None
dm_screen = None
factor_screen = None
show_hist_screen = None

admin_login()
