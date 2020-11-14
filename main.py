from PIL import ImageDraw,Image,ImageFont,ImageOps
import random
import os
def crop(image):
    dp_size = 100,100
    mask = Image.open('image/mask.png').convert('L')
    mask.thumbnail(dp_size)
    im = Image.open(image)
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output

def split(text,font):
    lines=[]
    token=text.split(' ')
    line_length=600
    i=0
    while i<len(token):
        line=''
        while i<len(token) and (font.getsize(line+token[i])[0]<=line_length):
            line+=token[i]+' '
            i+=1
        if not line:
            line=token[i]
            i+=1
        lines.append(line)
    return lines


def create(text,dp,name,username,footer):
    image = Image.new('RGBA',(1080,1080),color="#FFFFFF")
    
    try:
        font_H1 = ImageFont.truetype('font/inter.ttf',size=30) #body
        font_H2 = ImageFont.truetype('font/inter.ttf',size=20) #footer/username
        font_H3 = ImageFont.truetype('font/inter.ttf',size=28) #handler
    except:
        pass
    
    text_list = split(text,font_H1)
    
    x=240
    y=(image.size[1]-font_H1.getsize('hg')[1]*(len(text_list)-1))//2
    
    display_=crop(dp)
    image.paste(display_,(x,y-100))
    write=ImageDraw.Draw(image)
    
    #name
    write.text((x+120,y-80),name,fill='black',font=font_H3)
    #username
    write.text((x+120,y-45),'@'+username,fill='#494646',font=font_H2)
    
    y+=20 #gap btw dp&body
    for _ in text_list:
        point=(x,y)
        write.text(point,_,fill='black',font=font_H1)
        y+=35
    
    #footer
    write.text((x,y+10),footer,fill='#494646',font=font_H2)
    image.save('render/tweet_'+username+'.png')


if __name__ == "__main__":
    name=str(input("Display Name: "))
    username=str(input("Username: "))
    dp=str(input("Profile Picture (path): "))
    tweet=str(input("Tweet: "))
    footer=str(input("Footer\Date$time (11:22 PM - 11/14/20): "))
    
    create(tweet,dp,name,username,footer)

