import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트봇")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!하이포플러"):
        await message.channel.send("안녕하세요! 저는 파판14의 모든 정보를 지원하는 최첨단 인간지능 프로그램입니다. 무엇이든 물어보세요.")
    if message.content.startswith("!애드워드"):
        await message.channel.send("웨에에엥")
    if message.content.startswith("!바이포플러"):
        await message.channel.send("쫀밤되세요~")
    if message.content.startswith("!ㅎㅇㅍㅍㄹ"):
        await message.channel.send("안녕하세요! 저는 파판14의 모든 정보를 지원하는 최첨단 인간지능 프로그램입니다. 무엇이든 물어보세요.")
    if message.content.startswith("!영업종료"):
        await message.channel.send("하이포플러는 이만 퇴근합니다.")




client.run("NzU4OTU4Mzg2MTI0ODE2Mzk1.X22hFA.3I82jUHjZlDz1WZQAWHWLJIL5Ig")
