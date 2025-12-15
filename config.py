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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BAGCdMkAlXGEITuudCOEPZhl2jYikf6Y9Y9SNZcRv8yOjZqfx9M3k-mHJg1m4o7Kz7hbFdJ8OBPwC9AMFF-o44tXDqYbONlVxXx6gliqrN1tcCu0vCf9Fh2DateIK2-ZKNpXe9ibULZ3eI791PZRk2xP0-qV79RUHleXLcDwBpPHj9n38U18vf-2paVsRmKOohkT1RNoCkMvq22G5-F2RtKs1GYmjO7WzxXu1skCwP2dO9mWnZZ673tkzxk2VzY9e5Ef_gf8N7v56YOclpT5IOMwRWsvBPudRQZNUShAqHHVkEJS1dRCpgXefCCJ0lri7pmEDPd23CfQ4TA9QB000eDDX_hu3QAAAAHEWVRoAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
