# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'introWindow.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_IntroWindow(object):
    def setupUi(self, IntroWindow):
        if not IntroWindow.objectName():
            IntroWindow.setObjectName(u"IntroWindow")
        IntroWindow.setEnabled(True)
        IntroWindow.resize(1431, 712)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IntroWindow.sizePolicy().hasHeightForWidth())
        IntroWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        IntroWindow.setFont(font)
        IntroWindow.setWindowTitle(u"Guess the Country")
        IntroWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(IntroWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMinimumSize(QSize(0, 60))
        self.start_btn.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.start_btn.setFont(font1)
        self.start_btn.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"padding: 5px;	\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"border-radius: 10;\n"
"background-color: rgb(255, 120, 0);")

        self.horizontalLayout.addWidget(self.start_btn)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 60))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3;")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.status_label.setFont(font2)
        self.status_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 5px;	\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"border-radius: 10;\n"
"background-color: rgb(28, 113, 216);")

        self.gridLayout.addWidget(self.status_label, 6, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setPixmap(QPixmap(u"GUI/resource_files/intro.png"))

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        IntroWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(IntroWindow)

        QMetaObject.connectSlotsByName(IntroWindow)
    # setupUi

    def retranslateUi(self, IntroWindow):
        self.start_btn.setText(QCoreApplication.translate("IntroWindow", u"Start !!", None))
        self.label_2.setText(QCoreApplication.translate("IntroWindow", u"<html><head/><body><p align=\"center\">GUESS THE COUNTRY</p></body></html>", None))
        self.status_label.setText(QCoreApplication.translate("IntroWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText("")
        pass
    # retranslateUi

