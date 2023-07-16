
import nextcord
from nextcord.ext import tasks, commands
import asyncio

class RoleChange(commands.Cog):
    
    def __init__(self, client):
        print('cog initiated')
        self._server_id = 1090432408492462222
        self._client = client
        self._guild = client.get_guild(self._server_id)
        print(client.get_guild(1090432408492462222))
    

    # event
    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        print("custom listener")
        # guild = Client.get_guild(self._server_id)
        print(after.activity)
        role = nextcord.utils.find(lambda r: r.name == 'custom_role', self._client.get_guild(1090432408492462222).roles)
        print(role)
        if role not in before.roles and str(after.activity) == "https://discord.gg/hNGt755M":
            print("doesn't have role but has requirement custom status")
            await after.add_roles(role)
            
        print("\n")
        await asyncio.sleep(2)




    # # command
    # @commands.command(self)
    # async def add_custom_role(ctx):
    #     await ctx.send('added')

    # @commands.has_role("custom_role")
    # async def check_custom_role(ctx, user: discord.Member):
    #     role = discord.utils.find(lambda r: r.name == 'custom_role', guild.roles)
    #     if role in user.roles:
    #         return True
    #     else:
    #         return False
    # @add_custom_role.error
    # async def add_custom_role_error(ctx, error):
    #     guild = client.get_guild(server_id)

    #     await ctx.send("You don't have permission to add roles")
def setup(client):
    client.add_cog(RoleChange(client))

