import sqlite3
import datetime
from diarymock import Diary

conn = sqlite3.connect('DiaryData.db')

c=conn.cursor()

try:
    c.execute("""CREATE TABLE diaries(
                date text,
                subject text,
                body text
                )
        """)
    conn.commit()
except:
    pass
def insertDiary(dia):
    with conn:
        c.execute("INSERT INTO diaries VALUES (:date, :subject, :body)", 
        {'date': dia.date, 'subject': dia.subject, 'body': dia.body})


def getDiaryBySubject(subject):
    c.execute("SELECT * FROM diaries WHERE subject=:subject", {'subject': subject})
    return c.fetchall()


def updateBody(dia, body):
    with conn:
        c.execute("""UPDATE diaries SET body = :body
                    WHERE subject = :subject""",
                  {'body': body, 'subject': emp.subject})


def removeDiary(dia):
    with conn:
        c.execute("DELETE from diaries WHERE subject = :subject AND body = :body",
                  {'subject': dia.subject, 'body': dia.body})



# d=datetime.datetime.today()
# subject = input('Enter a Subject : ')
# body = input('Enter a Body : ')
# dia = Diary(d,subject,body)
# removeDiary(dia)    
# print(getDiaryBySubject('hello Python'))
