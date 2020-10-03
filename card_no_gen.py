import random
import math
import accounts as acnt
import cardlog as cl





def check(x):
    s=str(x)
    l=len(s)
    sum=0
    if (l%2)==1:
        g=0
        h=1
    elif (l%2)==0:
        g=1
        h=0
    for i in range(h,l-1,2):
        sum=sum+(((int(s[i]))*2)%10)+(((int(s[i]))*2)//10)
    for i in range(g,l,2):
        sum=sum+int(s[i])
    if (sum%10)==0:
        return 0
    else:
        return 1

def mastercard(L):
    c=1
    while(c==1):
        n=random.randint(51*math.pow(10,14),(56*math.pow(10,14))-1)
        c=check(n)
        if c==1:
            continue
        if n in L:
            c=1
    return n

def visa(L):
    c=1
    while(c==1):
        b=random.randrange(13,17,3)
        n=random.randint(4*math.pow(10,b-1),(5*math.pow(10,b-1))-1)
        c=check(n)
        if c==1:
            continue
        if n in L:
            c=1
    return n


'''Instruction:
Enter the existing cards numbers as integers in a list and pass the list
as paramter while calling either of the card generator functions'''

# connection = acnt.establish_connection('localhost','root','vishal26','bank')
# cur = connection.cursor()
# cur.execute('''SELECT cardno FROM acntcard;
# ''')
# result = cur.fetchall()
# lis = []
# for i in result:
#     for j in i:
#         lis.append(j)
#
# number1=(mastercard(lis))
# number2=(visa(lis))
# print(number1)
# print(number2)

