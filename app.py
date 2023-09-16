from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

# New root route
@app.route('/')
def root():
    return "The app is running!"

group1 = []
group2 = []
teams = {"Team A": [], "Team B": []}

@app.route('/assign_group', methods=['POST'])
def assign_group():
    name = request.json.get('name')
    group = request.json.get('group')
    
    if group == "Group 1":
        group1.append(name)
    elif group == "Group 2":
        group2.append(name)
    else:
        return jsonify({"error": "Invalid group"})
        
    all_names = group1 + group2
    random.shuffle(all_names)
    
    teams["Team A"] = all_names[:len(all_names)//2]
    teams["Team B"] = all_names[len(all_names)//2:]
    
    return jsonify({"teams": teams})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
