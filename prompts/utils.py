import termios
import sys
import tty

def getch(exception=False):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        if ch == '\033':
            # fix: state machine for escape code
            ch += sys.stdin.read(2)
        if ch == '\003' and exception:
            raise KeyboardInterrupt
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
