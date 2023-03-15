# Define a Quest class to represent each individual quest
class Quest:
    def __init__(self, name, description, prerequisites, completion_message):
        self.name = name
        self.description = description
        self.prerequisites = prerequisites
        self.completion_message = completion_message
        self.completed = False

    # Check if the player has completed all prerequisites for the quest
    def is_available(self, player):
        for prerequisite in self.prerequisites:
            if prerequisite not in player.completed_quests:
                return False
        return True

    # Complete the quest and print the completion message
    def complete(self, player):
        player.completed_quests.append(self.name)
        self.completed = True
        print(self.completion_message)

# Define a Player class to represent each individual player
class Player:
    def __init__(self, name):
        self.name = name
        self.completed_quests = []

# Define a list of available quests
quests = [
    Quest(
        name="Kill the Goblin King",
        description="The Goblin King has been terrorizing the nearby village. Slay him and bring back proof of his demise.",
        prerequisites=[],
        completion_message="You have successfully defeated the Goblin King! The villagers are overjoyed and reward you with a bag of gold."
    ),
    Quest(
        name="The Lost Treasure",
        description="Legend has it that a great treasure was buried long ago in the forest. Find the treasure and bring back proof of your discovery.",
        prerequisites=["Kill the Goblin King"],
        completion_message="You have found the Lost Treasure! Your pockets are now lined with gold and jewels."
    ),
]

# Create a new player
player = Player(name="Bob")

# Game loop
while True:
    # Display the available quests to the player
    available_quests = [quest for quest in quests if quest.is_available(player)]
    if not available_quests:
        print("You have completed all available quests!")
        break
    else:
        print("Available Quests:")
        for quest in available_quests:
            print(quest.name)
        print()

    # Ask the player to choose a quest
    chosen_quest_name = input("Choose a quest to accept: ")
    chosen_quest = next((quest for quest in available_quests if quest.name == chosen_quest_name), None)
    if chosen_quest is None:
        print("Invalid quest name. Please choose an available quest.")
        continue

    # Start the chosen quest
    print(f"You have accepted the quest: {chosen_quest.name}")
    print(chosen_quest.description)
    input("Press enter to begin the quest...")
    chosen_quest.complete(player)
    print()

# Game over
print("Thanks for playing!")
