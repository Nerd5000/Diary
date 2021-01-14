from database_manager import getDiary, getTitles, initializeDatabase, insertDiary, updateDiary, deleteDiary
from model import Diary


def printTitles():
    for title in getTitles():
        print('{}- {}'.format(title['id'], title['title']))


def printDiary():
    id = int(input('Diary id: '))
    diary = getDiary(id)
    print('Title: {}'.format(diary['title']))
    print('Body: {}'.format(diary['body']))


def addDiary():
    title = input('Title: ')
    body = input('Body: ')
    insertDiary(Diary(id=0, title=title, body=body))


def removeDiary():
    id = int(input('Diary id: '))
    confirmation = input(
        '''You will delete diary that has {} as id
        Type y to delete: '''.format(id))
    if confirmation.lower() == 'y':
        deleteDiary(id)


def changeDiary():
    id = int(input('Diary id: '))
    title = input('New Title: ')
    body = input('New Body:')
    updateDiary(Diary(id, title, body))
