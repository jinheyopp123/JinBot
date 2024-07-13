import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# 공지 채널 설정 저장을 위한 딕셔너리
announcement_channels = {}

@bot.event
async def on_ready():
    print(f'봇 이름: {bot.user.name}')
    print(f'봇 ID: {bot.user.id}')
    print('봇 준비 완료')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

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
    await ctx.send('https://github.com/jinheyopp123/JinBot | GitHub MIT 라이선스라 자유입니다 :)')

@bot.command()
async def ddos(ctx):
    await ctx.send('절대 안돼요')

@bot.command()
async def 개발자(ctx):
    await ctx.send('김진혁 제작')

@bot.command()
async def 개발내역(ctx):
    await ctx.send('현재 곧 개발이 완료됩니다.')

@bot.command()
async def 비밀메세지(ctx):
    await ctx.send('DM으로 비밀번호 요청을 하였습니다!')
    await ctx.author.send('비밀번호를 입력해주세요')

    def check(dm_message):
        return dm_message.author == ctx.author and isinstance(dm_message.channel, discord.DMChannel)

    try:
        dm_message = await bot.wait_for('message', check=check, timeout=60)  # 60초 대기
        if dm_message.content == '0821':
            await dm_message.channel.send('확인되었습니다.')
            embed = discord.Embed(title='비밀 메세지', description='알아서 하세요')
            await ctx.send(embed=embed)
        else:
            await ctx.send('비밀번호가 틀렸습니다.')
    except asyncio.TimeoutError:
        await ctx.send('시간이 초과되었습니다. 다시 시도해주세요.')

@bot.command()
@commands.has_permissions(kick_members=True)
async def 추방(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        if member:
            await ctx.send(f'{member.mention}을(를) 추방합니다.')
            await member.kick(reason=reason)
        else:
            await ctx.send('추방할 멤버를 멘션해주세요.')
    else:
        await ctx.send('권한이 부족합니다.')

@bot.command()
@commands.has_permissions(ban_members=True)
async def 밴(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        if member:
            await ctx.send(f'{member.mention}을(를) 밴합니다.')
            await member.ban(reason=reason)
        else:
            await ctx.send('밴할 멤버를 멘션해주세요.')
    else:
        await ctx.send('권한이 부족합니다.')

@bot.command()
@commands.has_permissions(administrator=True)
async def 공지채널설정(ctx, channel: discord.TextChannel):
    announcement_channels[ctx.guild.id] = channel.id
    await ctx.send(f'공지 채널이 {channel.mention}으로 설정되었습니다!')

bot.run('YOUR_BOT_TOKEN')
