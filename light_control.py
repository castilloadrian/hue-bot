import os
from dotenv import load_dotenv, find_dotenv
from phue import Bridge

# Loads all enviroment variables in the .env file
load_dotenv(find_dotenv())

# Sets bridge IP address to variable set in .env file
BRIDGE_IP_ADDRESS = os.environ.get("BRIDGE_IP_ADDRESS")
b = Bridge(BRIDGE_IP_ADDRESS)

# This only needs to be ran once to get connected then comment it out. Press top button on Hue bridge
# b.connect()

# Gets all information needed from the hue bridge thats referenced in the ip address
b.get_api()

# Turn my room lights on
def turn_lights_on():
    b.set_light('Adrian 1','on', True)
    b.set_light('Adrian 2','on', True)

# Turn my room lights off
def turn_lights_off():
    b.set_light('Adrian 1','on', False)
    b.set_light('Adrian 2','on', False)