
def  otp_gen():
    import random
    n=random.randint(10000,99999)
    return f"_____SMS_____\nYour account is being accessed for making a transaction\nYour OTP is {n} \nPlease confirm transaction"

# print(otp_gen())