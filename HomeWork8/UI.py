

import menu
import db


def start():
    menu.view_main_menu()

    selection = menu.choice_user()
    if selection == 1:
        db.show_pupils()
    elif selection == 2:        
        db.show_parents()
    elif selection == 3:
        db.add_pupils()
    elif selection == 4:
        db.add_parents()
    elif selection == 5:
        db.find_parent()
    elif selection == 6:
        print("До свидания")
        quit()

