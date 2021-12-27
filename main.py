import nextcord
from nextcord.ext import commands
from time import sleep as wait
import asyncio
import json 

intents = nextcord.Intents.default()
intents.members = True

ranks = {}

# goal: Create a customizable bot that allows an admin create roles based on invites 
#
# What could be improved: It indexes poorly. Instead of iterating through every invite with invites > 0, it iterates through 
# every member which would work poorly on large servers. A


f = open('config.json')
config = json.load(f)
token = config['token']


for i in config:
    if not i == 'token':
        ranks[int(i)] = int(config[i])



bot = commands.Bot(command_prefix='-')
client = nextcord.Client(intents=intents)


async def get_key(val):
    for key, value in ranks.items():
        if val == value:
             return int(key)
    return False


async def get_value_of_dict(dict):
    tmp = []
    for key,value in dict.items():
        tmp.append(int(value))
    return tmp

@client.event
async def on_message(message):
    if message.content.startswith('!syncinvites'):
        while True:
            print('[Log] Checking for any new status updates')
            invites = 0
            allmembers = message.guild.members
            print('[Log] Scanning all members, one moment...')
            for member in message.guild.members: # iterate through all members using var 'member'
                for i in await message.guild.invites(): # iterate through every invite link from every member
                    if i.inviter == member: # if the inviter of an invite LINK was that member...
                        invites += i.uses # ... iterate invite variable + the number of link uses
                
                
                if invites > 0:
                    print(f'[Log] {member} has {invites} invites')
                    totalinvites = invites
                    for key, value in reversed(ranks.items()):
                        if totalinvites >= key:
                            for role in member.roles:
                                if role.id in await get_value_of_dict(ranks) and await get_key(role.id) < key:
                                    role = message.guild.get_role(int(role.id))
                                    print(f'[Log] Removing Role "{role}"')
                                    await member.remove_roles(role)
                                #print(f'{member} has role {roles.id}')
                            
                            
                            role = message.guild.get_role(int(value)) # new instance of role, same variable because it made the most sense
                            if not role in member.roles:
                                print(f'[Log] {member} has at least {key} invites, giving them the role @{value}')
                                await member.add_roles(role)

                            return

            asyncio.sleep(60)

@client.event    
async def on_ready():
    print('[Log] Bot has authenticated and started successfully')
                

token = config['token']
try:
    client.run(token)
except:
    print('[ERROR] Token is incorrect')