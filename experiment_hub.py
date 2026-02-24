from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


EXPERIMENTS = {
    "1": {
        "name": "Socket chat server",
        "cwd": BASE_DIR,
        "command": [sys.executable, "experiments/socket_chat/chat_server.py"],
    },
    "2": {
        "name": "Socket chat client",
        "cwd": BASE_DIR,
        "command": [sys.executable, "experiments/socket_chat/chat_client.py"],
    },
    "3": {
        "name": "HTTP API basic chatbot",
        "cwd": BASE_DIR,
        "command": [sys.executable, "experiments/http_api/simple_api_server.py"],
    },
    "4": {
        "name": "Django chatbot prototype",
        "cwd": BASE_DIR / "experiments" / "django_chat",
        "command": [sys.executable, "manage.py", "runserver"],
    },
    "5": {
        "name": "Python script runner GUI",
        "cwd": BASE_DIR,
        "command": [sys.executable, "experiments/script_runner/ejecutor.py"],
    },
}


def print_menu() -> None:
    print("\n=== chatbotFiles Experiment Hub ===")
    for key, exp in EXPERIMENTS.items():
        print(f"{key}. {exp['name']}")
    print("0. Exit")


def run_experiment(option: str) -> None:
    experiment = EXPERIMENTS[option]
    cmd = experiment["command"]
    cwd = experiment["cwd"]

    print(f"\nRunning: {experiment['name']}")
    print(f"Command: {' '.join(cmd)}")
    print(f"CWD: {cwd}\n")

    env = os.environ.copy()
    subprocess.run(cmd, cwd=str(cwd), env=env, check=False)


def main() -> None:
    while True:
        print_menu()
        option = input("Select experiment: ").strip()

        if option == "0":
            print("Goodbye")
            return

        if option not in EXPERIMENTS:
            print("Invalid option")
            continue

        run_experiment(option)


if __name__ == "__main__":
    main()
