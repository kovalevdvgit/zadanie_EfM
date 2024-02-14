import os


class core_phone_book:
    def __init__(self):
        self.view_lines = 4#настройка количества строк справочника, можно ввести None для вывода всех строк на одной странице
        self.create_file()
        self.view_all()




    def view_all(self, line = 2):
        with open(self.file_name, 'r') as file:
            text_lines = file.readlines()
        self.view(text_lines[:1][0], list(enumerate(text_lines[1:])))


    def view(self, header, body):

        #body = list(enumerate(body))

        index = 0
        view_lines = self.view_lines

        while True:
            os.system('CLS')
            if view_lines and len(body) >= view_lines :
                info = body[(view_lines * index):view_lines + (view_lines * index)]
                menu =  '''
                        ______________________________________________________________
                        |Следующая страница -> e, предыдущая -> q                    |
                        |Для добавления введите -> a(en)                             |
                        |Для поиска введите -> f(en)                                 |
                        |Для редактирования записи введите номер строки -> 1 (пример)|
                        |Для выхода введите -> ex                                    |
                        |Для перехода к началу нажмите кнопку "Enter"                |
                        |____________________________________________________________|
                        '''
            else:
                info = body
                menu =  '''
                        ______________________________________________________________
                        |Для добавления введите -> a(en)                             |
                        |Для поиска введите -> f(en)                                 |
                        |Для редактирования записи введите номер строки -> 1 (пример)|
                        |Для выхода введите -> ex                                    |
                        |Для перехода к началу нажмите кнопку "Enter"                |
                        |____________________________________________________________|
                        '''


            print('\n', self.obrabotka_vuvoda(header, True),'\n')
            print('==='*60,'\n')
            try:
                for n, i in info:
                    print(n+1,(self.obrabotka_vuvoda(i)))
            except:
                pass

            print(menu)
            but = input('\t\t\t Ввод ->  ')
            if but == 'e' and view_lines:
                index += 1
                if len(body[(view_lines * index):view_lines + (view_lines * index)]) == 0:
                    index -= 1
            elif but == 'q' and view_lines:
                index -= 1
                if index < 0:
                    index += 1
            elif but =='a':
                self.add()
                break
            elif but =='f':
                self.find()
                break
            elif but =='ex':
                break
            elif but == '':
                self.view_all()
                break
            else:
                try:
                    self.select(int(but))
                    break
                except Exception as e:
                    pass

    def add(self):
        os.system('CLS')
        print('''
                 Введите фамилию, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый), разделяя позиции пробелами!
                 Если в названии организации есть пробел замените его на _.
                 ''')
        new_line = input('\t\t\t Ввод ->  ').split()
        print('''
                 Для подтверждения изменений введите y(en)
                 ''')
        selecter = input('\t\t\t Ввод ->  ')
        if selecter == 'y':
            new_line = new_line[:6] if len(new_line) > 6 else new_line
            with open(self.file_name, 'a') as file:
                if len(new_line) != 0:
                    file.write(f'{" ".join(new_line)}\n')
        self.view_all()

    def find(self):
        os.system('CLS')
        print('''
                    Введите параметр/ры для поиска(имя, фамилия, итд.)
                ''')
        template  = input('\t\t\t Ввод ->  ')
        try:
            template = template.split(' ')
        except:
            template = [template]

        with open(self.file_name, 'r') as file:
            text_lines = list(enumerate(file.readlines()))

        header = text_lines[:1]
        boody = text_lines[1:]
        try:
            buffer_line = []
            for n, line in boody:
                find_successfully = []
                for t in template:
                    if any([True for word in line.split(' ') if t in word]):
                        find_successfully.append(True)
                    else:
                        find_successfully.append(False)
                if all(find_successfully):
                    buffer_line.append((n-1, line))
        except:
            pass

        self.view(header[0][1], buffer_line)

    def select(self, number:int):

        with open(self.file_name, 'r') as file:
            text_lines = list(enumerate(file.readlines()))
        os.system('CLS')
        print(f'\n{self.obrabotka_vuvoda(text_lines[0][1], True)}')
        print('===' * 60, '\n')
        for n, i in text_lines:
            if n == number:
                print(f'{n}{self.obrabotka_vuvoda(i)}')
                print('''
                         Введите новые значения
                        ''')
                new_line = input('\t\t\t Ввод ->  ')
                print('''
                         Для подтверждения изменений введите y(en)
                        ''')

                selecter = input('\t\t\t Ввод ->  ')
                if selecter == 'y':

                    new_line = new_line.split(' ')
                    new_line= new_line[:6] if len(new_line) > 6 else new_line
                    text_lines[n] = (n, f'{" ".join(new_line)}\n')

                    with open(self.file_name, 'w') as file:
                        for n, i in text_lines:
                            if i != '\n':
                                file.write(i)
        self.view_all()

    def create_file(self, file_name:str='phone_numbers.txt') -> None:
        self.file_name = file_name
        if file_name in os.listdir():
            pass
        else:
            with open(file_name, 'w') as file:
                file.write(f'Фамилия Имя Отчество Название_организации Телефон_рабочий Телефон_личный(сотовый)\n')

    def obrabotka_vuvoda(self, line:str, dop_space:bool=False, otst:int=25):

        if dop_space:
            itog = otst * ' '
        else:
            itog = (otst - 1) * ' '

        for i in line.split(' '):
            if len(i) < otst:
                itog += (i + (otst - len(i)) * ' ')
            else:
                itog += f'{i:0.19} '
        return itog


core_phone_book()
