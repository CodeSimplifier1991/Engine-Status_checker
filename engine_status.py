# Initial command will be as an empty string message
get_theCommand = " "
message = " "

# At the start, the engine is not running
engine_running = False

# While the conditions below are true, the commands will be executed
while True:

    # The client enters a command and the command will be converted to lower cases letters
    get_theCommand = input("Enter your command: ").lower()

    # If the command is "START", the second condition will be checked
    if get_theCommand == 'start':

        # If the engine is already running, the client cannot start the engine again
        if engine_running:
            # The message will be shown on the console
            message = "Engine is already running"

        # If the condition above is not true
        else:
            # The engine will start, and the message will confirm it
            engine_running = True
            message = "Engine started!"

    # If the command equals to "STOP"
    elif get_theCommand == 'stop':

        # If the engine is not running already, the error message will be shown
        if not engine_running:
            message = "Engine already stopped"

        # And if the condition above is not true
        else:
            # The engine will be off and the confirming message will be shown on the console
            engine_running = False
            message = "Engine stopped!"

    # If the client needs help with the options and prints option as a command,
    elif get_theCommand == "help":

        # The possible options will be shown on the console to guide the client to choose from
        message = """
Start - To start the engine
Stop - To stop the engine
Quit - To quit the command line
Help - To get help option
        """
    # If the command is "QUIT", the programs will jumps out of the loop
    elif get_theCommand == "quit":
        break

    # If the command is invalid, the client will be notified and they will be asked to enter another command
    else:
        message = "Invalid command"

    # The final command will be shown on the console
    print(message)