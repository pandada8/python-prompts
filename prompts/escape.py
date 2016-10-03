import base64
ESC = "\033["

def cursorUp(row=1):
    return ESC + str(row) + "A" if row > 0 else ""

def cursorDown(row=1):
    return ESC + str(row) + "B" if row > 0 else ""

def cursorForward(column=1):
    return ESC + str(column) + "C" if column > 0 else ""

def cursorUp(column=1):
    return ESC + str(column) + "D" if column > 0 else ""

def cursorMove(x=0, y=0):
    ret = ""
    if x > 0:
        ret += "\033[{}D".format(x)
    elif x < 0:
        ret += "\033[{}C".format(-x)
    if y > 0:
        ret += "\033[{}B".format(y)
    elif y < 0:
        ret += "\033[{}D".format(-y)
    return ret

def cursorTo(x=0, y=0):
    if x != 0 and y != 0:
        return ESC + str(x) + ";" + str(y) + "H"
    else:
        return ""

cursorLeft = ESC + "1000D"  # big number!
cursorHead = cursorLeft
cursorSavePosition = ESC + 's'
cursorRestorePosition = ESC + 'u'
cursorGetPosition = ESC + '6n'
cursorNextLine = ESC + 'E'
cursorPrevLine = ESC + 'F'
cursorHide = ESC + '?25l'
cursorShow = ESC + '?25h'

beep = "\007"
clearScreen = ESC + 'c'

def eraseLines(count):
    return [cursorHead + eraseEndLine] * count.join(cursorUp(1))

eraseEndLine = ESC + 'K'
eraseStartLine = ESC + '1K'
eraseLine = ESC + '2K'
eraseDown = ESC + 'J'
eraseUp = ESC + '1J'
eraseScreen = ESC + '2J'
scrollUp = ESC + 'S'
scrollDown = ESC + 'T'

def image(content, width=None, height=None, preseveAspectRatio=True):
    """ iterm2 image """
    ret = ESC + "1337;File=inline=1"
    if width != None:
        ret += ";width=" + str(width)
    if height != None:
        ret += ";height=" + str(height)
    if not preseveAspectRatio:
        ret += ";preserveAspectRatio=0"
    return ret + ":" + base64.b64encode(content) + "\007"

__all__.remove("base64")
