import os


def check_if_root():
    if os.geteuid() == 0:
        return True
    else:
        print("Error: Are you running as root?")
        exit(1)