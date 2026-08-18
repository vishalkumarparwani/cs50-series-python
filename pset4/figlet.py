import sys
import random
import pyfiglet


def main():
    if len(sys.argv) == 1:
        font = random.choice(pyfiglet.FigletFont.getFonts())

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid Usage")

        if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit("Invalid Usage")

        font = sys.argv[2]

    else:
        sys.exit("Invalid Usage")

    text = input("Input: ")

    print(pyfiglet.figlet_format(text, font=font))


if __name__ == "__main__":
    main()
