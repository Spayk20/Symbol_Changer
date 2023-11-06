import os
import sys
import pandas as pd

from PyQt5 import uic
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog

from rules import umlauts_changing, emails_selection

pd.options.mode.chained_assignment = None


class Window(QWidget):
    def __init__(self, app):
        QWidget.__init__(self)
        self.set()
        self.file = ''
        self.dir = './FILES'
        self.ui.lst_info.addItem('>>> Откройте файл')
        self.ui.btn_open.clicked.connect(self.open)
        self.ui.btn_work.clicked.connect(self.file_processing)

        self.ui.rb_ww.toggled.connect(self.onClicked)
        self.ui.rb_dach.toggled.connect(self.onClicked)
        self.ui.rb_ww.setChecked(True)

    def set(self):
        self.ui = uic.loadUi('symbols_design.ui')
        self.ui.show()

    def message(self, settext):
        self.errmsg = QMessageBox()
        self.errmsg.setText(settext)
        self.errmsg.setIcon(QMessageBox.Critical)
        self.errmsg.setWindowTitle('Ошибка')
        self.errmsg.exec_()

    def saving(self, df, fname, sname):
        dir = os.path.dirname(os.path.abspath(__file__))
        OUT_FOLDER = 'FILES'
        file_path = os.path.join(dir, OUT_FOLDER, f'{fname}-{sname}')
        df.to_excel(file_path, f'{fname}-{sname}', index=False)

    def open(self):
        self.file, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '.', 'Файлы Excel (*.xls, *.xlsx)')
        if self.file:
            self.ui.lst_info.clear()
            self.ui.lst_info.addItem(f'>>> Открыт файл: {QFileInfo(self.file).fileName()}')
            self.book = pd.read_excel(self.file)

    def file_checking(self):
        if {'First Name', 'Last Name', 'Account Name (Account Name)', 'Email', 'Wrong email', 'Email source',
                'Secondary Email', 'Wrong secondary Email', 'Secondary Email source'}.issubset(self.book.columns) is False:
            result = 'Отсутствуют обязательные колонки'
        elif self.book['First Name'].isnull().sum() > 0:
            result = 'Пустые ячейки в столбце First Name'
        elif self.book['Last Name'].isnull().sum() > 0:
            result = 'Пустые ячейки в столбце Last Name'
        elif self.book['Account Name (Account Name)'].isnull().sum() > 0:
            result = 'Пустые ячейки в столбце Account Name'
        return result

    def file_processing(self):
        try:
            try:
                file_errors = self.file_checking()
                self.message(f'{file_errors}')
            except:
                self.book, changes_in_columns = umlauts_changing(self.book, self.radioButton.text())
                self.ui.lst_info.addItem(f'>>> Выполняю преобразование по правилам региона: {self.radioButton.text()}')
                self.ui.lst_info.addItem(f'>>> Заменено {changes_in_columns["First Name"]} символов в столбце First Name')
                self.ui.lst_info.addItem(f'>>> Заменено {changes_in_columns["Last Name"]} символов в столбце Last Name')
                self.ui.lst_info.addItem(f'>>> Заменено {changes_in_columns["Account Name (Account Name)"]} символов в столбце Account Name')

                try:
                    self.book = emails_selection(self.book)
                    self.ui.lst_info.addItem(f'>>> Почты перемещены')
                except:
                    self.message('Что-то не так с почтами')

                self.book.drop_duplicates(keep='first', ignore_index=False, inplace=True)
                self.ui.lst_info.addItem(f'>>> Дубликаты удалены')
                self.saving(self.book, 'RESULT', QFileInfo(self.file).fileName())
                self.ui.lst_info.addItem(f'>>> Сохранено в RESULT-{QFileInfo(self.file).fileName()}')
                self.suspecting(self.book)
        except:
            self.message('Файл не выбран')

    # def duplicate(self):
    #     if self.file:
    #         df = pd.read_excel(self.file)
    #         df.drop_duplicates(keep='first', ignore_index=False, inplace=True)
    #         self.ui.lst_info.addItem(f'>>> Дубликаты удалены')
    #         self.saving(df, 'WITHOUT_DUPLICATES', QFileInfo(self.file).fileName())
    #         self.ui.lst_info.addItem(f'>>> Сохранено в WITHOUT_DUPLICATES-{QFileInfo(self.file).fileName()}')
    #     else:
    #         self.message('Файл не выбран')

    def suspecting(self, dtframe):
        self.ui.lst_info.addItem(f'>>> Проверка First Name и Last Name')
        df_susp, susp_cell = self.suspect_cells()
        self.ui.lst_info.addItem(f'>>> Подозрительных ячеек {susp_cell}')
        self.saving(df_susp, 'SUSPECTED', QFileInfo(self.file).fileName())
        self.ui.lst_info.addItem(f'>>> Сохранено в SUSPECTED-{QFileInfo(self.file).fileName()}')

    def suspect_cells(self):
        df_susp = pd.DataFrame(columns=['Столбец', 'Ячейка'])
        columns = ('First Name', 'Last Name')
        susp_cells = 0
        susp_first = self.book.index[self.book['First Name'].str.contains('[%]|[(]|[)]|[.]|[\s]|["]|[0-9]')].values + 2
        susp_second = self.book.index[self.book['Last Name'].str.contains('[%]|[(]|[)]|[.]|[\s]|["]|[0-9]')].values + 2
        for cell_first in susp_first:
            df_susp.loc[len(df_susp.index)] = 'First Name', cell_first
        for cell_second in susp_second:
            df_susp.loc[len(df_susp.index)] = 'Last Name', cell_second
        susp_cells = self.book['First Name'].str.contains('[%]|[(]|[)]|[.]|[\s]|["]|[0-9]').sum() + self.book[
            'Last Name'].str.contains('[%]|[(]|[)]|[.]|[\s]|["]|[0-9]').sum()
        return df_susp, susp_cells

    def onClicked(self):
        self.radioButton = self.sender()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window(app)
    app.exec_()
