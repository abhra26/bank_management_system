
def establish_connection(host, user, passwd, database):
    import mysql.connector as cntr
    from mysql.connector import Error
    connection = None
    try:
        connection = cntr.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database
            )

        return connection

    except Error as e:
        return f'An error occured : {e}'

# test = establish_connection('localhost', 'root', 'vishal26', 'bank')
# cur = test.cursor()
# cur.execute("SHOW TABLES;")
# print(cur.fetchall())

class account:
    def __init__(self, accno,passwd, first_name, last_name,dob, email, phone, address, city, state,  aadhar, zip_code, gender ):
        self.accno = accno
        self.passwd = passwd
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.aadhar = aadhar
        self.zip_code = zip_code
        self.gender = gender

    def accno(self):
        return self.accno

    def passwd(self):
        return self.passwd

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def name(self):
        return self.first_name+''+self.last_name

    def dob(self):
        return self.dob

    def email(self):
        return self.email

    def phone(self):
        return self.phone

    def address(self):
        return self.address

    def city(self):
        return self.city

    def state(self):
        return self.state

    def aadhar(self):
        return self.aadhar

    def zip_code(self):
        return self.zip_code

    def gender(self):
        return self.gender

def addto_users(accno,passwd, first_name, last_name,dob, email, phone, address, city, state, aadhar, zip_code,gender):
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f'''INSERT INTO users VALUES
    ({accno},{passwd},'{first_name+' '+last_name}','{dob}','{email}','{gender}',{phone},'{address}','{city}','{state}',{aadhar},{zip_code});
    ''')
    conection.commit()

# user_1 = addto_users(
#     1,
#     4495,
#     'Abhraneel',
#     'Saha',
#     '26-09-2003',
#     'abhraneel2003@gmail.com',
#     9836276787,
#     '1-Kalibari Lane, Jadavpur',
#     'Kolkata',
#     'West Bengal',
#     8987654565,
#     700032,
#     'M'
# )

def create_table_individual(accno,amount):
    import datetime
    conection = establish_connection('localhost', 'root', 'vishal26', 'bank')
    cur = conection.cursor()
    cur.execute(f"""CREATE TABLE {'acnt'+str(accno)}
      (date TEXT NOT NULL, 
      time TEXT NOT NULL, 
      history TEXT NOT NULL, 
      amountleft bigint NOT NULL
      );
    """)
    date = datetime.date.today()
    time = str(datetime.datetime.now()).split()[-1]

    cur.execute(f''' INSERT INTO {'acnt'+str(accno)} VALUES
        ('{str(date)}' , '{time}' , 'account created' , {amount} );
    ''')
    conection.commit()



# cur.execute("""CREATE TABLE IF NOT EXISTS users
#   (id INT AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   age INT,
#   gender TEXT,
#   nationality TEXT,
#   PRIMARY KEY (id)
# )
# """)




