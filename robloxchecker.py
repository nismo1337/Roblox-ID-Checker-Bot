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
async def robloxinfo(ctx, id):
    userinfo = requests.get(url+id)
    userthumbnail = requests.get(thumbnail_url+id+'&size='+size+'&format='+format+'&isCircular='+is_circular)
    if userinfo.status_code == 200 and userthumbnail.status_code == 200:
        data = userinfo.json()
        username = data['name']
        display_name = data['displayName']
        description = data['description']
        thumbnail_data = userthumbnail.json()
        image_url = thumbnail_data['data'][0]['imageUrl']
        embed = discord.Embed(title=f'Roblox Information for User ID {id}', description=f'Username: {username}\nDisplay name: {display_name}\nDescription: {description}', color=0x00ff00)
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send('Error retrieving user information')

client.run("put ur bot token here:D")
