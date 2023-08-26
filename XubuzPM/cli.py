import sys

from . import cli_help
from .cli_install import cli_install
from .cli_update import sources_update
from .cli_upgrade import upgrade

def cli():
    if len(sys.argv) == 1:
        cli_help.main_help()
    else:
        if sys.argv[1] == "install":
            cli_install()
        elif sys.argv[1] == "help":
            cli_help.main_help()
        elif sys.argv[1] == "update":
            sources_update()
        elif sys.argv[1] == "upgrade":
            upgrade()
        elif sys.argv[1] == "--version":
            cli_help.version()
        else:
            print(f"Unknown Argument: {sys.argv[1]}")
            cli_help.main_help()
