import discord
import requests
import os
import time
#from discord import message
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True



#bot = commands.Bot(command_prefix='!', intents=intents)

Client = discord.Client(intents=intents)
@Client.event
async def on_ready():
  print('we have new loggin from {Clinent.user}')
@Client.event
async def on_message(message):
  if message.author == Client.user:
    return
  if message.content.startswith("/hello bot"):
     await message.channel.send("wellcome")
     time.sleep(2)
     await message.channel.send(" write a nother command: \n 1-/photo codin \n 2-/your favorite language \n 3-/your club and where \n 4-/thank's i don't need this boot ")
     #message_2 = await message.channel.send("write a nother command")
  
  if message.content.startswith("1"):
    await message.channel.send("wait for uploaing your photo ...")
    time.sleep(2)
    send_photo_path = 'https://www.shutterstock.com/image-photo/business-man-computer-hand-close-260nw-2059017617.jpg'
    try:
      response = requests.get(send_photo_path)
      response.raise_for_status()

      os.makedirs('downloaded_images', exist_ok= True)

      with open('downloaded_images/codin.jpg', 'wb') as file:
                file.write(response.content)

      file = discord.File('downloaded_images/codin.jpg')
      await message.channel.send(file=file)
    except Exception as e:
      await message.channel.send(f"Error: {e}")
  if message.content.startswith("2"):
    time.sleep(1)
    await message.channel.send(" python ,dart,c++")
  if message.content.startswith("3"):
    time.sleep(1)
    await message.channel.send("i am in i tech club in skikda")
  if message.content.startswith("4"):
    time.sleep(1)
    await message.channel.send("ok ,you can call me in any time you want😃")

  
      

      
     
    
     
       
     
#@Client.event
#async def on_message1(message1):
  #if message1.author == Client.user:
    #return
#@Client.event
#async def on_message1(message1):
  #print('we have new role for bot')
  #if message1.author == Client.user:
    #return
  #if message1.content.startswith("/photo codin"):
       #await message1.channel.send(" wait for your photo.. ")
       #send_photo = r'C:\\disscord'
       #try:
         #file = discord.File(send_photo)
         #await message1.channel.send(file=file)
       #except Exception as e:
         #await message1.channel.send(f"error in your path: {e}")

    #async def send_photo(photo):
      #await photo.channel.send(send_photo)
 # await send_photo(send_photo)
    

  

Client.run('MTE4OTkzODgyODcyMzYyNjA2NA.GeNOmJ.S-MyB4kuM9LKUGTCST8rqUfQ2BiRlZ_bwTQoeI')