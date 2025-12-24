import sys
from pymul.core.dispatcher import dispatch

def main():
    if len(sys.argv) < 2:
        print("Usage: pymul <command> <target>")
        sys.exit(1)

    dispatch(sys.argv[1:])

if __name__ == "__main__":
    main()