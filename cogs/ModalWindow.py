# Импорт основных библиотек

import disnake
from disnake.ext import commands

# Основной код

class RecruitementModal(disnake.ui.Modal):
    def __init__(self, arg):
        self.arg = arg  
       
        components = [
            disnake.ui.TextInput(label="Ваше настоящее имя", placeholder="Введите ваше настоящее имя", custom_id="name"),
            disnake.ui.TextInput(label="Ваш возраст", placeholder="Введите ваш возраст", custom_id="age"),
            disnake.ui.TextInput(label="Почему именно вы?", placeholder="Расскажите почему именно вас должны взять", custom_id="why_you")
        ]
        if self.arg == "moderator":
            title = "Набор на должность модератора"
        else:
            title = "Набор на должность администратора"
        super().__init__(title=title, components=components, custom_id="recruitementModal")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        name = interaction.text_values["name"]
        age = interaction.text_values["age"]
        why_you = interaction.text_values["why_you"]
        embed = disnake.Embed(color=0x2F3136, title="Заявка отправлена!")
        embed.description = f"{interaction.author.mention}, Благодарим вас за **заявку**! " \
                            f"Если вы нам **подходите**, администрация **свяжется** с вами в ближайшее время."
        embed.set_thumbnail(url=interaction.author.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        channel = interaction.guild.get_channel(...)  #ID канала куда будут отправляться заявки
        await channel.send(f"**Заявка на роль {self.arg}** от {interaction.author.mention}\n **Настоящее имя** - {name} **({age} лет)**\n **Резюме:**\n *{why_you}*")
        

class RecruitementSelect(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Модератор", value="moderator", description="Следящий за порядком чата"),
            disnake.SelectOption(label="Администратор", value="admin", description="Украшающий сервер"),
        ]
        super().__init__(
            placeholder="Выберите желаемую роль", options=options, min_values=0, max_values=1, custom_id="recruitement"
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(RecruitementModal(interaction.values[0]))


class Recruitement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.slash_command(description="Стань управляющим!")
    async def recruit(self, ctx):
        view = disnake.ui.View()
        view.add_item(RecruitementSelect())
                
        await ctx.send('Выберите желаемую роль', view=view, ephemeral=True)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(RecruitementSelect())
        self.bot.add_view(view,
                          message_id="...")  # Вставить ID сообщения, которое отправится после использования с команда !recruit


def setup(bot):
    bot.add_cog(Recruitement(bot))
