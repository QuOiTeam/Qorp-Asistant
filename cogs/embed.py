# Импорт команд
import disnake
from disnake.ext import commands

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def embed(self, interaction):
        embed = disnake.Embed(title="Embed title", description="Embed description", color=0x00ff00)
        embed.add_field(name="Field 1", value="Value 1", inline=False)
        embed.add_field(name="Field 2", value="Value 2", inline=False)
        embed.add_field(name="Field 3", value="Value 3", inline=False)
        embed.set_footer(text="Embed footer")
        embed.set_author(name="Embed author")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Embed(bot))