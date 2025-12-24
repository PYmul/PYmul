from pymul.core.os_detect import detect_os
from pymul.commands.install import install_package

def dispatch(args):
    command = args[0]
    target = args[1] if len(args) > 1 else None

    os_name = detect_os()

    if command == "install" and target:
        install_package(target, os_name)
    else:
        print("Unknown command")