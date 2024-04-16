# from __future__ import unicode_literals
import json
from dateutil import *
import dateutil.parser as dparser
import datetime
from datetime import *
import os


# Передать номер для чтения заметки по номеру
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

# Написать заметку, пока в двух видах
def writeNote():
    # ofstream = open("./notes.txt", 'a')
    jsonstream = open("./notes.json", 'r+', encoding = 'Windows_1251')
    
    line_title = input("Введите заголовок заметки: ")
    while line_title == "" or line_title == " " or line_title == None:
        print("Ошибочный ввод!")    
        line_title = input("Введите заголовок заметки: ")
    
    line_msg = input("Введите тело заметки: ")
    while line_msg == "" or line_msg == " " or line_msg == None:
        print("Ошибочный ввод!")
        line_msg = input("Введите тело заметки: ")
    else:
        date = datetime.now()
        date_string = date.strftime('%Y-%m-%d')
        dictionary = {
            "date": date_string,
            "title": line_title,
            "message": line_msg
        }
        
        # 
        # json_object = json.dumps(dictionary, indent=4, ensure_ascii=False) # separators=(';', ':') 

        # ofstream.write("\n" + date_string + '\n' + line_title + "\n" + line_msg + "\n")
        
        file_data = json.load(jsonstream)
        file_data["notes"].append(dictionary) # без дампа работает отлично!
        jsonstream.seek(0)
        # json_object = json.dumps(file_data, indent= 4, ensure_ascii=False)
        json.dump(file_data, jsonstream, indent = 4)
        # jsonstream.write(json_object)
        print("Заметка успешно сохранена")
    jsonstream.close()
    # ofstream.close()

def readNotes():
    jsonstream = open("notes.json", 'r')
    file_data = json.load(jsonstream)
    
    value = file_data["notes"]
    for el in value:
        for v in el.values():
            print(v)
        print("\n")
    
def changeNote(note_num):
    jsonstream = open("notes.json", 'r+', encoding = 'Windows_1251')
    file_data = json.load(jsonstream)
    value = file_data["notes"]
    mas = None
    res = None
    cnt = 0
    for el in value:
        mas = el.values()
        for value in mas:
            cnt+=1
        if (cnt == note_num*3):
            res = mas
            break
    
    if res is not None:
        valuesList = list(res)    
        print(valuesList)
        red_title = input("Новый заголовок: ")
        red_msg = input("Новое сообщение: ")
    else:
        print("Error")
                
    

print("================================")
print("Заметочник запущен!")
print("================================")

while True:
    print("Команды:\n1. Написать заметку [add]\n2. Прочитать заметку по номеру/дате/все заметки [by_num/by_date/all]\n3. Редактировать заметку[red]\n4. Удалить заметку[del]")
    com = input("Введите номер команды: ")
    match com:
        case 'add':
            writeNote()
        case 'all':
            res = input("Все? [Y|N]")
            if res.lower() == "y": 
                readNotes()
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
        case 'red':
            number = int(input("Введите номер записки: "))
            changeNote(number)
        case _:
            pass
        

