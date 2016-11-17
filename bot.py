import botogram


bot = botogram.create("277452410:AAFGQ4SDIYcHRxfB9iI55crZVwJgIL2lN8A")


@bot.command("add")
def add_command(chat, message, args):
    """Add url for check"""
    chat.send("Add url for check")


@bot.command("remove")
def remove_command(chat, message, args):
    """Remove url from check"""
    chat.send("Remove url for check")


@bot.command("list")
def list_command(chat, message, args):
    """List urls for check"""
    chat.send("List url for check")


if __name__ == "__main__":
    bot.run()
