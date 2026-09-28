import getpass
import os
import socket

class ShellEmulator:
    """Эмулятор командной оболочки."""

    def __init__(self):
        """Получить данные реальной операционной системы."""
        self.username = getpass.getuser()
        self.hostname = socket.gethostname()
        self.running = True

    def get_prompt(self):
        """Сформировать приглашение командной строки."""
        return f"{self.username}@{self.hostname}:~$ "

    def parse_command(self, user_input):
        """Разобрать пользовательский ввод."""
        user_input = os.path.expandvars(user_input)

        if "$HOME" in user_input:
            home = os.path.expanduser("~")
            user_input = user_input.replace("$HOME", home)

        parts = user_input.split()

        if not parts:
            return "", []

        command = parts[0]
        args = parts[1:]

        return command, args

    def command_stub(self, command, args):
        """Вывести имя команды-заглушки и ее аргументы."""
        print(command, *args)

    def execute_command(self, command, args):
        """Выполнить введенную команду."""
        if command == "ls":
            self.command_stub(command, args)

        elif command == "cd":
            self.command_stub(command, args)

        elif command == "exit":
            self.running = False

        else:
            print(f"{command}: command not found")

    def run(self):
        """Запустить интерактивный режим."""
        while self.running:
            try:
                user_input = input(self.get_prompt())
            except (KeyboardInterrupt, EOFError):
                print()
                break

            command, args = self.parse_command(user_input)

            if not command:
                continue

            self.execute_command(command, args)

if __name__ == "__main__":
    emulator = ShellEmulator()
    emulator.run()