# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class Vegile(HackingTool):
    TITLE = "Vegile - Ghost In The Shell"
    DESCRIPTION = "This tool will set up your backdoor/rootkits when " \
                  "backdoor is already setup it will be \n" \
                  "hidden your specific process,unlimited your session in " \
                  "metasploit and transparent."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Vegile.git",
        "cd Vegile && sudo chmod +x Vegile"
    ]
    RUN_COMMANDS = ["cd Vegile && sudo bash Vegile"]
    PROJECT_URL = "https://github.com/Screetsec/Vegile"

    def before_run(self):
        os.system('echo "You can Use Command: \n'
                  '[!] Vegile -i / --inject [backdoor/rootkit] \n'
                  '[!] Vegile -u / --unlimited [backdoor/rootkit] \n'
                  '[!] Vegile -h / --help"|boxes -d parchment')


class ChromeKeyLogger(HackingTool):
    TITLE = "Chrome Keylogger"
    DESCRIPTION = "Hera Chrome Keylogger"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/HeraKeylogger.git",
        "cd HeraKeylogger && sudo apt-get install python3-pip -y && sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd HeraKeylogger && sudo python3 hera.py"]
    PROJECT_URL = "https://github.com/UndeadSec/HeraKeylogger"


class PostExploitationTools(HackingToolsCollection):
    TITLE = "Post exploitation tools"
    TOOLS = [
        Vegile(),
        ChromeKeyLogger()
    ]