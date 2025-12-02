from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class JokeBot:
    def __init__(self):
        self.chat_agent = Agent("google-gla:gemini-2.5-flash", system_prompt="Ne a joking programming nerd, always answere with a programming joke. Also add in some emojis to make it funnier.")
        
        self.result = None
        
    def chat(self,prompt: str):
        # ternary operator to set message_history, or one line if-else statement
        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history)
        
        return {"user": prompt, "bot": self.result.output}
    

if __name__ == "__main__":
    # vi skapar en joke-bot instans, som en klass (boten är skickad in som self)
    bot = JokeBot()
    
    # kallar på metoden chat (bot är skickad in som self med 'bot.chat')
    result = bot.chat("Tell me a math joke?")
    result = bot.chat("hello thare")
    
    result = bot.chat("What did i ask you first?")
    print(result)
        