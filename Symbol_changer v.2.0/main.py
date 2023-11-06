import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtSvg
from PySide6.QtCore import QFileInfo
import pandas as pd
from PySide6.QtWidgets import QMainWindow, QButtonGroup, QFileDialog, QMessageBox, QApplication

from ui_interface import Ui_MainWindow
from drag_n_drop import lnklist
from regions import de_to_ascii, WW, DACH
from help_window import SWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.open_btn.clicked.connect(self.openfile)
        self.ui.get_res_btn.clicked.connect(self.result)
        self.ui.pushButton.clicked.connect(self.clear)
        self.ui.concate_btn.clicked.connect(self.btnsummarise)
        self.ui.info_btn.clicked.connect(self.openWin)

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.ui.wwradio)
        self.buttonGroup.addButton(self.ui.dachradio)
        self.buttonGroup.buttonClicked.connect(self.check_button)
        self.selected_button = 'None'

    def check_button(self, radioButton):
        self.selected_button = radioButton.text()

    def openfile(self):
        files = []
        self.xls_file, _ = QFileDialog.getOpenFileNames(self, 'Выберите Файл', '.', 'Файлы Exсel (*.xls)')

        for elem in self.xls_file:
            files.append(QFileInfo(elem).fileName())
            lnklist.append(elem)
        self.ui.filelist.addItems(files)


    def result(self):

        if len(lnklist) < 1:
            self.errmsg = QMessageBox()
            self.errmsg.setIcon(QMessageBox.Critical)
            self.errmsg.setInformativeText('Выберите файлы для работы')
            self.errmsg.setWindowTitle("Ошибка")
            self.ui.resultlist.clear()
            self.errmsg.exec_()
        else:

            columns = ('First Name', 'Last Name', 'Account Name')
            if self.selected_button == 'None':
                self.errmessage()
            else:
                self.ui.resultlist.clear()
                self.summarise()
                book = pd.read_excel("Concatenated_file.xlsx")
                self.ui.resultlist.addItem("Началась замена символов")
                for j in columns:
                    self.changes = 0
                    ch = 0
                    for i in range(0, len(book.index)):

                        if self.selected_button == 'WW':
                            book[j].iloc[i], ch = de_to_ascii(book[j].iloc[i], WW)
                        if self.selected_button == 'DACH':
                            book[j].iloc[i], ch = de_to_ascii(book[j].iloc[i], DACH)


                    self.changes += ch
                    self.ui.resultlist.addItem(f">>> Заменено {self.changes} символов в столбце {j}")

                self.emails_parse(book)
                self.ui.resultlist.addItem(">>> Столбец Secondary email удален")
                book.to_csv("RESULT.csv", index=False)
                self.ui.resultlist.addItem("Файл RESULT.csv создан")

    def errmessage(self):
        self.errmsg = QMessageBox()
        self.ui.label_2.setStyleSheet(u"color: red;")
        self.errmsg.setIcon(QMessageBox.Critical)
        self.errmsg.setInformativeText('Выберите регион')
        self.errmsg.setWindowTitle("Ошибка")
        self.errmsg.exec_()
        self.ui.label_2.setStyleSheet(u"color: black;")

    def btnsummarise(self):
        if len(lnklist) < 1:
            self.errmsg = QMessageBox()
            self.errmsg.setIcon(QMessageBox.Critical)
            self.errmsg.setInformativeText('Выберите файлы для работы')
            self.errmsg.setWindowTitle("Ошибка")
            self.ui.resultlist.clear()
            self.errmsg.exec_()
        if len(lnklist) == 1:
            self.errmsg = QMessageBox()
            self.errmsg.setIcon(QMessageBox.Critical)
            self.errmsg.setInformativeText('Для объединения нужно минимум 2 файла')
            self.errmsg.setWindowTitle("Ошибка")
            self.ui.resultlist.clear()
            self.errmsg.exec_()
        else:
            self.ui.resultlist.clear()
            self.summarise()
            self.ui.resultlist.addItem("Готово")

    def summarise(self):
        df = pd.concat([pd.read_excel(f, skiprows=1, skipfooter=3) for f in lnklist], ignore_index=True)
        self.ui.resultlist.addItem("Объединение файлов в Concatenated_file.xlsx")
        df.dropna(subset=['CONTACTID'], inplace=True)
        df.drop_duplicates(subset=['CONTACTID'], keep='first', inplace=True)
        self.ui.resultlist.addItem("Очистка дубликатов")
        df.to_excel("Concatenated_file.xlsx", index=False)

    def emails_parse(self, book):
        for i in range(0, len(book.index)):
            if pd.isnull(book["Email"].iloc[i]):
                book["Email"].iloc[i] = book["Secondary Email"].iloc[i]
        del book["Secondary Email"]

    def clear(self):
        lnklist.clear()
        self.ui.filelist.clear()

    def openWin(self):
        self.secondWin = SWindow(self)
        self.secondWin.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
