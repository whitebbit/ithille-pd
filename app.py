import csv

import requests
from faker import Faker
from flask import Flask, jsonify, request
import flask

app = Flask(__name__)
fake = Faker()


@app.route('/requirements')
def requirements():
    with open('requirements.txt', 'r', encoding='utf-16') as file:
        requirements = [line.replace('\x00', '').strip() for line in file.readlines()]

    return flask.render_template('requirements.html', requirements=requirements)


@app.route('/users/generate', methods=['GET'])
def generate_users():
    try:
        count = int(request.args.get('count', 100))

        if count < 1:
            return jsonify({"error": "Count must be greater than 0"}), 400

        users = [{"name": fake.name(), "email": fake.email()} for _ in range(count)]

        return jsonify(users)

    except ValueError:
        return jsonify({"error": "Invalid count format"}), 400


@app.route('/mean')
def mean():
    with open('hw.csv', 'r') as file:
        csv_reader = list(csv.reader(file))

        total_height = [float(row[1]) for row in csv_reader[1:-1]]
        total_weight = [float(row[2]) for row in csv_reader[1:-1]]

        mean_height = sum(total_height) / len(total_height) if len(total_height) > 0 else 0
        mean_weight = sum(total_weight) / len(total_weight) if len(total_weight) > 0 else 0

    return flask.render_template('mean.html', mean_height=mean_height, mean_weight=mean_weight)


@app.route("/space")
def space():

    try:
        r = requests.get("http://api.open-notify.org/astros.json")
        data = r.json()
        return f"The number of astronauts in orbit: {data['number']}"
    except Exception:
        return jsonify({"error": "Connection error"}), 400


if __name__ == '__main__':
    app.run()
