import botogram


bot = botogram.create("277452410:AAFGQ4SDIYcHRxfB9iI55crZVwJgIL2lN8A")


@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("Hello world")


if __name__ == "__main__":
    bot.run()
