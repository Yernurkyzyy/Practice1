import json
import os

def load_json(filename, default):
    if not os.path.exists(filename):
        return default
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def get_settings():
    return load_json("settings.json", {"sound": True, "car_color": "red", "difficulty": 1})

def save_score(name, score, distance):
    scores = load_json("leaderboard.json", [])
    scores.append({"name": name, "score": score, "distance": distance})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:10]
    save_json("leaderboard.json", scores)