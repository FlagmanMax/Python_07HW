import json
import md_controller
import csv

DB = "contacts_DB.json"
exportTxt = "export.txt"
exportCsv = "export.csv"

def create():
    data = []
    with open(DB, 'w') as file:
        json.dump(data,file)
        print("->\tБД создана и очищена")
    
def add():
    name = input("Введите Имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    
    data_BD = []
    # Get new ID
    with open(DB, 'r', encoding='UTF-8') as file:
        data_BD = json.load(file) 
        if len(data_BD) == 0:
            ID_new = 0
        else:
            ID_new = data_BD[-1]["ID"] + 1   
    
    data_new = {
        "ID": ID_new,
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    data_BD.append(data_new)
        
    with open(DB, "w", encoding='UTF-8') as file:
        json.dump(data_BD, file, indent=2, ensure_ascii=False)
    print('->\tНовый контакт успешно добавлен!')
    
def addFromFile(entry):    
    data_BD = []
    
    data_new = {
        "ID": entry[0],
        "Name": entry[1],
        "Surname": entry[2],
        "Phone number": entry[2],
        "Comment": entry[3],
    }
    data_BD.append(data_new)
        
    with open(DB, "w", encoding='UTF-8') as file:
        json.dump(data_BD, file, indent=2, ensure_ascii=False)
    print('->\tНовый контакт успешно добавлен!')
    
def view():
    try:
        with open(DB, 'r', encoding='UTF-8') as file:
            try:
                data_BD = json.load(file)
                print(f"id\t\tName\t\tSurname\t\tPhone\t\tComment")
                print("--------------------------------------------------------------------------------")
                dict = {}
                for i in range(0, len(data_BD)):
                    dict = data_BD[i]
                    print(*dict.values(), sep="\t\t")
            except ValueError:
                print("file {} readout error".format(DB))            
    except FileNotFoundError:
        print("file {} does not exist".format(DB))
    
def getId():
    try:
        id = int(input('->\tВведите id контакта: '))
        return id
    except ValueError:
        print('->\tОшибка ввода')
        return getId() 

def checkId():   
    
    id = getId()
    result = 0
    data_BD = []
    index = 0
    
    with open(DB, 'r', encoding='UTF-8') as file:
        data_BD = json.load(file)
        for i in range(0, len(data_BD)):
            if id == data_BD[i]['ID']:
                result = 1
                index = i
                break      
    
    return id, result, data_BD, index

def delete():
    
    id, result, data_BD, index = checkId()

    if result == 1:         
        with open(DB, 'w', encoding='UTF-8') as file:
            del data_BD[index]
            json.dump(data_BD, file, indent=2, ensure_ascii=False)
            print('->\tКонтакт удалён!')
    else:
        print(f'->\tКонтакт с id = {id} не найден!')
        
def edit():
    
    id, result, data_BD, index = checkId()
    
    if result == 1:  
        
        dict1 = data_BD[index]
        print(*dict1.values(), sep="\t\t")
        
        name = input("Введите Имя: ")
        surname = input('Введите Фамилию: ')
        phone = input('Введите номер телефона: ')
        comment = input('Введите коментарий: ')
    
        data_new = {
            "ID": dict1["ID"],
            "Name": name,
            "Surname": surname,
            "Phone number": phone,
            "Comment": comment,
        }
        
        data_BD[index] = data_new
        
        with open(DB, "w", encoding='UTF-8') as file:
            json.dump(data_BD, file, indent=2, ensure_ascii=False)
        print('->\tНовый контакт успешно обновлен!')
    else:
        print(f'->\tКонтакт с id = {id} не найден!')

def search():
    str = input("Введите Имя или Фамилию: ")
    result = []
    data_BD = []
    
    with open(DB, 'r', encoding='UTF-8') as file:
        data_BD = json.load(file)
        for i in range(0, len(data_BD)):
            if str == data_BD[i]['Name'] or str == data_BD[i]['Surname']:
                result.append(i)
    
    if len(result) > 0:
        dict = {}
        for i in range(0, len(result)):
            dict = data_BD[result[i]]
            print(*dict.values(), sep="\t\t")
    else:
        print('->\tКонтакт не найден')

def export_txt():
    with open(DB, 'r', encoding='UTF-8') as file:
        data_BD = json.load(file)
        if len(data_BD) > 0:
            with open(exportTxt, 'w',encoding='UTF-8') as export:
                for i in range(0, len(data_BD)):           
                    str1 = ";".join(map(str,list((data_BD[i].values())))) + "\n"           
                    export.write(str1)
            print(f"->\tЭкспорт данных в файл {exportTxt} успешно завершен")
        else:
            print("->\tОшибка экспорта в файл")
            
def import_txt():
    fileTxt = input("Введите название файла: ")
    with open(fileTxt, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        
    lst1 = list(map(lambda x: x.split(";"), map(lambda x: x.strip(), lines)))
    
    data_BD = []
    for i in range(0,len(lst1)):
        data_new = {
            "ID": int(lst1[i][0]),
            "Name": lst1[i][1],
            "Surname": lst1[i][2],
            "Phone number": lst1[i][3],
            "Comment": lst1[i][4],
        }
        data_BD.append(data_new)
    
    with open(DB, "w", encoding='UTF-8') as file:
        json.dump(data_BD, file, indent=2, ensure_ascii=False)

    print(f"->\tИмпорт данных из файла {fileTxt} успешно завершен")
            
def export_csv():
    with open(DB, 'r', encoding='UTF-8') as file:
        data_BD = json.load(file)
        if len(data_BD) > 0:
            with open(exportCsv, 'w',newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for i in range(0, len(data_BD)):           
                    lst1 = map(str,list((data_BD[i].values())))        
                    writer.writerow(lst1)
            print(f"->\tЭкспорт данных в файл {exportCsv} успешно завершен")
        else:
            print("->\tОшибка экспорта в файл")
            
def import_csv():
    fileTxt = input("Введите название файла: ")
    with open(fileTxt, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        
    lst1 = list(map(lambda x: x.split(","), map(lambda x: x.strip(), lines)))
    
    data_BD = []
    for i in range(0,len(lst1)):
        data_new = {
            "ID": int(lst1[i][0]),
            "Name": lst1[i][1],
            "Surname": lst1[i][2],
            "Phone number": lst1[i][3],
            "Comment": lst1[i][4],
        }
        data_BD.append(data_new)
    
    with open(DB, "w", encoding='UTF-8') as file:
        json.dump(data_BD, file, indent=2, ensure_ascii=False)

    print(f"->\tИмпорт данных из файла {fileTxt} успешно завершен")