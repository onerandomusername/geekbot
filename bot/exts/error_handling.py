from discord.ext import commands
from bot import Bot
import verboselogs
import logging

log: verboselogs.VerboseLogger = logging.getLogger(__name__)
class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: Bot):
        self.bot = bot


    @commands.command()
    async def throw(self, ctx: commands.Context):
        raise Exception

    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler"""
        log.error(error)
        await ctx.send('something went wrong')


def setup(bot: Bot):
    bot.add_cog(ErrorHandler(bot))
