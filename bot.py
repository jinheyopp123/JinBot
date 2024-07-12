import discord
from discord.ext import commands

# 봇 인스턴스 생성
intents = discord.Intents.default()
intents.message_content = True  # MESSAGE CONTENT INTENT 활성화
bot = commands.Bot(command_prefix='!', intents=intents)

# 봇 준비 이벤트
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# "안녕" 메시지에 응답 및 "임베드" 메시지에 임베드 응답
@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '안녕':
        await message.channel.send('안녕하세요!')

    if message.content.lower() == '디도스':  # "디도스" 메시지에 응답
        await message.channel.send('ㄴㄴㄴㄴㄴ')
    
    if message.content.lower() == '임베드':  # "임베드" 메시지에 임베드 메시지 전송
        embed = discord.Embed(title="테스트", description="테스트중입니다")
        await message.channel.send(embed=embed)

# 예제 명령어
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='라이선스')
async def hello(ctx):
    await ctx.send('https://github.com/jinheyopp123/JinBot|GitHub MIT라이선스라 자유입니다 :)')

@bot.command(name='ddos')
async def hello(ctx):
    await ctx.send('절대 안돼요')

@bot.command(name='개발자')
async def hello(ctx):
    await ctx.send('김진혁 제작')


# 하드코딩된 봇 토큰으로 봇 실행
TOKEN = 'YOUR_TOKEN'
bot.run(TOKEN)
