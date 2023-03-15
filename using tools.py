import time

# Define a function for using a spanner to fix vents
def fix_vents(player, spanner):
    print("You approach the vent and begin to use your spanner to fix it.")
    time.sleep(2)
    print("You tighten the bolts and adjust the vent cover, making sure it's secure.")
    time.sleep(2)
    print("You test the vent by blowing on it and feel the air flow through smoothly.")
    time.sleep(2)
    print("The vent is now fixed!")
    player.add_experience(50)
    spanner.use()


import time

# Define a function for splicing wires
def splice_wires(player, wire_stripper, wire1, wire2):
    print("You carefully strip the ends of the wires using your wire stripper.")
    time.sleep(2)
    print("You twist the exposed wire ends together and wrap them tightly with electrical tape.")
    time.sleep(2)
    print("The wires are now spliced together!")
    player.add_experience(50)
    wire_stripper.use()
    wire1.use()
    wire2.use()


# Define a function for customs registration
def register_customs(player):
    print("Welcome to the customs registration desk.")
    print("Please read and accept the following terms and conditions:")
    print("1. You are responsible for your actions in this MUD.")
    print("2. You must follow all rules and regulations set forth by the MUD administrators.")
    print("3. You must treat all other players with respect.")
    print("Do you accept these terms and conditions? (Y/N)")

    # Wait for player input
    while True:
        response = input("> ").lower()
        if response == "y":
            print("Thank you for registering with customs.")
            player.is_registered = True
            break
        elif response == "n":
            print("You cannot enter the MUD without accepting the terms and conditions.")
            print("Goodbye.")
            player.quit()
            break
        else:
            print("Invalid input. Please enter Y or N.")




