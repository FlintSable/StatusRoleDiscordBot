import nextcord
import os
from dotenv import load_dotenv, dotenv_values


load_dotenv()

from flask import Flask

client = nextcord.Client(intents = nextcord.Intents.all())

server_id = 1090432408492462222

custom_status = "https://discord.gg/hNGt755M"

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_presence_update(before, after):
    print("running again")
    guild = client.get_guild(server_id)
    role = nextcord.utils.find(lambda r: r.name == 'custom_role', guild.roles)
    print(role)
    print(str(after.name))
    # if str(after.activity) == custom_status:
    await after.add_roles(role)
    print("run end \n")

my_secret = os.getenv('DISCORD_TOKEN')
client.run(my_secret)

app = Flask(__name__)
@app.route('/')
def index():
    return "Bot up and running"

app.run(host="0.0.0.0", debug=True, port=8080)


# def main():
#     client = discord.Client(intents = discord.Intents.all())

#     server_id = 1090432408492462222
#     custom_status = "https://discord.gg/hNGt755M"

#     @client.event
#     async def on_read():
#         print("we have logged in as {0.user}".format(client))

#     #client.event
#     async def on_presence_update(before, after):
#         guild = client.get_guild(server_id)
#         role = discord.utils.find(lambda r: r.name == 'custom_role', guild.roles)
#         if str(after.activity) == custom_status:
#             await after.add_roles(role)
    
#     my_secret = os.getenv('DISCORD_TOKEN')
#     client.run(my_secret)
#     # return 0





# if __name__ == '__main__':
#   main()
#   app = Flask(__name__)
#   @app.route('/')
#   def index():
#      return "Bot up and running"
#   app.run(host="0.0.0.0", debug=True, port=8080)


# if __name__ == '__main__':
    # main()