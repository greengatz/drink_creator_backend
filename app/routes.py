from app import app
from flask import request

from . import drink_creator

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

@app.route('/drinks')
def drinks():
    spirit = request.args.get('spirit')
    mixer = request.args.get('mixer')
    type = request.args.get('type')
    return drink_creator.generateDrink(spirit, mixer, type)