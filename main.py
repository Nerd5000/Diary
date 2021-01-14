from database_manager import closeConn
from controler import *


def main():
    while True:
        choice = int(input('''
        =======================
        1- Get Titles.
        2- Get Diary.
        3- Add Diary.
        4- Delete Diary.
        5- Update Diary.    
        6- Exit.   
        Choice: '''))
        if choice == 1:
            printTitles()
        elif choice == 2:
            printDiary()
        elif choice == 3:
            addDiary()
        elif choice == 4:
            removeDiary()
        elif choice == 5:
            changeDiary()
        elif choice == 6:
            closeConn()
            break


if __name__ == "__main__":
    initializeDatabase()
    main()
