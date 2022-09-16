import discord
import sys

# pyinstaller --onefile startup.pyw
GUILD_ID = 0

MEMBER_ROLE_ID = 0

BOT_CMD_CHANNEL_ID = 0

IMPORTANT_CATEGORY_ID = 0
ADMIN_CATEGORY_ID = 0
DONT_TOUCH_THESE_CATEGORIES = {IMPORTANT_CATEGORY_ID, ADMIN_CATEGORY_ID}

class MyClient(discord.Client):
    async def on_ready(self):
        guild = None
        for g in self.guilds:
            if g.id == GUILD_ID:
                guild = g
        for chan in guild.channels:
            if chan.category_id not in DONT_TOUCH_THESE_CATEGORIES:
                await chan.set_permissions(chan.guild.get_role(MEMBER_ROLE_ID), send_messages=True, connect=True, send_tts_messages=False, embed_links=False, attach_files=False)
        await self.logout()

client = MyClient()
client.run('ODE2NzMyODQzNTQ3NTU3OTM4.YD_PvA._r9ih0BWt9AUJedbY3TXLD8lUII')
