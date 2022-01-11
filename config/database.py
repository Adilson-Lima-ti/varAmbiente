import os
from dotenv import load_dotenv

load_dotenv()

var1="Modularizando variável"

database_infos = {
    "database" : os.getenv('DATABASE'),
    "port": os.getenv('PORT'),
    "user": os.getenv('USERNAMEDB'),
    "password": os.getenv('PASSWORD')
}