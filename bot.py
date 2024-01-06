import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

@bot.slash_command(
        name = 'kickall',
        description = "Kicks all members that don't have a role"
)
async def kickall(ctx):
    if not ctx.author.guild_permissions.kick_members:
        return await ctx.send('You do not have the required permissions')    
        
    for member in ctx.guild.members:
        if member.roles:
            try:
                await member.kick(reason = 'Kicking all members without roles')
                await ctx.send(f'Kicked {member.display_name}')
                
            except discord.Forbidden:
                await ctx.send(f'Failed to kick {member.display_name} due to missing permissions.')
                continue
                
            except discord.HTTPException as e:
                await ctx.send(f'Failed to kick {member.display_name}')
        else:
            pass        



bot.run('TOKEN')
