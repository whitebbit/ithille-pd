import sqlite3

from flask import Flask, jsonify
import database as db

app = Flask(__name__)


@app.route('/names/', methods=['GET'])
def unique_names():
    conn = sqlite3.connect(db.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT first_name) FROM customers")
    result = cursor.fetchone()
    conn.close()
    return jsonify({'count': result[0]})


@app.route('/tracks/', methods=['GET'])
def track_count():
    conn = sqlite3.connect(db.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tracks")
    result = cursor.fetchone()
    conn.close()
    return jsonify({'count': result[0]})


@app.route('/tracks-sec/', methods=['GET'])
def track_info():
    conn = sqlite3.connect(db.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, artist, duration_seconds, release_date FROM tracks")
    tracks = cursor.fetchall()
    conn.close()
    track_info_list = [{'id': row[0], 'artist': row[1], 'duration_seconds': row[2], 'release_date': row[3]} for row in
                       tracks]
    return jsonify({'tracks': track_info_list})


if __name__ == '__main__':
    app.run()
