from .utils import getch
from . import color
from .escape import eraseLines, cursorMove, eraseBackspace
import sys
import string

def password(question="Password"):
    sys.stdout.write(color.white(question + " "))
    sys.stdout.flush()
    pwd = ""
    while True:
        ch = getch(True)
        # todo: multi byte character support
        if ch in string.printable[:-6]:
            pwd += ch
            sys.stdout.write("*")
            sys.stdout.flush()
        elif ch == '\r':
            sys.stdout.write("\n")
            return pwd;
        elif ch == "\x7f":
            sys.stdout.write(eraseBackspace(len(pwd)))
            pwd = pwd[:-1]
            sys.stdout.write("*" * len(pwd))
            sys.stdout.flush()
        else:
            continue

def checkbox():
    pass

def choice(question, choices):
    index = 1
    def print_choices():
        for n, i in enumerate(choices):
            if n == index:
                print(color.green(color.bold("> ") + i))
            else:
                print("  " + i)
    print(color.bold.cyan("? ") + question)
    print_choices()
    while True:
        ch = getch()
        if ch == "\033[A":
            index = (index - 1) % len(choices)
        elif ch == "\033[B":
            index = (index + 1) % len(choices)
        elif ch == "\r":
            sys.stdout.write(eraseLines(len(choices) + 1))
            sys.stdout.write(cursorMove(len(question) + 3, -1))
            print(color.cyan.bold(choices[index]))
            return index, choices[index]
        elif ch == "\003":
            raise KeyboardInterrupt
        else:
            continue
        print(eraseLines(len(choices) + 1), end="")
        print_choices()
