# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gamewindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        if not GameWindow.objectName():
            GameWindow.setObjectName(u"GameWindow")
        GameWindow.setEnabled(True)
        GameWindow.resize(797, 552)
        font = QFont()
        font.setBold(True)
        GameWindow.setFont(font)
        GameWindow.setWindowTitle(u"Guess the Country")
        self.centralwidget = QWidget(GameWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.emoji_label = QLabel(self.centralwidget)
        self.emoji_label.setObjectName(u"emoji_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emoji_label.sizePolicy().hasHeightForWidth())
        self.emoji_label.setSizePolicy(sizePolicy)
        self.emoji_label.setMinimumSize(QSize(400, 50))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.emoji_label.setFont(font1)
        self.emoji_label.setStyleSheet(u"background-color: rgb(153, 193, 241);\n"
"border-color: rgb(26, 95, 180);\n"
"border-radius: 10;")

        self.verticalLayout_2.addWidget(self.emoji_label)

        self.timer_label = QLabel(self.centralwidget)
        self.timer_label.setObjectName(u"timer_label")
        sizePolicy.setHeightForWidth(self.timer_label.sizePolicy().hasHeightForWidth())
        self.timer_label.setSizePolicy(sizePolicy)
        self.timer_label.setMinimumSize(QSize(400, 50))
        self.timer_label.setStyleSheet(u"background-color: rgb(255, 120, 0);\n"
"border-radius: 10;")

        self.verticalLayout_2.addWidget(self.timer_label)

        self.hint_txt = QTextEdit(self.centralwidget)
        self.hint_txt.setObjectName(u"hint_txt")
        sizePolicy.setHeightForWidth(self.hint_txt.sizePolicy().hasHeightForWidth())
        self.hint_txt.setSizePolicy(sizePolicy)
        self.hint_txt.setMinimumSize(QSize(400, 80))
        self.hint_txt.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_2.addWidget(self.hint_txt)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.n_correct_label = QLabel(self.centralwidget)
        self.n_correct_label.setObjectName(u"n_correct_label")
        self.n_correct_label.setMinimumSize(QSize(80, 80))
        self.n_correct_label.setFont(font)
        self.n_correct_label.setStyleSheet(u"background-color: rgb(87, 227, 137);\n"
"border-radius: 4;")

        self.horizontalLayout_2.addWidget(self.n_correct_label)

        self.n_wrong_label = QLabel(self.centralwidget)
        self.n_wrong_label.setObjectName(u"n_wrong_label")
        self.n_wrong_label.setMinimumSize(QSize(80, 80))
        self.n_wrong_label.setFont(font)
        self.n_wrong_label.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"border-radius: 4;")

        self.horizontalLayout_2.addWidget(self.n_wrong_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMaximumSize(QSize(16777215, 40))
        self.status_label.setFont(font1)
        self.status_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 5px;	\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"border-radius: 10;\n"
"background-color: rgb(28, 113, 216);")

        self.gridLayout.addWidget(self.status_label, 11, 0, 1, 2)

        self.live_video_label = QLabel(self.centralwidget)
        self.live_video_label.setObjectName(u"live_video_label")
        self.live_video_label.setAutoFillBackground(False)
        self.live_video_label.setStyleSheet(u"border-radius: 50;\n"
"")
        self.live_video_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.live_video_label, 1, 0, 1, 1)

        GameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameWindow)

        QMetaObject.connectSlotsByName(GameWindow)
    # setupUi

    def retranslateUi(self, GameWindow):
        self.emoji_label.setText("")
        self.timer_label.setText(QCoreApplication.translate("GameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"></span></p></body></html>", None))
        self.hint_txt.setHtml(QCoreApplication.translate("GameWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Symbolized by the Statue of Liberty, representing freedom and democracy. The bald eagle signifies strength and freedom. Hamburgers are iconic in cuisine, and corn is a staple crop.</span></p></body></html>", None))
        self.n_correct_label.setText(QCoreApplication.translate("GameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">12</span></p></body></html>", None))
        self.n_wrong_label.setText(QCoreApplication.translate("GameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">12</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("GameWindow", u"<html><head/><body><p align=\"center\">GUESS THE COUNTRY</p></body></html>", None))
        self.status_label.setText(QCoreApplication.translate("GameWindow", u"<html><head/><body><p align=\"center\">Game status</p></body></html>", None))
        self.live_video_label.setText("")
        pass
    # retranslateUi

