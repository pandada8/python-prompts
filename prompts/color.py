import sys

ESC = "\033["

stylingMap = {
    "italic": "3",
    "highlight": "7",
    "dim": "2",
    "underline": "4",
    "bold": "1",
    "blink": "5",
    # fg
    "red": "31",
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    # bg
    "bgblack": "40",
    "bgred": "41",
    "bgblack": "40",
    "bgred": "41",
    "bggreen": "42",
    "bgyellow": "44",
    "bgblue": "44",
    "bgmagenta": "45",
    "bgcyan": "46",
    "bgwhite": "47",
}


class Color(object):
    def __init__(self):
        self.format = []

    def __getattr__(self, key):
        if key.startswith("__") or key == "format":
            return super(Color).__getattr__(self, key)

        if key.lower() not in stylingMap:
            print("fail to found map for {}".format(key))
            return self
        else:
            self.format.append(stylingMap[key.lower()])
            return self

    def __call__(self, text):
        ret = ESC + ";".join(self.format) + "m" + text + ESC + "0m"
        self.attr = []
        return ret

sys.modules[__name__] = Color()
