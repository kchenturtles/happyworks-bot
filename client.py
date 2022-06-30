import discord

class Client(discord.Client):
    # -------------------------------"Global" Variables:-------------------------------#
    # for example:
    # MELUMI = 640714673045504020  # my discord id
    # ----------------------------------------------------------------------------------#

    async def on_ready(self):
        activity = discord.Activity(type=discord.ActivityType.listening,
                                    name="My Chemical Romance")  
        await self.change_presence(activity=activity)
        print('bot online')
    
    async def on_message(self, message):
        if message.author == self.user:  
            return
        
        message_lower = message.content.lower()

        if "hi" in message_lower:
            await message.channel.send("heyo")
