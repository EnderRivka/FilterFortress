from discord import *
TOKEN = 'insert token here'
client = Client()
CURSEWORDS = (open("badwords.txt","r").read()).split()
LGBT = ["gay","lesbian","transgender","queer"]
client.filtercursewords = {}
client.customfilter = {}
client.lgbt = {}
@client.event
async def on_message(message):#filters
    if message.author == client.user:
        return
    try:
        print(client.customfilter[message.guild.id])
    except:
        client.filtercursewords[message.guild.id] = False
        client.lgbt[message.guild.id] = False
        client.customfilter[message.guild.id] = []
    if message.author.roles[len(message.author.roles)-1].permissions.administrator == True:#looks at user's highest role, and sees if it's administrator
        if message.content.startswith("!help"):
            await message.channel.send("Do !filter <word> to filter a word")
            await message.channel.send("Do !unfilter <word> to unfilter a word")
            await message.channel.send("Do !filtered to see what is filtered")
            await message.channel.send("Do !clearfilter to clear the custom filter")
            await message.channel.send("Do !allowcursing to allow cursing")
            await message.channel.send("Do !disallowcursing to disallow cursing")
            await message.channel.send("Do !allow.lgbt to allow talk about lgbt topics")
            await message.channel.send("Do !disallowlgbt to disallow talk about lgbt topics")
            return
        if message.content.startswith('!disallowcursing'):
            if client.filtercursewords[message.guild.id] == False:
                client.filtercursewords[message.guild.id] = True
                await message.channel.send("Cursing is now filtered")
            else:
                await message.channel.send("Cursing was already filtered")
            return
        if message.content.startswith('!allowcursing'):
            if client.filtercursewords[message.guild.id] == True:
                client.filtercursewords[message.guild.id] = False
                await message.channel.send("Cursing is now allowed")
                return
            else:
                await message.channel.send("Cursing was already allowed")

        if message.content.startswith('!disallowlgbt'):
            if client.lgbt[message.guild.id] == False:
                client.lgbt[message.guild.id] = True
                await message.channel.send("LGBT conversation is now filtered")
            else:
                await message.channel.send("LGBT was already filtered")
            return
        if message.content.startswith('!allowlgbt'):
            if client.lgbt[message.guild.id] == True:
                client.lgbt[message.guild.id] = False
                await message.channel.send("LGBT conversation is now allowed")
                return
            else:
                await message.channel.send("LGBT was already allowed")
        if message.content.startswith('!clearfilter'):
            if len(client.customfilter[message.guild.id]) > 0:
                client.customfilter[message.guild.id] = []
                await message.channel.send("Your custom filter has been cleared")
            else:
                await message.channel.send("Your custom filter is empty")
        if message.content.startswith('!filtered'):
            if len(client.customfilter[message.guild.id]) > 0:
                await message.channel.send(", ".join(client.customfilter[message.guild.id]))
            else:
                await message.channel.send("You have no custom words filtered. Do !filter <word> to add a word to the filter.")
            return
        if message.content.startswith('!filter'):
            if message.content.split()[1].lower() in client.customfilter[message.guild.id] or (message.content.split()[1].lower() in CURSEWORDS and client.filtercursewords[message.guild.id] == True):
                await message.channel.send("That is already filtered")
            elif len(message.content.split()) > 1:
                client.customfilter[message.guild.id].append(message.content.split()[1].lower())
                await message.channel.send(content=message.content.split()[1] + " is now filtered")
            else:
                await message.channel.send(content="You did not enter a word to be filtered. Use !filter <word>")
            return
        if message.content.startswith('!unfilter'):
            if len(message.content.split()) > 1:
                content = message.content.split()
                try:
                    client.customfilter[message.guild.id].remove(content[1])
                    await message.channel.send(content=content[1]+" is now unfiltered")
                except:
                    await message.channel.send(content = "That isn't filtered")
            else:
                await message.channel.send(content="You did not enter a word to be unfiltered. Use !unfilter <word>")
            return
        if client.filtercursewords[message.guild.id] == True:
            for word in CURSEWORDS:
                if word in "".join(message.content.split()).lower():
                    await message.delete()
                    await message.channel.send(content = "What you said was filtered, {0.author.mention}".format(message))
                    return
        if client.lgbt[message.guild.id] == True:
            for word in LGBT:
                if word in "".join(message.content.split()).lower():
                    await message.delete()
                    await message.channel.send(content = "What you said was filtered, {0.author.mention}".format(message))
                    return
        for word in client.customfilter[message.guild.id]:
            if word in "".join(message.content.split()).lower():
                await message.delete()
                await message.channel.send(content = "What you said was filtered, {0.author.mention}".format(message))
                return
    else:
        await message.channel.send("You do not have permissions to do that")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
client.run(TOKEN)