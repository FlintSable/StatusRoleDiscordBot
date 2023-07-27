import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()




# intents = nextcord.Intents.default()
intents = nextcord.Intents.all()
intents.members = True
intents.presences = True
# test server id
# server_id = 1090432408492462222
# main server id
server_id = 1123332194245546034



client = commands.Bot(command_prefix = 'x', intents = intents)

# client = commands.Bot()

@client.event
async def on_ready():
    print("bot is ready")
    print("we have logged in as {0.user}".format(client))
    
    print("------------")

# @client.event
# async def on_presence_update(before, after):
#     print("running again")
#     guild = client.get_guild(server_id)
#     role = nextcord.utils.find(lambda r: r.name == 'custom_role', guild.roles)
#     print(role)
#     print(str(after.name))
#     # if str(after.activity) == custom_status:
#     await after.add_roles(role)
#     print("run end \n")


initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])


print(initial_extensions)




if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)
    # main()
    # app = Flask(__name__)
    # @app.route('/')
    # def index():
    #     return "Bot up and running"
    # app.run(host="0.0.0.0", debug=True, port=8080)


token = os.getenv('DISCORD_TOKEN')
client.run(token, reconnect=True)