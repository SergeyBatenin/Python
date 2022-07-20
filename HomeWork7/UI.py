

import menu
import DB


def start():
    menu.view_main_menu()

    selection = menu.choice_user()
    if selection == 1:
        DB.print_db()
    elif selection == 2:        
        DB.add_user()
    elif selection == 3:
        DB.delete_user()
    elif selection == 4:
        DB.show_contact()
    elif selection == 5:
        DB.clear_db()
    elif selection == 6:
        DB.export_json()
    elif selection == 7:
        DB.import_json()
    elif selection == 8:
        print("До свидания")
        quit()


