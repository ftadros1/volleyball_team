from flask import Flask, request, jsonify
import random

app = Flask(__name__)


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
    app.run()
