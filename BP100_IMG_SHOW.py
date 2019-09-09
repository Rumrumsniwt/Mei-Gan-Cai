#!/usr/bin/python3

# BP1~100 on Akatsuki shown with images
# Author: Murmurtwins

from PIL import Image,ImageDraw,ImageFont,ImageFilter
from io import BytesIO
import requests, json, math, time
import os

page=int(input('Page number (0,1,2,...):')) # Page Number of API
ID=int(input('Your ID? (An integer):')) # Your User ID
item=int(input('Item (0~99):')) # Item of BP on that certain page (0~99)
module=input('Best or Recent?:') # bruh
optiontosave=input('Wanna save your record? (Y/N):') # Decide whether to save or not

url='http://akatsuki.pw/api/v1/users/scores/'+module+'?mode=0&p='+str(page)+'&l=100&rx=1&id='+str(ID)
url2='https://akatsuki.pw/api/v1/users/rxfull?id='+str(ID)
r=requests.get(url)
r2=requests.get(url2)
result=json.loads(r.text)
result2=json.loads(r2.text)
scores=result['scores']
name=result2['username']
width=900
height=300
image=Image.new('RGB',(width,height),(255,255,255))
image2=Image.new('RGB',(900,250),(0,0,0))
font1=ImageFont.truetype('arial.ttf',36)
font11=ImageFont.truetype('arial.ttf',24)
font12=ImageFont.truetype('arial.ttf',12)
font2=ImageFont.truetype('ARLRDBD.ttf',150)
font21=ImageFont.truetype('ARLRDBD.ttf',36)
font22=ImageFont.truetype('ARLRDBD.ttf',24)
font3=ImageFont.truetype('digifaw.ttf',32)
font4=ImageFont.truetype('GOTHIC.ttf',65)
font41=ImageFont.truetype('GOTHIC.ttf',50)

url11='https://assets.ppy.sh/beatmaps/'
setid=str(scores[item]['beatmap']['beatmapset_id'])
url12='/covers/cover.jpg'
fullurl=url11+setid+url12
url3='https://old.ppy.sh/api/get_beatmaps?k=41a40b9c34b5f28e51c588aa9cba1ea335f6cb24&b='+str(scores[item]['beatmap']['beatmap_id'])
r3=requests.get(url3)
result3=json.loads(r3.text)
songname=result3[0]['artist']+' - '+result3[0]['title']+' ['+result3[0]['version']+']'
creator=' (Beatmap by '+result3[0]['creator']+')'
#creator=' (Beatmap by sdfsfsdfsfsdfsdfsfsdf)'

response=requests.get(fullurl)
response=response.content
BytesIOOBj=BytesIO()
BytesIOOBj.write(response)
img=Image.open(BytesIOOBj)
img=Image.blend(img,image2,0.7)
image.paste(img,(0,50))
draw=ImageDraw.Draw(image)

itemdes=''
if module=='best':
	itemdes='Your BP'+str((page-1)*100+item+1)+' is:'
elif module=='recent':
	itemdes='Your recent performance ('+str((page-1)*100+item+1)+') is:'

draw.text((10,8),itemdes,font=font1,fill=(0,0,0))
draw.text((815-9*len(creator),9),creator,font=font11,fill=(0,0,0))

maxcombo=str(scores[item]['max_combo'])+'/'
maxcombomap=str(scores[item]['beatmap']['max_combo'])
count300='x'+str(scores[item]['count_300'])
count100='x'+str(scores[item]['count_100'])
count50='x'+str(scores[item]['count_50'])
countgeki='x'+str(scores[item]['count_geki'])
countkatu='x'+str(scores[item]['count_katu'])
countmiss='x'+str(scores[item]['count_miss'])
playtime='Playtime: '+scores[item]['time']
acc=str(scores[item]['accuracy'])+'%'
pp=str(round(scores[item]['pp'],2))+'pp'
rank=scores[item]['rank']
beatmapid='Beatmap ID: '+str(scores[item]['beatmap']['beatmap_id'])
player='Player: '+name
mods=scores[item]['mods']

if rank=='A':
	draw.text((10,100),rank,font=font2,fill=(0,255,0))
elif rank=='B':
	draw.text((10,100),rank,font=font2,fill=(0,0,255))
elif rank=='C':
	draw.text((10,100),rank,font=font2,fill=(199,21,133))
elif rank=='SS':
	draw.text((5,100),'S',font=font2,fill=(255,255,0))
	draw.text((20,100),'S',font=font2,fill=(255,255,0))
elif rank=='SSH':
	draw.text((5,100),'S',font=font2,fill=(245,245,220))
	draw.text((20,100),'S',font=font2,fill=(245,245,220))
elif rank=='S':
	draw.text((10,100),'S',font=font2,fill=(255,255,0))
elif rank=='SH':
	draw.text((10,100),'S',font=font2,fill=(245,245,220))
elif rank=='D':
	draw.text((10,100),'D',font=font2,fill=(255,255,0))
	
draw.text((120,55),songname,font=font11,fill=(255,255,255))
#draw.text((10,100),rank,font=font2,fill=(0,255,0))
draw.text((120,90),'300',font=font3,fill=(0,245,255))
draw.text((200,100),count300,font=font11,fill=(255,255,255))
draw.text((350,90),'geki',font=font3,fill=(0,245,255))
draw.text((440,100),countgeki,font=font11,fill=(255,255,255))
draw.text((120,120),'100',font=font3,fill=(0,238,0))
draw.text((200,130),count100,font=font11,fill=(255,255,255))
draw.text((350,120),'katu',font=font3,fill=(0,238,0))
draw.text((450,130),countkatu,font=font11,fill=(255,255,255))
draw.text((120,150),'50',font=font3,fill=(255,215,0))
draw.text((180,160),count50,font=font11,fill=(255,255,255))
draw.text((350,150),'X',font=font21,fill=(255,0,0))
draw.text((380,160),countmiss,font=font11,fill=(255,255,255))

draw.text((120,200),beatmapid,font=font11,fill=(255,255,255))
draw.text((120,230),player,font=font11,fill=(255,255,255))
draw.text((120,260),playtime,font=font22,fill=(255,255,255))

draw.text((510,100),acc,font=font41,fill=(255,255,255))
draw.text((510,200),pp,font=font41,fill=(255,255,255))
draw.text((510,150),maxcombo+maxcombomap,font=font41,fill=(255,255,255))

modsafter=mods-128
comb=[2,8,16,64,256,576,1024,4096]
comc=[0,0,0,0,0,0,0,0]
imgdt=Image.open("DT.jpg")
imgez=Image.open("EZ.jpg")
imgfl=Image.open("FL.jpg")
imghd=Image.open("HD.jpg")
imghr=Image.open("HR.jpg")
imght=Image.open("HT.jpg")
imgnc=Image.open("NC.jpg")
imgso=Image.open("SO.jpg")
term=7
while modsafter>0:
	if modsafter<comb[term]:
		term-=1
	else:
		modsafter-=comb[term]
		comc[term]+=1
		term-=1

n=1
ycoor=0
if len(songname)>=58:
        ycoor=90
else:
        ycoor=50
        
if comc[0]==1:
	image.paste(imgez,(770,ycoor))
	n+=1
else:
	pass

if comc[1]==1:
	image.paste(imghd,(770+(n-1)%2*65,ycoor+(n-1)//2*65))
	n+=1
else:
	pass

if comc[2]==1:
	image.paste(imghr,(770+(n-1)%2*65,ycoor+(n-1)//2*65))
	n+=1
else:
	pass

if comc[3]==1:
	image.paste(imgdt,(770+(n-1)%2*65,ycoor+(n-1)//2*65))
	n+=1
else:
	pass

if comc[4]==1:
	image.paste(imght,(770+(n-1)%2*65,ycoor+(n-1)//2*65))
	n+=1
else:
	pass

if comc[5]==1:
	image.paste(imgnc,(770+(n-1)%2*65,ycoor+(n-1)//2*65))
	n+=1
else:
	pass

if comc[6]==1:
	image.paste(imgfl,(770+(n-1)%2*65,ycoor+(n-1)//2*65))
	n+=1
else:
	pass

if comc[7]==1:
	image.paste(imgso,(770+(n-1)%2*65,ycoor+(n-1)//2*65))
	n+=1
else:
	pass

localtime=time.asctime(time.localtime(time.time()))
draw.text((740,280),localtime,font=font12,fill=(255,255,255))

if optiontosave.lower()=="y":
        data=open("BP-Record.txt",'a')
        print(str(time.time())+'\t'+str(round(scores[item]['pp'],2))+'\t'+str((page-1)*100+item+1)+'\t'+str(ID)+'\t'+module,file=data)
        data.close()
elif optiontosave.lower()=="n":
        pass

image.save('result.png')
image.show()
