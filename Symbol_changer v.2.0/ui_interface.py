from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# from .Icons import rc_icons
from drag_n_drop import ListBoxWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(581, 493)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"QFrame {\n"
" background-color: rgb(255, 255, 255);\n"
" border-radius: 3;\n"
" border-style: solid;\n"
" border-bottom-width: 1;\n"
" border-color: rgb(10, 10, 10);\n"
"}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.header)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: 0;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.appname = QLabel(self.frame_5)
        self.appname.setObjectName(u"appname")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.Weight(75)
        self.appname.setFont(font)
        self.appname.setStyleSheet(u"border-width: 0;\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.appname, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.frame_2)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"QFrame {\n"
" background-color: rgb(255, 255, 255);\n"
" border-radius: 3;\n"
" border-style: solid;\n"
" border-right-width: 1;\n"
" border-color: rgb(10, 10, 10);\n"
"}\n"
"")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.open_btn = QPushButton(self.menu)
        self.open_btn.setObjectName(u"open_btn")
        font1 = QFont()
        font1.setPointSize(32)
        font1.setBold(False)
        font1.Weight(50)
        font1.setKerning(True)
        self.open_btn.setFont(font1)
        self.open_btn.setStyleSheet(u"QPushButton {\n"
" background-color: #005aff;\n"
" border-color: #005aff;\n"
" border-radius:25px;\n"
" max-width:50px;\n"
" max-height:50px;\n"
" min-width:50px;\n"
" min-height:50px;\n"
"}\n"
"QPushButton::hover{\n"
" background-color: #004db9;\n"
"}")
        icon = QIcon()
        icon.addFile('.\Icons\open_file.svg', QSize(), QIcon.Normal)
        self.open_btn.setIcon(icon)
        self.open_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.open_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(self.menu)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.Weight(50)
        self.label_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.wwradio = QRadioButton(self.frame)
        self.wwradio.setObjectName(u"wwradio")

        self.verticalLayout_3.addWidget(self.wwradio)

        self.dachradio = QRadioButton(self.frame)
        self.dachradio.setObjectName(u"dachradio")

        self.verticalLayout_3.addWidget(self.dachradio)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 320, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.info_btn = QPushButton(self.menu)
        self.info_btn.setObjectName(u"info_btn")
        self.info_btn.setStyleSheet(u"QPushButton {\n"
" background-color: #005aff;\n"
" border-color: #005aff;\n"
" border-radius:25px;\n"
" max-width:50px;\n"
" max-height:50px;\n"
" min-width:50px;\n"
" min-height:50px;\n"
"}\n"
"QPushButton::hover{\n"
" background-color: #004db9;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(".\Icons\help.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_btn.setIcon(icon1)
        self.info_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.info_btn, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.menu, 0, Qt.AlignLeft|Qt.AlignTop)

        self.mainbody_container = QFrame(self.frame_2)
        self.mainbody_container.setObjectName(u"mainbody_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainbody_container.sizePolicy().hasHeightForWidth())
        self.mainbody_container.setSizePolicy(sizePolicy1)
        self.mainbody_container.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.mainbody_container.setFrameShape(QFrame.StyledPanel)
        self.mainbody_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mainbody_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 0, 0)
        self.filelist = ListBoxWidget(self.mainbody_container)
        self.filelist.setObjectName(u"filelist")
        self.filelist.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.filelist)

        self.frame_4 = QFrame(self.mainbody_container)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
" background-color: #005aff;\n"
"}\n"
"QPushButton::hover{\n"
" background-color: #004db9;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.mainbody_container)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.mainbody_container)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.resultlist = QListWidget(self.frame_8)
        self.resultlist.setObjectName(u"resultlist")
        self.resultlist.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.resultlist)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_3 = QFrame(self.mainbody_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 0)
        self.concate_btn = QPushButton(self.frame_3)
        self.concate_btn.setObjectName(u"concate_btn")
        self.concate_btn.setStyleSheet(u"QPushButton {\n"
" background-color: #005aff;\n"
"}\n"
"QPushButton::hover{\n"
" background-color: #004db9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.concate_btn)

        self.get_res_btn = QPushButton(self.frame_3)
        self.get_res_btn.setObjectName(u"get_res_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.get_res_btn.sizePolicy().hasHeightForWidth())
        self.get_res_btn.setSizePolicy(sizePolicy2)
        self.get_res_btn.setMinimumSize(QSize(0, 20))
        self.get_res_btn.setStyleSheet(u"QPushButton {\n"
" background-color: #005aff;\n"
"}\n"
"QPushButton::hover{\n"
" background-color: #004db9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.get_res_btn)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.mainbody_container)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.appname.setText(QCoreApplication.translate("MainWindow", u"Symbols Changer", None))
#if QT_CONFIG(tooltip)
        self.open_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_btn.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0435\u0433\u0438\u043e\u043d \u0434\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0430 \u0437\u0430\u043c\u0435\u043d\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d:", None))
        self.wwradio.setText(QCoreApplication.translate("MainWindow", u"WW", None))
        self.dachradio.setText(QCoreApplication.translate("MainWindow", u"DACH", None))
#if QT_CONFIG(tooltip)
        self.info_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e\u043c\u043e\u0449\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.info_btn.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440", None))
#if QT_CONFIG(tooltip)
        self.concate_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0431\u044a\u0435\u0434\u0435\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.concate_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
#if QT_CONFIG(tooltip)
        self.get_res_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u0438 \u0437\u0430\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u0438\u043c\u0432\u043e\u043b\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.get_res_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

