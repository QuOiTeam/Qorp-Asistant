# Импорт команд

import disnake
from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Создание самой команды
    
    @commands.slash_command(description="Очистка сообщений")
    @commands.has_permissions(administrator=True)
    async def clear(self, interaction, amount: int):
        # Отправка эмбед сообщения после удаления
        await interaction.channel.purge(limit=amount + 1)
        
        embed = disnake.Embed(title="Clear", description=f"Удалено {amount} сообщений", color=990000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1150101252093509635/1184141878225023028/CLEAR-12-12-2023.png?ex=658ae510&is=65787010&hm=12029b7425701bab5ff18f83e2818a6b43cef9da328c0222d2eb54bdc6bbff6d&=&format=webp&quality=lossless&width=1020&height=398")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
        
# Соединение команды с ботом

def setup(bot):
    bot.add_cog(Clear(bot))