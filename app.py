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


teams = {"Fruity Punch": [], "Bannana Split": []}

@app.route('/assign_group', methods=['POST'])
def assign_group():
    data = request.json
    name = data['name']
    
    # Randomly assign the person to a team
    chosen_team = random.choice(['Fruity Punch', 'Bannana Split'])
    
    # Re-balance teams if needed
    other_team = 'Bannana Split' if chosen_team == 'Fruity Punch' else 'Fruity Punch'
    if len(teams[chosen_team]) > len(teams[other_team]):
        chosen_team = other_team
    
    # Add the person to the chosen team
    teams[chosen_team].append(name)
    
    return jsonify({'teams': teams})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
