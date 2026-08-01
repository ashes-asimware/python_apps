import repocommands as rc


class RepoManager:
    def __init__(self):
        self.commands = rc.git_commands

    def execute_command(self, command_name, *args):
        if command_name in self.commands:
            command_function = self.commands[command_name]
            return command_function(*args)
        else:
            raise ValueError(f"Command '{command_name}' not found in git commands.")


rm = RepoManager()
# Example usage:
print(rm.execute_command("clone", "https://github.com/user/repo.git", "/path/to/clone"))
