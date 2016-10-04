from prompts import ui
from prompts import color

def main():

    print(ui.password("Enter you password"))
    # ui.prompt("")
    print(ui.choice("Gendar", ["Male", "Female", "Others"]))

    # ui.multi_choice("What ")

if __name__ == '__main__':
    main()
