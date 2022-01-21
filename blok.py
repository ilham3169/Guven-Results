from telethon import TelegramClient
import logging
import time
from telethon import events, Button
import requests
from bs4 import BeautifulSoup
import asyncio
import os
import time

"""
while x != 6646850:
	r = requests.get(f"https://netice.az/result?type=2&exam=637&class=11&group=1&sector=1&code={x}")
	soup = BeautifulSoup(r.content, "html.parser")
	ad = soup.findAll("div", {"class", "student_name"})
	soyad = soup.findAll("div", {"class", "student_surname"})
	bal = soup.findAll("div", {"class", "score"})
	is_nomresi = soup.findAll("div", {"class", "work_number"})
	if len(is_nomresi) == 1:
		x = x+1
		mesaj = f"{ad[0].text}:{soyad[0].text}:{bal[0].text}:{is_nomresi[0].text}"
		print(mesaj)
		file = open("data.txt", "a")
		file.write(f"\n{mesaj}")
		file.close()
	if len(is_nomresi) == 2:
		print(f"{x} 2 ədəd iş nömrəsi!")
	else:
		print(f"{x} iş nömrəli hesab yoxdur.! ❌")
		x = x+1
"""



api_id = 10097563 
api_hash = "55bebccb5fdf45b664bbafb454bf2d97"
bot = "5071498609:AAGfz_LgEs8uC75aHgctnsj9RORuexF5OZs"

client = TelegramClient("guvendb2", api_id, api_hash).start(bot_token= bot)
client = TelegramClient("blok", api_id = api_id, api_hash = api_hash).start()
entity = client.get_entity("https://t.me/+aNCo0DaC-14wZTY6")
@client.on(events.NewMessage(pattern = "/start"))
async def sent(event):
		counter  = 0
		x = 6670000
		while x != 0:
			r = requests.get(f"https://netice.az/result?type=2&exam=637&class=11&group=1&sector=1&code={x}")
			soup = BeautifulSoup(r.content, "html.parser")
			ad = soup.findAll("div", {"class", "student_name"})
			soyad = soup.findAll("div", {"class", "student_surname"})
			bal = soup.findAll("div", {"class", "score"})
			is_nomresi = soup.findAll("div", {"class", "work_number"})
			if len(is_nomresi) == 1:
				x = x-1
				mesaj = f"{ad[0].text}:{soyad[0].text}:{bal[0].text}:{is_nomresi[0].text}"
				print(mesaj)
				file = open("data.txt", "a")
				file.write(f"\n{mesaj}")
				file.close()
				
			if len(is_nomresi) == 2:
				print(f"{x} 2 ədəd iş nömrəsi!")
			else:
				print(f"{x} iş nömrəli hesab yoxdur.! ❌")
				x = x-1
			
			counter = counter+1
			
			if counter == 50:
				try:
					await client.send_file("guvenblok", "data.txt")
					counter = 0
				except:
					await event.reply(".txt boşdur")
			else:
				pass



client.run_until_disconnected()


