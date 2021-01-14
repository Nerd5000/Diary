import sqlite3
from model import Diary

conn = sqlite3.connect('diary.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


# diary['title']
# diary['id']
# diary['body']


def initializeDatabase():
    cursor.execute(
        'create table if not exists diary(id integer not null primary key autoincrement, title text, body text)')


def getDiary(id):
    cursor.execute('select * from diary where id=:id', {'id': id})
    diary = cursor.fetchone()
    return diary


def getTitles():
    titles = cursor.execute('select title, id from diary')
    return titles


def insertDiary(diary):
    cursor.execute('insert into diary(title,body)values(:title,:body)', {
                   'title': diary.title, 'body': diary.body})
    conn.commit()


def deleteDiary(id):
    cursor.execute('delete from diary where id=:id', {'id': id})
    conn.commit()


def updateDiary(Diary):
    cursor.execute('update diary set title=:title, body=:body where id=:id', {
                   'title': Diary.title, 'body': Diary.body, 'id': Diary.id})
    conn.commit()


def closeConn():
    conn.commit()
    conn.close()
