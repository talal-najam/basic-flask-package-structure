from flask import render_template, jsonify, request, url_for, redirect
from FlaskMongo import app
from FlaskMongo.models import User


@app.route('/something', methods=['GET, POST'])
def index():
    if request.type == 'POST':
        user_data = request.get_json()
        username = user_data['username']
        password = user_data['password']

        newUser = {}

        newUser['username'] = username
        newUser['password'] = password
        return jsonify(newUser)
    
    return jsonify({'Hero': 'Arc Warden'})