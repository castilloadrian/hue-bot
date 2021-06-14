from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_screen():
    return 'Welcome to Hue-Bot Adrian!'

@app.route('/on')
def on_screen():
    return 'All Hue lights are on!'

@app.route('/off')
def off_screen():
    return 'All Hue lights are off!'