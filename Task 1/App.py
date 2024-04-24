import json
import dateutil.parser as dparser
import secrets
from datetime import *
# from dateutil import *

# Передать номер для чтения заметки по номеру
def readNote(argc):
    jsonstream = open("notes.json", 'r')
    file_data = json.load(jsonstream)
    value = file_data["notes"]
    cnt = 0
    if isinstance(argc, int):
        for el in value:
            mas = el.values()
            for value in mas:
                cnt+=1
            if (cnt == argc*4):
                valuesList = list(mas)    
                for field in valuesList:
                    print(field)
                print("================================")
                break
    elif isinstance(argc, date):
        rel_list = list()
        for el in value:
            mas = el.values()
            for value in mas:
                if cnt%4==1:
                    if dparser.parse(value).date() == argc:
                        rel_list.append(mas)
                cnt += 1
        
        if len(rel_list) == 0:
            print("Не найдено сообщений за эту дату")
        else:
            for i in range(0, len(rel_list)):
                print("\n")
                line = list(rel_list[i])
                for value in line:
                    print(value)
                print("================================")
    else:
        pass
    jsonstream.close()

# Написать заметку, пока в двух видах
def writeNote():
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
            "id" : secrets.token_hex(nbytes=16),
            "date": date_string,
            "title": line_title,
            "message": line_msg
        } 
        file_data = json.load(jsonstream)
        file_data["notes"].append(dictionary) # без дампа работает отлично!
        jsonstream.seek(0)
        json.dump(file_data, jsonstream, indent = 4)
        print("Заметка успешно сохранена")
        
    jsonstream.close()


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
    cnt = 0
    if (note_num == 0):
        print("Неверный номер, индексация идёт с единицы!")
        return
    # el = elements
    for el in value: 
        # mas - список значений
        mas = el.values()
        for value in mas:
            cnt+=1
        if (cnt == note_num*4):
            valuesList = list(mas)    
            print(valuesList)
            red_title = input("Новый заголовок: ")
            red_msg = input("Новое сообщение: ")
            dictionary = {
                "id" : valuesList[0],
                "date": valuesList[1],
                "title": red_title,
                "message": red_msg
            }
            mas = dictionary
            break
        
    file_data["notes"][note_num-1] = mas
    jsonstream.seek(0)
    jsonstream.truncate()
    json.dump(file_data, jsonstream, indent = 4)          


def deleteNote(note_num):
    jsonstream = open("notes.json", 'r+', encoding = 'Windows_1251')
    old_file_data = json.load(jsonstream)
    new_file_data = old_file_data
    
    if note_num <= 0 or note_num > len(old_file_data["notes"]):
        print("Нет такого индекса!")
        return
    if note_num != 1:
        for i in range(0, note_num-1):
            new_file_data["notes"][i] = old_file_data["notes"][i]
    else:
        new_file_data["notes"] = new_file_data["notes"][1:]    
        jsonstream.seek(0)
        jsonstream.truncate()
        json.dump(new_file_data, jsonstream, indent = 4)
        print("Удалено!")
        return
    if note_num != len(old_file_data):
        for i in range(note_num, len(old_file_data["notes"])):
            new_file_data["notes"][i-1] = old_file_data["notes"][i]
            
    new_file_data["notes"] = new_file_data["notes"][:-1]    
    jsonstream.seek(0)
    jsonstream.truncate()
    json.dump(new_file_data, jsonstream, indent = 4)
    print("Удалено!")


# Основная программа начинается здесь
print("================================")
print("Заметочник запущен!")
print("================================")

while True:
    print("Команды:\n1. Написать заметку [add]\n2. Прочитать заметку по номеру/дате/все заметки [by_num/by_date/all]\n3. Редактировать заметку[red]\n4. Удалить заметку[del]")
    com = input("Введите команду: ")
    match com:
        case 'add':
            writeNote()
        case 'all':
            readNotes()
        case 'by_num':
            num = int(input("Номер записки: "))
            readNote(num)
        case 'by_date':
            msgdate = input("Введите дату сообщения: ")
            dt = dparser.parse(msgdate)
            if dt is not None:
                search_date = dt.date()
                readNote(search_date)
        case 'red':
            number = int(input("Введите номер записки: "))
            changeNote(number)
        case 'del':
            number = int(input("Введите номер записки: "))
            deleteNote(number)
        case _:
            print("Неверный ввод!")
        

