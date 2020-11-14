import random


def encrypt(n):
    s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'
    c=''
    d=''
    for i in range(len(s)):
        while True:
            x=0
            a=random.randint(0,62)
            b=random.randint(0,62)
            for k in range(len(d)):
                if s[a]==d[k]:
                    if s[b]==c[len(c)-k-1]:
                        x=1
            if x==0:
                c=c+s[b]
                d=s[a]+d
                break
    final=c+d
    f=open("code.txt",'a')
    f.write(final+'\n')
    f.close()
    t=''
    for i in n:
        if i in s:
            for j in range(len(s)):
                if i==s[j]:
                    break
            t=t+final[(j*(-1))-1]+final[j]
        else:
            t=t+i+i
    return (t)


def decrypt(n):
    s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'
    f=open("code.txt",'r')
    l=f.readlines()
    f.close()
    f=open("code.txt",'w')
    code=l[0]
    del l[0]
    f.writelines(l)
    f.close()
    code=code[0:-1]
    t=''
    for i in range(0,len(n)-1,2):
        for j in range(-1,(((len(code))//2)*(-1))-1,-1):
            if n[i]==code[j]:
                if n[i+1]==code[(j+1)*(-1)]:
                    t=t+s[(j+1)*(-1)]
                    break
        else:
            t=t+n[i]
    return (t)
