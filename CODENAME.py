import discord
import requests
from bs4 import BeautifulSoup
from discord import Game


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트봇")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!하이꽃튼"):
        await message.channel.send("안녕하세요! 저는 사사게친구들을 알려주는 똑똑한 봇입니다.")
    if message.content.startswith("!사사게후보"):
        await message.channel.send('다음 사사게 유력 후보는 "톤베리@파티장" 님입니다.')
    if message.content.startswith("!ssg"):
        print(message.content)
        q=message.content.split(' ')[1]
        searchpage = requests.get('http://www.inven.co.kr/board/ff14/4485?name=subjcont&keyword={}'.format(q))
        bsoup = BeautifulSoup(searchpage.content, 'html.parser')
        results = bsoup.findAll("a", attrs={"class":"sj_ln"})
        await message.channel.send('지금부터 사사게친구인지 알려줄께요!')
        for x in results[1:]:
            await message.channel.send(x["href"])
        if 0==len(results[1:]):
            await message.channel.send('안타깝게도 아직 사사게친구가 아니네요~')
    if message.content.startswith("!영업종료"):
        await message.channel.send("꼬튼은 이만 퇴근합니다.")
client.run("NzU5MDI2NjAyMDI1MDI1NTM3.X23gmw.qMdlQjqxFTNUYKx6Ox275drANag")
