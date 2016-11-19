import logging
import botogram
import db

logging.basicConfig(level=logging.INFO)

bot = botogram.create("277452410:AAFGQ4SDIYcHRxfB9iI55crZVwJgIL2lN8A")


@bot.command("add")
def add_command(chat, message, args):
    """Add url for check"""

    if len(args) == 1:
        db.add_url(chat.id, args[0])
        chat.send("Ok")

    else:
        chat.send("Enter valid url")


@bot.command("remove")
def remove_command(chat, message, args):
    """Remove url from check"""

    if len(args) == 1:
        db.remove_url(chat.id, args[0])
        chat.send("Ok")

    else:
        chat.send("Enter valid url")


@bot.command("list")
def list_command(chat, message, args):
    """List urls for check"""

    url_list = db.get_url_list(chat.id)

    msg = '\n'.join(url_list)

    chat.send(msg)


if __name__ == "__main__":
    bot.run()
