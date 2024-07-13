import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'봇 이름: {bot.user.name}')
    print(f'봇 ID: {bot.user.id}')
    print('봇 준비 완료')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '안녕':
        await message.channel.send('안녕하세요!')

    if message.content.lower() == '디도스':
        await message.channel.send('ㄴㄴㄴㄴㄴ')

    if message.content.lower() == '임베드':
        embed = discord.Embed(title='테스트', description='테스트중입니다')
        await message.channel.send(embed=embed)

    if message.content.lower() == '임베드2':
        embed = discord.Embed(title='없는데요?', description='없다고요')
        await message.channel.send(embed=embed)

@bot.command()
async def hello(ctx):
    await ctx.send('안녕하세요!')

@bot.command()
async def 라이선스(ctx):
    await ctx.send('https://github.com/jinheyopp123/JinBot | GitHub MIT라이선스라 자유입니다 :)')

@bot.command()
async def ddos(ctx):
    await ctx.send('절대 안돼요')

@bot.command()
async def 개발자(ctx):
    await ctx.send('김진혁 제작')

@bot.command()
async def 개발내역(ctx):
    await ctx.send('현재 곧 개발이 완료됩니다.')

# 봇 토큰을 여기에 입력하세요.
TOKEN = 'YOUR_TOKEN'
bot.run(TOKEN)

