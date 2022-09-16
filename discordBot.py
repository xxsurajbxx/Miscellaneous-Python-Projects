import discord
import csv

# pyinstaller --onefile discordBot.py

MEMBER_ROLE_ID = 0

BOT_CMD_CHANNEL_ID = 0

IMPORTANT_CATEGORY_ID = 0
ADMIN_CATEGORY_ID = 0
DONT_TOUCH_THESE_CATEGORIES = {IMPORTANT_CATEGORY_ID, ADMIN_CATEGORY_ID}

CREATE_A_VC_CHANNEL_ID = 0

created_VCs=[]
stats = []
class MyClient(discord.Client):
    async def on_ready(self):
        with open('Tracker.csv', 'r') as file:
            x = csv.reader(file)
            for line in x:
                stats.append(line)
        await client.change_presence(activity=discord.Game(name="by myself :("), status=discord.Status.dnd, afk=False)
        print("Ready...")

    async def on_message(self, message):
        isMod = False
        for role in message.author.roles:
            if role.permissions.administrator:
                isMod=True
        if isMod and len(message.content) and message.content[0]=='!':
            if message.content=='!help':
                await message.channel.send("Commands:\n!dc - Disconnects me :(\n!startup - People can now message in text channels and join voice channels\n!shutdown - nobody can message in text channels or join voice channels\n!registerTeam - creates a team so that you can keep track of wins and losses\n!addWin - records a win for a registered team\n!addLoss - records a loss for a registered team\n!stats - displays stats for a specified team")
            elif message.channel.id==BOT_CMD_CHANNEL_ID:
                if message.content=="!dc":
                    await message.channel.send("See you later...")
                    await discord.Client.logout(self);
                    with open('Tracker.csv', 'w') as file:
                        w = csv.writer(file)
                        for row in stats:
                            w.writerow(row)
                    print("disconnected\n")


                elif message.content=="!shutdown":
                    print(f'shutting down {message.guild.name} server: ')
                    await message.channel.send("working on it...")
                    for vc in created_VCs:
                        if vc.guild.id==message.guild.id:
                            created_VCs.remove(vc)
                            await vc.delete()
                    for chan in message.guild.channels:
                        if chan.category_id not in DONT_TOUCH_THESE_CATEGORIES:
                            await chan.set_permissions(chan.guild.get_role(MEMBER_ROLE_ID), send_messages=False, connect=False, send_tts_messages=False, embed_links=False, attach_files=False)
                            print(f'\t{chan.name} is done')
                    await message.channel.send("Server has been shutdown")
                    print("Server has been shutdown\n")


                elif message.content=="!startup":
                    print(f'starting up {message.guild.name} server: ')
                    await message.channel.send("working on it...")
                    for chan in message.guild.channels:
                        if chan.category_id not in DONT_TOUCH_THESE_CATEGORIES:
                            await chan.set_permissions(chan.guild.get_role(MEMBER_ROLE_ID), send_messages=True, connect=True, send_tts_messages=False, embed_links=False, attach_files=False)
                            print(f'\t{chan.name} is done')
                    await message.channel.send("Server has been started")
                    print("Server has been started\n")
                else:
                    await message.channel.send('I don\'t recognize that command\nType "!help" to get a list of commands')
            else:
                words = message.content.split()
                teamname=""
                for w in words:
                    if w!=words[0]:
                        teamname+=w
                        teamname+='_'
                teamname = teamname[:-1]
                if words[0]=="!registerTeam":
                    if len(words)<2:
                        await message.channel.send('to use this function, you must type "!registerTeam" followed by a space and the name of the team')
                    else:
                        stats.append([teamname, '0', '0', '.'])
                        await message.channel.send('done')
                elif words[0]=="!addWin":
                    if len(words)<2:
                        await message.channel.send('to use this function, you must type "!addWin" followed by a space and the name of the registered team')
                    else:
                        flag = True
                        for team in stats:
                            if team[0]==teamname:
                                team[1] = str(int(team[1])+1)
                                if int(team[2])!=0:
                                    team[3] = str(float(team[1])/float(team[2]))
                                flag=False
                                await message.channel.send("done")
                                break;
                        if flag:
                            await message.channel.send("couldn't find that team, make sure that there isn't a typo")
                elif words[0]=="!addLoss":
                    if len(words)<2:
                        await message.channel.send('to use this function, you must type "!addLoss" followed by a space and the name of the registered team')
                    else:
                        flag = True
                        for team in stats:
                            if team[0]==teamname:
                                team[2] = str(int(team[2])+1)
                                team[3] = str(float(team[1])/float(team[2]))
                                flag = False
                                await message.channel.send("done")
                                break;
                        if flag:
                            await message.channel.send("couldn't find that team, make sure that there isn't a typo")
                elif words[0]=="!stats":
                    if len(words)<2:
                        await message.channel.send('to use this function, you must type "!stats" followed by a space and the name of the registered team')
                    else:
                        flag = True
                        for team in stats:
                            if team[0]==teamname:
                                teamname=""
                                for x in team[0]:
                                    if x!='_':
                                        teamname+=x
                                    else:
                                        teamname+=' '
                                flag = False
                                wlr = team[3]
                                if wlr=='.':
                                    wlr='0'
                                else:
                                    wlr = "{:.2f}".format(float(team[3]))
                                await message.channel.send(f'{teamname}\nWins: {team[1]}\nLosses: {team[2]}\nWins/Losses: {wlr}')
                                break;
                        if flag:
                            await message.channel.send("couldn't find that team, make sure that there isn't a typo")
                            
    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None and after.channel.id==CREATE_A_VC_CHANNEL_ID:
            new_VC = await after.channel.guild.create_voice_channel(f'{member.display_name}\'s VC')
            created_VCs.append(new_VC)
            await member.move_to(new_VC)
            print(f'creating VC for {member.display_name}')
        if before.channel is not None and before.channel in created_VCs:
            if len(before.channel.members)==0:
                created_VCs.remove(before.channel)
                await before.channel.delete()
                print(f'deleted {before.channel.name}')
        if before.channel is not None and before.channel!=after.channel:
            print(f'{member.display_name} left {before.channel.name}')
        if after.channel is not None and before.channel!=after.channel:
            print(f'{member.display_name} joined {after.channel.name}')
        

client = MyClient()
client.run('ODE2NzMyODQzNTQ3NTU3OTM4.YD_PvA._r9ih0BWt9AUJedbY3TXLD8lUII')
