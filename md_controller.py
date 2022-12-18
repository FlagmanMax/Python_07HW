import md_ui
import md_db

def inputProcessing():
    try:
        inputInt = int(input('\n->\tВведите пункт меню: '))
        return inputInt
    except ValueError:
        print('->\tОшибка ввода\n')
        return inputProcessing()
    
def choiceProcessing():
    while(True):
        choice = md_ui.menu()
        
        if choice < 1 or choice > 11:
            print('->\tОшибка ввода\n')
        elif choice == 1:   #1 - Создать новую книгу или очистить существующую
            md_db.create()
        elif choice == 2:   #2 - Добавить новый контакт
            md_db.add() 
        elif choice == 3:   #3 - Удалить контакт
            md_db.delete()
        elif choice == 4:   #4 - Редактировать контакт
            md_db.edit()
        elif choice == 5:   #5 - Найти контакт
            md_db.search()
        elif choice == 6:   #6 - Показать все контакты
            md_db.view()
        elif choice == 7:   #7 - Экспорт в txt-файл
            md_db.export_txt()  
        elif choice == 8:   #8 - Экспорт в csv-файл
            md_db.export_csv() 
        elif choice == 9:   #9 - Импорт из в txt-файла
            md_db.import_txt()  
        elif choice == 10:  #10 - Импорт из в csv-файла
            md_db.import_csv()
        elif choice == 11:
            print('->\tДо новых встреч!\n')
            exit()           