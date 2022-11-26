from env import Env

class Bot:

    state = 0

    def start():
        Bot.state = 1

    def stop():
        Bot.state = 0

    def is_turned_on():
        return Bot.state == 1

    def get_state():
        return Bot.state

    def is_command(commands,name):
        for command in commands:
            command = Env.get_env('COMMAND_PREFIX') + command.name
            if name == command:
                return True
        return False