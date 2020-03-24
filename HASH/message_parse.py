
class MessageHandler:
    def __init__(self, bot):
        self.client = bot
        self.pokeypy = bot.pokeypy
    
    async def handle_message(self, message):
        
        # Handles check if pokemon appers
        if self.pokeypy.check_message(message):
            await self.pokeypy.get_pokemon_name(message)
            return

        await self.client.process_commands(message)