import discord
from discord.ext import commands
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# intents = discord.Intents.default()
# intents.members = True

client = discord.Client(intents = discord.Intents.all())

# client = commands.Bot()

@client.event
async def on_ready():
    print("bot is ready")
    print("------------")

initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

print(initial_extensions)



if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

token = os.getenv('DISCORD_TOKEN')
client.run(token)