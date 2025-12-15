import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6474527080").split()))
OWNER_ID = int(getenv("OWNER_ID","7589155944"))
MONGO_URL = getenv("MONGO_URL","mongodb+srv://kranpant_db_user:kranpant_db_user@cluster0.xy6tc02.mongodb.net/?appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "6566448442:AAHPV-9OIMz9YB0LaGFCEXaZVjmHAQbRBIU")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BAFwyZ4AKvRayB-D-7S6QI1ZRKQxe4EummJbvGqj84rVPX2tzdbGLcNw8Hqn5d_WTFwWeb67EbbZ63EcsQ2fuTjaGAp7pPiLziEkeWMhYd48Syqdgd3hjxtXqPZo_t8hfyPp6C05uh2AMNelGIlNW5Wc8X1JY6atwazXWVnIfMuA87178yR6X-jLoS2mjWgqQZZ59_3uqSalApkCWNug7ZySEjGzW5DrUpdcuN9PUmUEV6wA1yDpd7BZIPacylOhCIz66Q4CYc9w0kTwncSOnGMrVy1VpXtYFcgfTG4atYk90RHEy66gPDpZiyoa0aFC8IqhyB9EiV_UuTVWFAopmW9ooBXn_wAAAAHEWVRoAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
