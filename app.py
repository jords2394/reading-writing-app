
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Load progress data
def load_progress():
    if os.path.exists("data/progress.json"):
        with open("data/progress.json") as f:
            return json.load(f)
    return {"reading": 0, "writing": 0}

# Save progress
def save_progress(data):
    with open("data/progress.json", "w") as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reading')
def reading():
    return render_template("reading.html")

@app.route('/writing')
def writing():
    return render_template("writing.html")

@app.route('/update-progress', methods=["POST"])
def update_progress():
    data = load_progress()
    activity = request.json.get("activity")
    if activity in data:
        data[activity] += 1
    save_progress(data)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
