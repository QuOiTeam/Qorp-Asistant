# Импорт основных библиотек 


import disnake
from disnake.ext import commands
from disnake.utils import get

import os
import json
import discord

# Обозначение бота

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    activity=disnake.Game("QA (V 1.SB.6)", status=disnake.Status.online)
)

# Удаление команды "помощи"

bot.remove_command("help")

# Создание json файла с предупреждениями

if not os.path.exists("user.json"):
    with open("user.json", 'w') as file:
        file.write("{}")

# Запуск бота

@bot.event
async def on_ready():
    print(" ")
    print("┌[ ВАШ БОТ АКТИВИРОВАН ]")
    print(f"├[Имя бота: ➤ {bot.user.name}]")
    print(f"├[Версия бота: ➤ 01.SB.6.0]")
    print(f"├[Разработчик: ➤ QuOi]")
    print(f"└[ID бота: ➤ {bot.user.id}]")
    print(" ")
    
    for guild in bot.guilds:
        for member in guild.members:
            with open("user.json", 'r') as file:
                data = json.load(file)

            with open("user.json", 'w') as file:
                data[str(member.id)] = {
                    "WARNS": 0,
                    "CAPS": 0
                }
                json.dump(data, file, indent=4)
        
        
# Переписываю команду "помощи"
@bot.slash_command(name="help", description="Выводит список команд")
async def help(inter):
    message = disnake.Embed(title="Основные команды", description='''Реестр команд:
    **/help** - Выводит список команд
    **/ban** - Банит пользователя
    **/unban** - Анбанит пользователя
    **/timeout** - Отправляет пользователя в таймаут
    **/untimeout** - Отменяет таймаут пользователю
    **/clear [количество сообщений]** *(только для администрации)* - удаляет сообщения 
    **/recruit** - Отправить заявку на пост управляющего
    **/verify** - Пройти верификацию
    ''', color=990000)
    
    await inter.response.send_message(embed=message)
    
# Импорт "когов" в бота

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
        
# Обозначение токена бота

token = open("token.txt", 'r').readline()

# Старт работы

bot.run(token)
