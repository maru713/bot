import discord
import random
import cv2

f=open("card list.txt","r")

F=open("cards ID.txt","r")

data=f.readlines()
Data=F.readlines()

f.close()
i=0
for w in data:
   data[i]=w.replace("\n","")
   Data[i]=Data[i].replace("\n","")
   i=i+1

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!create"):
        num=message.content.replace("!create","")
        try:
           if num=="":
              num=8
           else:
              num=int(num)
        except ValueError:
           num=8
        if num>8:
           num=8
        if num!=8:
           M="ランダムでないカードはコストが小さい順にデッキに入ります\n"
        else:
           M=""
        m=[-1,-1,-1,-1,-1,-1,-1,-1]
        i=0
        iname=["","","","","","","",""]
        mm="https://link.clashroyale.com/deck/jp?deck="
        a=len(data)
        
        for w in range(num):
           
            while 1:
                r=random.randint(0,a-1)
                
                if r not in m:
                   m[w]=r
                   break
        for w in range(8-num):
            while 1:
               if i not in m:
                  m[w+num]=i
                  break
               else:
                  i=1+i
        for w in range(8):
            
            iname[w]=str(m[w])+".png"
            
            mm=mm+Data[r]
            if w!=7:
                mm=mm+";"
                
        img0=cv2.imread(iname[0])
        img1=cv2.imread(iname[1])
        img2=cv2.imread(iname[2])
        img3=cv2.imread(iname[3])
        img4=cv2.imread(iname[4])
        img5=cv2.imread(iname[5])
        img6=cv2.imread(iname[6])
        img7=cv2.imread(iname[7])

        img=cv2.hconcat([img0,img1])
        img=cv2.hconcat([img,img2])
        img=cv2.hconcat([img,img3])
        imag=cv2.hconcat([img4,img5])
        imag=cv2.hconcat([imag,img6])
        imag=cv2.hconcat([imag,img7])
        img=cv2.vconcat([img,imag])
        
        cv2.imwrite("output.png",img)

        fp=open("output.png","rb")
        M=M+"URL➡"+mm+"&id=J90PUUYV"

        await client.send_file(message.channel,fp)
        await client.send_message(message.channel, M)
        
        fp.close()

        
        
client.run("Mzk4Nzk5NTYyMjE2NTcwODgw.DTDylg.ZewGejpbGBzwfHuoWk9vw9EYQCs")
