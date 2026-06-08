import os
import math
import platform as plt

        ### Инициализация функций, словарей и списков ###
def getOS():
    os_name = plt.system()
    if (os_name == "Windows"): return("win")
    elif (os_name == "Darwin"): return("mac")
    else: return("lin")

settings = {
    "beta_Math": False,
    "beta_find": False,
    "beta_suppFormat": False # тест
    }
suppMath = {
    "easy": ['+', '-', '*', '/', "**", "//"],
    "norm": ["MAX", "MIN", "NOD", "NOK"],
    "hard": ["IF"],
    "beta": ["COND"]
}

sp = "\\" if (getOS() == "win") else '/'

suppType = ["csv"]
table = []
len_max = []
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
path = list(
            map(str, (os.path.dirname(os.path.abspath(__file__))
                     ).split(sp)
               )
           )
dataInPath = []

def showPath(): return(sp.join(path))
def bye():
    print(f"\t\t" + r" |\  _    _  ___   | ")
    print(f"\t\t" + r" |/   \  /  /   \  | ")
    print(f"\t\t" + r" | \   \/   |___/  | ")
    print(f"\t\t" + r" |_/  _/    \___   . ")
    print(f"\n"); exit()
def toggle(nme): settings[nme] = False if (settings[nme] == True) else True
def printOnOff(nme): print(f"\t ВЫКЛ." if (settings[nme] == False) else print(f"\t ВКЛ."))

################################################

    ## v.6
    ## -----                    ( ! будет ! )
# + ## добавлено графическ. прощание и приветствие(лого tablX) 
# + ## таблица стала красивее
    ## добавлена поддерка иностранного csv
# + ## добавлены настройки и некоторые бета-функции
    ## добавлена обработка ошибок в осташихся местах
    ## исправлено множество ошибок в коде
# + ## улучшена читаемость кода

              ###########################
                ##    НАЧАЛО КОДА    ##
print(f"\n")
print(f"\t" + r"                               \    /             ")
print(f"\t" + r"                                \  /         ___  ")
print(f"\t" + r"  |        /\      |\    |       \/         /   \ ")
print(f"\t" + r" _|_      /  \     |/    |       /\        | ___  ")
print(f"\t" + r"  |      /____\    | \   |      /  \       |/   \ ")
print(f"\t" + r"  \__   /      \   |_/   |__   /    \       \___/ ")
print(f"\n")

def start():
      ## пишем информацию о том, что можно делать
    if (settings["beta_find"] == True):
        print("Введите '!go' для поиска файла")

    print("Введите '!settings' для открытия настроек.")

    print("Введите '!exit' для выхода")

    if (settings["beta_find"] == True):
        print(f"Введите имя файла c расширением", end=" ") 
        print("(если он находится в этой же директории): ")
        nameFile = input().strip()
    else:
        print(f"Введите имя файла c расширением: ", end="")
        nameFile = input().strip()
    
    return(nameFile)
nameFile = start()

  ## ищем папку(если пользователь хочет)
if (nameFile == "!go" and
    settings["beta_find"] == True):
    print(f"\nимя_папки - выбрать следующую директорию")
    print("'..' - предыдущая директория")
    print("'..done")
    print(f"'..ls' - показать папки и файлы в этой директории\n")

    def find_tabl():
        print(f"Текущая директория - {showPath()}")
        dataInPath = os.listdir(showPath())
        txt = input()

        if (txt == ".."):
            path.pop(-1)

        elif (txt == "..ls"):
            print("В данной директории находится:")
            for loop_part in dataInPath:
                if (len(loop_part) != 0): print(f"\t{loop_part}")
                else: print("Директория пуста!")
            
        
        elif (txt == "..done"):
            return(path)
        
        else:
            if (txt in dataInPath):
                path.append(txt)
            else:
                print("Такой папки не найдено :)")
        
        find_tabl()  # повторяем функцию для получения полного пути
    path = find_tabl()
    nameFile = input(f"Введите имя файла c расширением: ").strip()
    nameFile = showPath() + '/' + nameFile

  ## или открываем настройки(также по запросу)
elif (nameFile == "!settings"): 
    def setting(settings):
        print(f"\nНастройки. Для переключения настройки напишите её номер.")
        print(f"\nДля выхода из настроек напишите 'exit', а для выхода из tablX - !exit")

        while (True):
            print(f"\t1. Бета-функции Math.")
            printOnOff("beta_Math")

            print(f"\t2. Бета-поиск таблицы на этом компьютере")
            printOnOff("beta_find")

            # print(f"\t3. Бета-поддержка не-CSV форматов таблиц")
            # printOnOff("beta_suppFormat")

            change = input().strip()
            
            if (change == '1'): toggle("beta_Math")
            elif (change == '2'): toggle("beta_find")
            elif (change == '3'): toggle("beta_suppFormat")
            elif (change == "exit"): break
            elif (change == "!exit"): bye()
            else: setting()
        
        return(settings)
    settings = setting(settings)

if (nameFile == "!exit"): bye()

  ## разделяем название файла на имя + расширение
try: bodyFile, typeFile = map(str, nameFile.split("."))
except:
    print(f"\nВы ввели неверные данные!")
    print(f"Убедитесь, что вы правильно ввели имя!\n")
    exit()

  ## если тип файла не поддерживается, выводим ошибку
typeFile = typeFile.lower()
if (typeFile not in suppType):
    print(f"\nИзвините, такой формат файла не поддерживается!")
    print("Попробуйте скачать новую версию утилиты", end="")
    print("или конветировать таблицу в один из форматов:")
    for sType in suppType:
        print("   ", sType)
    print(f"\n")
    exit()



if (typeFile == "csv"):
      ### Чтение и запись таблицы CSV в список для отображения
    
    try:  # считаем строки суммарно
        with open(nameFile, "r") as set:
            len_lns = len(set.readlines())
        set.close()

        with open(nameFile, "r") as atext:
            warn = False
            sepMin = 0
            text = atext.readline()
              ## если csv не по-российским стандартам выводим соотв. сообщ.
              ## а также пытаемся расшифровать таблицу
            if (';' not in text) and (',' in text):
                print("Данная таблица была сделана", end=" ")
                print("не российским редактором таблиц!")
                print("Есть ли в ячейках вашей таблицы запятые?(yes/no(...))")

                if (input() == "yes"):
                    if (settings["beta_suppFormat"] == True):
                        print("Пытаемся открыть таблицу!(бета-функция)")
                        sepMin = text.count(';')
                        for i in range(len_lns - 1):
                            text = atext.readline()
                            sepMin = min(sepMin, text.count(';'))
                        len_hds = sepMin + 1
                        warn = True
                        sep = ','
                    
                    elif (settings["beta_suppFormat"] == False):
                        print("Приносим свои извинения, скорее", end= " ")
                        print("всего таблицу не получится открыть!")
                        print("Но в настройках есть бета-функция для такого случая!")
                else:
                    sep = ','
            
            elif (';' not in text and ',' not in text):
                None  # сделать(ошибка)
            
            else:
                sep = ';'
        atext.close()

        with open(nameFile, "r") as file:
            text = file.readline()
              
              ## если csv нормальный
            if (warn == False): 
                table = list(map(str, text.split(sep)))
                len_hds = len(text.split(sep))  # добавляем 1-ую строку

                ## добавляем остальные строки
                for unUse in range(len_lns):
                    text = file.readline()
                    table += text.split(sep)
            
            #elif (warn == True):
            #1    if ()
            #    table += 
        file.close()
    
    except(FileNotFoundError):  # если файл не открывается
        print(f"Файла {nameFile} не существует! :/ ")
        print("Убедитесь, что файл с таблицей находится в", end=" ")
        print(f"одной и той же директории с tablX!\n")
        exit()

      ## удаление "\n" в ячейках таблицы
    cnt4 = 0
    for cell in range(1, len(table)):
        cnt4 += 1
        if (cnt4 % len_hds):  # если ячейка последняя - убираем '\n'
            table[cell] = table[cell].removesuffix("\n")

      ## преобразуем числовые значения списка в int/float
    for loop_part in range(len(table) - 1):
        try:  # преобразуем в int
            table.insert(loop_part, int(table[loop_part]))
            table.pop(loop_part + 1)

        except ValueError:
            try:  # преобразуем в float
                table.insert(loop_part, float(table[loop_part]))
                table.pop(loop_part + 1)

            except ValueError:  # оставляем как string
                None

      ### Конец ### 

if (typeFile == "another"):
    code = None


  ### Вывод таблицы в консоль
def print_tabl ():
    cnt = 1
    cnt2 = 0
    cnt3 = 1
    cnt5 = 0
    cnt6 = 0
    cnt7 = 0
    cnt8 = 0
    tabl_line = ""
    var3 = 0
    
      ## дополняем алфавит
    if (52 >= len_hds > 26):
        for loop_let in alph:
            alph.append('A' + loop_let)
    elif (len_hds > 52):
        print("Приносим свои извинения! Ваша таблица", end=" ")
        print("слишком большая по ширине! Она не может быть выведена")
        exit()

      ## определяем максимальное кол-во символов в 
      ## каждом столбце
    for loop_value in table:
        if (cnt3 != 1):
            len_max[cnt2] = max(len_max[cnt2], len(str(loop_value)))
        if (cnt3 == 1):
            len_max.append(len(str(loop_value)))

        if (len_hds - cnt2 == 1):
            cnt2 = -1
            cnt3 += 1
        cnt2 += 1
    
      ## считаем длину линии таблицы
    for loop_len_column in len_max:
        for unUse in range(len(str(loop_len_column))):
            tabl_line += "-"  # добавляем длину из-за кол-ва цифр в каждом столбце
        tabl_line += "--"  # пробелы между '|' и значениями
    
    for unUse in range(len(str(len_lns))):  # добавляем длину из-за
        tabl_line += "-"                    # длины № строки
    
    tabl_line += "-------------" # добавляем длину линии для красоты +
                                 # длина отступа(между № строк и 1-ой ячейкой)


      ## выводим таблицу
    print(tabl_line)
    
    print("        ", end="")
    for loop_let in alph[:len_hds]:
        cnt7 += 1
        var3 = 0
        if (cnt7 == 1):
            while (len(loop_let) < len_max[0]):
                var3 += 1
                if (var3 % 2 == 0):
                    loop_let += " "
                else:
                    loop_let = " " + loop_let
            print(loop_let, end=" ")
        
        elif (cnt7 != len_hds):
            while (len(loop_let) < len_max[cnt7 - 1]):
                var3 += 1
                if (var3 % 2 == 0):
                    loop_let = " " + loop_let
                else:
                    loop_let += " "
            print("|", loop_let, end=" ")
        
        elif (cnt7 == len_hds):
            while (len(loop_let) < len_max[len_hds - 1]):
                var3 += 1
                if (var3 % 2 == 0):
                    loop_let = " " + loop_let
                else:
                    loop_let += " "
            print("|", loop_let)

    print(f"{tabl_line}")

    for loop_v in table:
        loop_v = str(loop_v)
        if (cnt == 1):
            cnt5 += 1
            
            if (cnt5 >= len_lns + 1):
                break

            elif (cnt5 < 10):
                print(cnt5, end=")      ")
            elif (cnt5 < 100):
                print(cnt5, end=")     ")
            elif (cnt5 < 1000):
                print(cnt5, end=")    ")
            else:
                print(cnt5, end=")   ")
            
            var = 0
            while (len(loop_v) < len_max[0]):
                if (var % 2 == 0):
                    loop_v += " "
                else:
                    loop_v = " " + loop_v
            if (cnt == len_hds):
                print(loop_v)
            else:
                print(loop_v, end=" ")
            
        elif (cnt != len_hds):
            var = 0
            while (len(loop_v) < len_max[1]):
                var += 1
                if (var % 2 == 0):
                    loop_v = " " + loop_v
                else:
                    loop_v += " "
            print("|", loop_v, end=" ")

        elif (cnt == len_hds):
            var = 0
            while (len(loop_v) < len_max[2]):
                if (var % 2 == 0):
                    loop_v = " " + loop_v
                else:
                    loop_v += " "     
            print("|", loop_v)

        if (cnt == len_hds):
            cnt = 1
        else:
            cnt += 1

    print(tabl_line)
print_tabl()
  ### Конец ###


  ## конвертер из позиции ячейки таблицы в её значение
def lett_2_int(datas):
    num = 0
    letter = ""
    for loop_dat in datas:
        if (loop_dat.isdigit() == True):
            num += int(loop_dat)
        elif (loop_dat.isalpha()):
            letter += loop_dat
        else:
            res = 404

    if (res == 404):
        return("err_format")
    elif (num > len_lns):
        return("err_line")
    
    else:
        indx = num * len_hds
        if (letter in alph):
            for loop_let in alph:
                indx += 1
                if (loop_let == letter):
                    break
    return(indx)



  ## меню действий с таблицей
def menu():
    var = []
    args = ""
    print(f"\nДействия с таблицей:")
    print(f"\t edit - изменить")
    print(f"\t math - арифметические действия")
    print(f"\t exit - закрыть программу")
    
      # изменение таблицы
    do = input().strip().lower()
    if (do == "edit"):
        print(f"\nЗдесь вы можете изменять таблицу...")

      # математические операции с таблицей
    elif (do == "math"):
        print(f"\nВведите математическое выражение.", end=" ")
        print("Пример -> B2 * C3. Поддерживаются:")

          ## выводим список подерживаемых операций
        for word in suppMath["easy"]:
            print(f"\t{word}")
            if (suppMath["easy"][-1] == word):
                print(f"\n")  # отделяем строкой следующий тип Math

        for word in suppMath["norm"]:
            print(f"\t{word}")
            if (suppMath["norm"][-1] == word):
                print(f"\n")

        for word in suppMath["hard"]:
            print(f"\t{word}")
            if (suppMath["hard"][-1] == word and
                settings["beta_Math"] == True):
                print(f"\n")

        if (settings["beta_Math"] == True):
            for word in suppMath["beta"]:
                print(f"\t{word}")

          ## используем функции отбражения ошибок для сокращения и упрощения кода
        def err_math_format():
            print("Некорректные данные! Форматы:")
            print(" знач1 действие знач2")
            print(" действие знач1 знач2")
            print(" if знач1 действие знач2 = число/слово ; делать...")
            menu()
        def err_math_value():
            print("Данный тип значений не поддерживается!", end=" ")
            print(f"Попробуйте в значение ввести ссылку на ячейку таблицы!\n")
        def err_math_line():
            print("Вы неверно указали значения!", end=" ")
            print(f"В таблице всего {len_lns} строк!")

          ## получаем входное выражение
        maths = input().upper().strip()
        if (maths == ""):
            err_math_format()

          ## пытаемся разделить входные данные на части
        try:  ## easy
            v1, oper, v2 = map(str, maths.split())
            print(v1, oper)
            v1 = lett_2_int(v1)
            v2 = lett_2_int(v2)
            print(v1, oper)
            
            if (v1 == "err_format") or (v2 == "err_format"):
                TypeError
            elif (v1 == "err_line") or (v2 == "err_line"):
                TypeError
        except:
            try:  ## normal
                oper, v1, v2 = map(str, maths.split())
                v1 = lett_2_int(v1)
                v2 = lett_2_int(v2)

                if (v1 == "err_format") or (v2 == "err_format"):
                    TypeError
                elif (v1 == "err_line") or (v2 == "err_line"):
                    TypeError
            except:
                try:  ## hard
                    action = maths.split(';')[1] 
                    condits = list(map(str, maths.split()))
                    if (len(condits) < 4):
                        err_math_format()
                    oper = condits.pop(0)
                    v1 = condits.pop(0)
                    v2 = condits.pop(-1)
                    for word in condits:
                        if (lett_2_int(word) == "err_format" or
                            lett_2_int(word) == "err_line"):
                            break
                        else:
                            args += word
                    
                    v1 = lett_2_int(v1)
                    v2 = lett_2_int(v2)

                    if (v1 == "err_format") or (v2 == "err_format"):
                        TypeError
                    elif (v1 == "err_line") or (v2 == "err_line"):
                        TypeError
                except:
                    try:  ## beta
                        do = " надо сделать тут разделение beta "
                        if (v1 == "err_format") or (v2 == "err_format"):
                            TypeError
                        elif (v1 == "err_line") or (v2 == "err_line"):
                            TypeError
                    except:
                        if (v1 == "err_format") or (v2 == "err_format"): 
                            err_math_value()
                        elif (v1 == "err_line") or (v2 == "err_line"):
                            err_math_line()
        
        
          ## обрабатываем ошибки при неправильном формате ввода
        if (oper not in suppMath): err_math_format()
        
          ## производим простую математику
        elif (oper in suppMath["easy"]):
            if (oper == '+'):
                res = v1 + v2
            elif (oper == '-'):
                res = v1 - v2
            elif (oper == '*'):
                res = v1 * v2
            elif (oper == '/'):
                res = v1 / v2
            elif (oper == "**"):
                res = v1 ** v2
            elif (oper == "//"):
                res = v1 // v2

          ## производим среднюю математику
        elif (oper in suppMath["norm"]):
            if (oper == "MAX"):
                res = max(v1, v2)
            elif (oper == "MIN"):
                res = min(v1, v2)
            elif (oper == "NOD"):
                res = math.gcd(v1, v2)
            elif (oper == "NOK"):
                res = math.lcm(v1, v2)

          ## производим трудную математику
        elif (oper in suppMath["hard"]):
            if (oper == "IF"):
                if (args == "+"):
                    res = v1 + v2
                elif (args == "-"):
                    res = v1 - v2
                elif (args == "*"):
                    res = v1 * v2
                elif (args == "/"):
                    res = v1 / v2
                elif (args == "**"):
                    res = v1 ** v2
                elif (args == "//"):
                    res = v1 // v2
                
                #if (res == )

          ## производим бета-математику
        elif (oper in suppMath["beta"]):
            if (settings["beta_Math"] == True):
                do
        
        print(f"{res}\n")
        menu()
                
      ## выход
    elif (do == "exit"):
        bye()
    else:
        menu()

menu()