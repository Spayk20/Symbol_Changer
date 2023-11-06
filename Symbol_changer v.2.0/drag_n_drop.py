import os
from PySide6.QtCore import *
from PySide6.QtWidgets import *

lnklist = []


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            # files = [(u.toLocalFile()) for u in event.mimeData().urls()]
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                if os.path.basename(url.toLocalFile())[-3::1] == 'xls':
                    links.append(os.path.basename(url.toLocalFile()))
                    lnklist.append(url.toLocalFile())
            self.addItems(links)
        else:
            event.ignore()
