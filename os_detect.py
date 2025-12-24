import platform

def detect_os():
    system = platform.system().lower()

    if "windows" in system:
        return "windows"
    elif "linux" in system:
        return "linux"
    elif "darwin" in system:
        return "macos"
    else:
        return "unknown"