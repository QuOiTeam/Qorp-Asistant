# Импорт основных библиотек

import disnake
from disnake.ext import commands

# Создание класса и команды

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.slash_command(description="Бан пользователя")
    @commands.has_permissions(administrator=True)
    async def ban(self, interaction, user: disnake.User, *, reason=None):
        await interaction.guild.ban(user, reason=reason)
        await interaction.response.send_message(f"{user.mention} has been baned!", ephemeral=True)
        
        
    @commands.slash_command(description="Разбан пользователя")
    @commands.has_permissions(administrator=True)
    async def unban(self, interaction, user: disnake.User):
        await interaction.guild.unban(user)
        await interaction.response.send_message(f"{user.mention} has been unbaned!", ephemeral=True)
        
    
def setup(bot):
    bot.add_cog(Ban(bot))
        

# Тут мы используем disnake.User - это пользователь Discord, то есть вы можете забанить человека, который даже не находится на сервере. 
# В варианте disnake.Member - пользователь обязательно должен находиться на сервере