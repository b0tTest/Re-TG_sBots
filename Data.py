from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to rename documents and files with certain other features.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Support Channel ✨", url="https://t.me/mytestbotz")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Other bots ♥", url="https://t.me/Mybotzlist")],
        #[InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
Just send a document / video to start renaming. Then when asked, give the new name for the file. The bot will download the file and upload with new name.

1) To have a custom thumbnail on your file, add an 'jpg' image as thumbnail using /thumbnail command.
2) By default, videos are uploaded as videos. To prompt the bot to upload video as document, use /settings to change settings.

    """

    # About Message
    ABOUT = """
**About This Bot** 




Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)


    """
