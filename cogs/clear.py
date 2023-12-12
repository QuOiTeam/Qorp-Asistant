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
        embed.set_thumbnail(url="...")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
        
# Соединение команды с ботом

def setup(bot):
    bot.add_cog(Clear(bot))
