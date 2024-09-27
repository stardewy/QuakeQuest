import random
import json

def get_game_logic():
    items = ["key", "flashlight", "map"] #Example palang toooo
    selected_item = random.choice(items)
    return json.dumps({"item": selected_item})

# To make the function callable, define a simple interface
if __name__ == "__main__":
    print(get_game_logic())