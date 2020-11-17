import random
from PIL import Image,ImageDraw, ImageFont, ImageFilter

def font_select():
    '''This function sets the font for the text in captcha'''
    x=random.randint(1,3)
    if x==1:
        a=ImageFont.truetype('ariblk.ttf',40)   #1
    elif x==2:
        a=ImageFont.truetype('segoesc.ttf',40)  #2
    else:
        a=ImageFont.truetype('seguili.ttf',40)  #3
    return (a)

def create_captcha():
    '''This function creates the captcha'''
    st=''
    s="qwertyuioplkjhgfdsazxcvbnm1209873654QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in range(8):
        a=random.randint(0,61)
        st=st+s[a]

    image=Image.open('captcha_pic.jpg') #4
    draw=ImageDraw.Draw(image)
    position=150
    color='rgb(0,0,0)'
    for i in st:
        font=font_select()
        draw.text((position,60), i, fill=color, font=font)
        position=position+33

    blur=image.filter(ImageFilter.BLUR)
    blur.save('pic.png')#
    return st

create_captcha()

'''Instructions
download and save the other given files
#1 font file-give the location where the file is saved on the pc
#2 font file-give the location where the file is saved on the pc
#3 font file-give the location where the file is saved on the pc
#4 captcha background picture-give the location where the file is saved on the pc
#5 the final captcha pic- give the location where u want to save the picture so that u can display it later'''

'''Delete the instruction and numbering comments in the project code'''

