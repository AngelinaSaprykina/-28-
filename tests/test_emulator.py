import os

from src.emulator import ShellEmulator

def test_parse_command():
    """Проверить команду и ее аргументы."""
    emulator = ShellEmulator()

    command, args = emulator.parse_command(
        "ls file1 file2"
    )

    assert command == "ls"
    assert args == ["file1", "file2"]


def test_empty_command():
    """Проверить пустой ввод."""
    emulator = ShellEmulator()

    command, args = emulator.parse_command("")

    assert command == ""
    assert args == []


def test_environment_variable():
    """Проверить раскрытие переменной окружения."""
    emulator = ShellEmulator()
    os.environ["TEST_VAR"] = "documents"

    command, args = emulator.parse_command(
        "cd $TEST_VAR"
    )

    assert command == "cd"
    assert args == ["documents"]