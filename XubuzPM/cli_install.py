import sys
from .misc import check_if_root

def check_package_availability():
    pass

def install_package(i):
    check_package_availability(i)
    print(f"installing package: {i}")

def check_install_options(i):
    print(f"checking options in install subcommand: {i}")


def cli_install():
    #check_if_root()

    if len(sys.argv) == 2:
        print("Error: You must give atleast one argument. See 'xpm help install'")
    else:
        for i in sys.argv[2:]:
            if i[0] == "-":
                check_install_options(i)
            else:
                install_package(i)