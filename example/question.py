from prompts import ui
from prompts import color

def main():

    ui.password("Enter you password")
    ui.prompt("")
    ui.choice("Gendar", ["Male", "Female", "Others"])
    ui.multi_choice("What ")
