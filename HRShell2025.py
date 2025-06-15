import os
import sys
import socket
import subprocess
import platform
from datetime import datetime

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║   ██╗  ██╗██████╗ ███████╗██╗  ██╗███████╗██╗     ║
    ║   ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██║     ║
    ║   ███████║██████╔╝███████╗██████║█████╗  ██║     ║
    ║   ██╔══██║██╔═══╝ ╚════██║██╔══██║██╔══╝  ██║     ║
    ║   ██║  ██║██║     ███████║██║  ██║███████╗███████╗║
    ║   ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝║
    ║                                                    ║
    ║   Coded by Pakistani Ethical Hacker                 ║
    ║   Mr. Sabaz Ali Khan                               ║
    ║   Version: 2025.1.0                                ║
    ║   Date: June 15, 2025                              ║
    ╚════════════════════════════════════════════════════╝
    """
    print(banner)

def get_system_info():
    return {
        'OS': platform.system(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Architecture': platform.architecture()[0],
        'Hostname': socket.gethostname(),
        'IP': socket.gethostbyname(socket.gethostname()),
        'Current Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

def main():
    print_banner()
    print("\nWelcome to HRShell2025 - Ethical Hacking Command Shell")
    print("Type 'help' for available commands\n")

    while True:
        try:
            command = input(f"[HRShell2025@{get_system_info()['Hostname']}]# ")
            command = command.strip().lower()

            if command == 'exit':
                print("Exiting HRShell2025...")
                break
            elif command == 'help':
                print("""
Available Commands:
  sysinfo    - Display system information
  dir/ls     - List directory contents
  exec       - Execute system command
  clear/cls  - Clear screen
  exit       - Exit HRShell2025
                """)
            elif command in ['dir', 'ls']:
                print(execute_command('dir' if platform.system() == 'Windows' else 'ls -la'))
            elif command == 'sysinfo':
                info = get_system_info()
                for key, value in info.items():
                    print(f"{key}: {value}")
            elif command.startswith('exec '):
                cmd = command[5:].strip()
                if cmd:
                    print(execute_command(cmd))
                else:
                    print("Please provide a command to execute")
            elif command in ['clear', 'cls']:
                os.system('cls' if platform.system() == 'Windows' else 'clear')
                print_banner()
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit HRShell2025")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()