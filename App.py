# from __future__ import unicode_literals
import json
from dateutil import *
import dateutil.parser as dparser
import datetime
from datetime import *

# Передайте номер для чтения заметки по номеру
def readNote(number=date.today()):
    ifstream = open("notes.json", 'r')
    if isinstance(number, int):
        for i in range(number):
            # дата, заголовок, содержимое
            ifstream.readline()
            ifstream.readline()
            ifstream.readline()
        resline = ifstream.readline()
        print(resline)
    else:
        #реализовать фильтрацию по дате
        pass
    ifstream.close()

def writeNote():
    ofstream = open("./Progress task/notes.txt", 'a')
    jsonstream = open("./Progress task/notes.json", 'a', encoding='utf-8')
    line_title = "Заголовок: " + input("Введите заголовок заметки: ")
    while line_title == "" or line_title == " " or line_title == None:
        print("Ошибочный ввод!")
        line_title = "Заголовок: " + input("Введите заголовок заметки: ")
    
    line_msg = input("Введите тело заметки: ")
    while line_msg == "" or line_msg == " " or line_msg == None:
        print("Ошибочный ввод!")
        line_msg = input("Введите тело заметки: ")
    else:
        # date = datetime.date.today()
        date = datetime.now()
        date_string = date.strftime('%Y-%m-%d')
        dictionary = {
            "date": date_string,
            "title": line_title,
            "message": line_msg
        }
        json_object = json.dumps(dictionary,  indent=3, ensure_ascii=False) # separators=(';', ':')
        ofstream.write("\n" + date_string + '\n' + line_title + "\n" + line_msg + "\n")
        jsonstream.write("\n"+ json_object + "\n")
        print("Заметка успешно сохранена")
    jsonstream.close()
    ofstream.close()

def readNotes():
    ifstream = open("notes.json", 'r')
    for line in ifstream.readlines():
        print(line)


print("================================")
print("Заметочник запущен!")
print("================================")

while True:
    print("Команды:\n1. Написать заметку [add]\n2. Прочитать заметку по номеру/дате/все заметки [by_num/by_date/all]\n3. Редактировать заметку[red]\n4. Удалить заметку[del]")
    com = int(input("Введите номер команды: "))
    match com:
        case 1:
            writeNote()
        case 2:
            res = input("Все? [Y|N]")
            if res.lower() == "y": readNotes()
            else:
                res = input("По номеру? [Y|N]")
                if res.lower() == "y":
                    num = int(input("Номер записки: "))
                    readNote(num)
                else:
                    msgdate = input("Введите дату сообщения: ")
                    dt = dparser.parse(msgdate)
                    if dt is not None:
                        readNote(dt)
        case _:
            pass
        

