#!/usr/bin/python3

# BP1~100 on Akatsuki shown with images
# Author: Murmurtwins

from PIL import Image,ImageDraw,ImageFont,ImageFilter
from io import BytesIO
import requests, json, math
import cv2

page=8
url='http://akatsuki.pw/api/v1/users/scores/best?mode=0&p='+str(page)+'&l=100&rx=1&id=4391'
url2='https://akatsuki.pw/api/v1/users/rxfull?id=4391'
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
font2=ImageFont.truetype('ARLRDBD.ttf',150)
font21=ImageFont.truetype('ARLRDBD.ttf',36)
font22=ImageFont.truetype('ARLRDBD.ttf',24)
font3=ImageFont.truetype('digifaw.ttf',32)
font4=ImageFont.truetype('GOTHIC.ttf',65)
font41=ImageFont.truetype('GOTHIC.ttf',50)

item=26
url11='https://assets.ppy.sh/beatmaps/'
setid=str(scores[item]['beatmap']['beatmapset_id'])
url12='/covers/cover.jpg'
fullurl=url11+setid+url12

response=requests.get(fullurl)
response=response.content
BytesIOOBj=BytesIO()
BytesIOOBj.write(response)
img=Image.open(BytesIOOBj)
img=Image.blend(img,image2,0.7)
image.paste(img,(0,50))
draw=ImageDraw.Draw(image)

itemdes='Your BP'+str((page-1)*100+item+1)+' is:'

draw.text((10,8),itemdes,font=font1,fill=(0,0,0))

score=scores[item]['score']
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
songname=scores[item]['beatmap']['song_name']
player='Player: '+name
box=(0,0,260,256)

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

image.save('result.png')
image.show()