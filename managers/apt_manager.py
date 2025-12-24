import subprocess
from pymul.managers.base import BaseManager

class AptManager(BaseManager):
    def install(self, package):
        subprocess.run(["sudo", "apt", "install", "-y", f"python3-{package}"])