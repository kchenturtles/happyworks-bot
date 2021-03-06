# -------------------------------import----------------------------------#
import logging
from client import *
#import slashcommands
# -----------------------------------------------------------------------#


# Logging errors
logging.basicConfig(level=logging.ERROR)


# -------------------------------variables-------------------------------#
client = Client() # from client.py (this contains everything needed for the bot to function)

# -----------------------------------------------------------------------#


# -----------------------------slash commands----------------------------#
#slashcommands.init_slashcommands(client) # defines all your slash command functions

# -----------------------------------------------------------------------#


# -------------------------------launch bot------------------------------#
try:
    with open('token.txt') as f:
        TOKEN = f.readline() # bot token in git ignored file
except: pass
# try:
# except: pass
client.run(TOKEN)
# -----------------------------------------------------------------------#
