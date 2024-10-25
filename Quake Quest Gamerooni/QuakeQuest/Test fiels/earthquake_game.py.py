$ pip install Flask
from flask import Flask, render_template, request
import random
import time
app = Flask(__name__)

# Game Settings
class GameSettings:
    def __init__(self):
        self.mainshock_duration = 5  # Duration of the shaking effect in seconds
        self.retry_limit = 3  # Number of retries for negative outcomes

# Game State
class GameState:
    def __init__(self):
        self.current_scene = 1
        self.background_image = "living_room.jpg"
        self.monologue = ""
        self.narration = ""
        self.puzzles = {}
        self.inventory = []

# Initialize the game state
game_settings = GameSettings()
game_state = GameState()

@app.route('/')
def index():
    return render_template('index.html', background=game_state.background_image, 
                           monologue=game_state.monologue, 
                           narration=game_state.narration)

@app.route('/next', methods=['POST'])
def next_scene():
    if game_state.current_scene == 1:
        setup_scene_1()
    elif game_state.current_scene == 2:
        setup_scene_2()
    elif game_state.current_scene == 3:
        setup_scene_3()
    return render_template('index.html', background=game_state.background_image, 
                           monologue=game_state.monologue, 
                           narration=game_state.narration)

def setup_scene_1():
    game_state.current_scene = 1
    game_state.background_image = "living_room.jpg"
    game_state.monologue = "Home sweet home."
    game_state.narration = ("It’s been a week since my grandparents asked me to house-sit. "
                            "It’s closer to my college, so I gladly took up the offer. "
                            "The area is safe, and conveniently, there’s a church nearby.")

def setup_scene_2():
    game_state.current_scene = 2
    game_state.background_image = "study.jpg"
    game_state.monologue = "Aha. Could the key be in here?"
    game_state.narration = "It’s locked. Classic. But knowing lolo, there are probably some hints around the room to open this."

    # Define puzzles
    game_state.puzzles = {
        "drawer": {"locked": True, "solution": "board"},
        "computer": {"locked": True, "password": "prepared for incoming destruction"}
    }

def setup_scene_3():
    game_state.current_scene = 3
    game_state.background_image = "living_room_shaking.jpg"
    game_state.monologue = "Wait, what is happening?!"
    game_state.narration = "The room is shaking! Plates are falling down!"

@app.route('/interact', methods=['POST'])
def interact():
    action = request.form.get('action')
    if action == 'inspect_drawer':
        return handle_drawer_interaction()
    elif action == 'unlock_drawer':
        return handle_drawer_unlock()
    elif action == 'input_password':
        return handle_password_input()
    return render_template('index.html', background=game_state.background_image, 
                           monologue=game_state.monologue, 
                           narration=game_state.narration)

def handle_drawer_interaction():
    if game_state.puzzles["drawer"]["locked"]:
        game_state.monologue = "It's locked. I need to find the code."
    else:
        game_state.monologue = "The drawer is open! What's inside?"
    return render_template('index.html', background=game_state.background_image, 
                           monologue=game_state.monologue, 
                           narration=game_state.narration)

def handle_drawer_unlock():
    # Simulating unlocking the drawer with the correct code
    # Placeholder check for demo
    code = request.form.get('code')
    if code == "board":
        game_state.puzzles["drawer"]["locked"] = False
        game_state.monologue = "The drawer is now unlocked!"
    else:
        game_state.monologue = "Wrong code. Try again."
    return render_template('index.html', background=game_state.background_image, 
                           monologue=game_state.monologue, 
                           narration=game_state.narration)

def handle_password_input():
    # Check the password input for the computer
    password = request.form.get('password')
    if password == game_state.puzzles["computer"]["password"]:
        game_state.puzzles["computer"]["locked"] = False
        game_state.monologue = "The computer is now unlocked!"
    else:
        game_state.monologue = "Incorrect password. Try again."
    return render_template('index.html', background=game_state.background_image, 
                           monologue=game_state.monologue, 
                           narration=game_state.narration)

if __name__ == '__main__':
    app.run(debug=True)
