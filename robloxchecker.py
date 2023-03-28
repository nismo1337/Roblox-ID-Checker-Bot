import os
import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

thumbnail_url = 'https://thumbnails.roblox.com/v1/users/avatar?userIds='
url = 'https://users.roblox.com/v1/users/'
size = '420x420' # Sizes: 720x720, 420x420, 352x552...
format = 'Png' # Png or Jpeg
is_circular = 'false' # Determines if the thumbnail is Circular or not

@client.command()
async def robloxinfo(ctx, username):
    try:
        id = requests.get(url+'get-by-username?username='+username).json()['id']
        userinfo = requests.get(url+id)
        if userinfo.status_code == 200:
            data = userinfo.json()
            username = data['name']
            display_name = data['displayName']
            description = data['description']
            await ctx.send(f'Username: {username}\nDisplay name: {display_name}\nDescription: {description}')
        else:
            await ctx.send('Error retrieving user info')

        userthumbnail = requests.get(thumbnail_url+id+'&size='+size+'&format='+format+'&isCircular='+is_circular)
        if userthumbnail.status_code == 200:
            data = userthumbnail.json()
            image = data['data'][0]['imageUrl']
            await ctx.send(image)
        else:
            await ctx.send('Error retrieving user thumbnail')
    except:
        await ctx.send('Error: Invalid username or unable to retrieve user info')

client.run("put ur bot token here :D")
