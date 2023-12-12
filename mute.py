# Импорт библиотек

import datetime

import disnake
from disnake.ext import commands

# Основной код

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.slash_command(description="Лишить права голоса")
    @commands.has_permissions(administrator=True)
    async def timeout(self, interaction, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        mute_time = disnake.utils.format_dt(time, style="f")
        embed = disnake.Embed(title="Timeout", description=f"{member.mention} has been timed out until {mute_time}", color=990000)
        await interaction.response.send_message(f"{member.mention} muted for {time} for {reason}", ephemeral=True)
        
        
    # untimeout для пользователя
    
    @commands.slash_command(description="Снять ограничения голоса")
    @commands.has_permissions(administrator=True)
    async def untimeout(self, interaction, member: disnake.Member):
        await member.timeout(reason=None, until=None)
        await interaction.response.send_message(f"Untimed out {member.mention}", ephemeral=True)
    
    
        
def setup(bot):
    bot.add_cog(Timeout(bot))
    
