import os
from mcstatus import MinecraftServer
from server_tools import try_wake_server, check_server_up

class CommandHandler(object):

    def __init__(self, SERVER_TYPE):
        self.SERVER_TYPE = SERVER_TYPE
        self.mc_server = MinecraftServer.lookup("aloeil.ddns.net")
        self.minecraft_commands = [
            ('ping', self._minecraft_ping, 'RPI'),
            ('list', self._minecraft_list, 'RPI'),
            ('count', self._minecraft_count, 'RPI'),
        ]
        self.server_commands = [
            ('ping', self._server_ping, 'RPI'),
            ('boot', self._server_boot, 'RPI'),
            ('poweroff', self._server_poweroff, 'TOWER'),
        ]

    async def launch_command(self, ctx, command: str, command_list):
        command = command.lower()
        for command_data in command_list:
            if command_data[0] == command:
                break
        else:
            if self.SERVER_TYPE == 'RPI':
                return await ctx.send(f'Unrecognised command: `{command}`')

        if command_data[2] != self.SERVER_TYPE:
            return

        try:
            return await command_data[1](ctx)
        except Exception as e:
            await ctx.send(f'Command `{command}` failed: `{str(e)}`')




    """
    Minecraft commands
    """

    async def minecraft_command(self, ctx, command: str):
        await self.launch_command(ctx, command, self.minecraft_commands)

    async def _minecraft_ping(self, ctx):
        time = self.mc_server.ping()
        await ctx.send(f'Server is up and responded in {time} ms')

    async def _minecraft_count(self, ctx):
        status = self.mc_server.status()
        count, maxi = status.players.online, status.players.max
        await ctx.send(f'There is {count}/{maxi} players')

    async def _minecraft_list(self, ctx):
        query = self.mc_server.query()
        names = [f'\n - {name}' for name in query.players.names]
        await ctx.send(f'Players:{"".join(names)}')

    """
    Server commands
    """

    async def server_command(self, ctx, command: str):
        await self.launch_command(ctx, command, self.server_commands)

    async def _server_ping(self, ctx):
        if check_server_up():
            await ctx.send("Server is up !")
        else:
            await ctx.send("Server seems to be offline !")

    async def _server_boot(self, ctx):
        try_wake_server()
        await ctx.send("Sent WOL packet, startup may take 1-2 min !")

    async def _server_poweroff(self, ctx):
        if self.SERVER_TYPE == 'TOWER':
            await ctx.send("Shutting down server !")
            os.system('poweroff')
