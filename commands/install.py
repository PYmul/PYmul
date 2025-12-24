from pymul.managers.pip_manager import PipManager
from pymul.managers.apt_manager import AptManager
from pymul.managers.brew_manager import BrewManager
from pymul.managers.choco_manager import ChocoManager

def install_package(package, os_name):
    if os_name == "windows":
        manager = PipManager()
    elif os_name == "linux":
        manager = AptManager()
    elif os_name == "macos":
        manager = BrewManager()
    else:
        print("Unsupported OS")
        return

    manager.install(package)