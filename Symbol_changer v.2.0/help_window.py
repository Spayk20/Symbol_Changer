from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class SWindow(QtWidgets.QWidget):
    def __init__(self,
                 parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowTitle('Help')
        self.setGeometry(500, 250, 630, 350)
        self.label = QListWidget(self)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 630, 350))
        self.label.setMinimumSize(QSize(600, 0))
        self.label.addItem("Данная программа создана для облегчения специфической работы с Excel файлами.\n"
                            "\n"
                            "Возможности:\n"
                            "- конкатенация (оъединение).xls файлов\n"
                            "- замена специальных символов(умлаутов)\n" 
                            "Удаление дубликатов происходит в автоматическом режиме.\n"
                            "\n"
                            "Программа принимает только .xls файлы и отдает .xlsx и .csv файлы.\n"
                            "\n"
                            "ВНИМАНИЕ!\n"
                            "Для правильной работы программы необходимо загружать файлы сразу после их получения из CRM:\n"
                            " - первая строка - информация\n"
                            " - вторая строка - названия столбцов (CONTACTID, First Name, Last Name, Account Name, Email, Secondary Email)\n"
                            " - 3 последние строки файла необходимо не удалять.\n"
                            "\n"
                            "Как пользоваться:\n"
                            "1. Загрузите файлы с помощью кнопки '+' или перетащите их в окно.\n"
                            "2. Выберите регион согласно которому хотите заменить символы.\n"
                            "3. Нажмите кнопку 'Получить результат'\n"
                            "4. В папке с программой будет создан файл RESULT.csv\n")

