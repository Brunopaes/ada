"""Handler telegram requisitions."""
from telebot import TeleBot

from ada.configs import TELEGRAM
from ada.processors import morse

bot = TeleBot(
    **TELEGRAM
)


@bot.message_handler(commands=["morse"])
def morse_handler(message):
    bot.send_message(
        message.chat.id,
        return_morse(message)
    )


def return_morse(message):
    """Middle function for calling morse package.

    Parameters
    ----------
    message : dict
        The message object.

    Returns
    -------
    morse: morse.morse_parser
        Morse parser function.

    """
    return morse.morse_parser(' '.join(message.text.split(' ')[1:]))


if __name__ == "__main__":
    while True:
        try:
            bot.polling()
        except Exception as error:
            error.args
