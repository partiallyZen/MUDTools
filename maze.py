import random

# Define a function for the personality maze
def personality_maze(player):
    print("Welcome to the personality maze!")
    print("In this maze, your decisions will determine your personality traits.")

    # Define a dictionary to keep track of the player's personality traits
    personality = {
        "kindness": 0,
        "courage": 0,
        "wisdom": 0,
        "loyalty": 0,
    }

    # Define a list of personality questions and answers
    questions = [
        {
            "question": "You see a stranger in need on the side of the road. What do you do?",
            "answers": {
                "a": "Stop and help them.",
                "b": "Keep walking and mind your own business.",
            },
            "traits": {
                "kindness": 1,
            }
        },
        {
            "question": "You encounter a dangerous situation. What do you do?",
            "answers": {
                "a": "Face the danger head-on.",
                "b": "Run away and hide.",
            },
            "traits": {
                "courage": 1,
            }
        },
        {
            "question": "You are faced with a difficult decision. What do you do?",
            "answers": {
                "a": "Consult with others and gather information before deciding.",
                "b": "Make a quick decision based on your instincts.",
            },
            "traits": {
                "wisdom": 1,
            }
        },
        {
            "question": "Your friend needs your help, but you have plans with someone else. What do you do?",
            "answers": {
                "a": "Cancel your plans and help your friend.",
                "b": "Stick to your plans and let your friend handle their own problems.",
            },
            "traits": {
                "loyalty": 1,
            }
        },
    ]

    # Shuffle the questions to randomize their order
    random.shuffle(questions)

    # Loop through the questions and prompt the player for their answers
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for ans in q['answers']:
            print(f"{ans.upper()}: {q['answers'][ans]}")
        while True:
            response = input("> ").lower()
            if response in q['answers']:
                break
            else:
                print("Invalid input. Please enter a valid answer.")

        # Update the player's personality traits based on their answer
        for trait in q['traits']:
            personality[trait] += q['traits'][trait] if response == trait else 0

    # Determine the player's personality type based on their personality traits
    personality_type = ""
    if personality['kindness'] > personality['courage']:
        personality_type += "compassionate"
    else:
        personality_type += "brave"
    if personality['wisdom'] > personality['loyalty']:
        personality_type += " and wise"
    else:
        personality_type += " and loyal"

    # Print out the player's personality type
    print(f"Congratulations, {player.name}! You have completed the personality maze.")
    print(f"Your personality type is: {personality_type}.")
