import discord
from discord.ext import commands
from model import ayırtEt

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def KiminBotusun(ctx):
    await ctx.send(f'ben Mehmet efenin botuyum ')
@bot.command()
async def emoji(ctx):
    await ctx.send("🤣")
@bot.event
async def on_message_delete(message):
    print(message.content)

@bot.event
async def on_typing(channel, user, when):
    await channel.send(f"{user.display_name} fazla vaktimi alma :(")


@bot.command()
async def upload_image(ctx):
    attachments = ctx.message.attachments
    if attachments:
      #print(files)
      for attachment in attachments:
         file_name = attachment.filename
         file_path = f"image/{file_name}"
         await attachment.save(file_path)
         await ctx.send("Dosya yükledin!")

         await ctx.send (ayırtEt("C:/Users/erdal/Desktop/Mehmet Efe/AIBot/keras_model.h5","C:/Users/erdal/Desktop/Mehmet Efe/AIBot/labels.txt",file_path))
         
    else:
      await ctx.send("Dosya yüklemedin!")
bot.run("Token")
