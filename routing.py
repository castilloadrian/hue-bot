from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_screen():
    return render_template('index.html')

@app.route('/on')
def on_screen():
    return 'All Hue lights are on!'

@app.route('/off')
def off_screen():
    return 'All Hue lights are off!'