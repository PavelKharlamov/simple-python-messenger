# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Messenger(object):
    def setupUi(self, Messenger):
        if Messenger.objectName():
            Messenger.setObjectName(u"Messenger")
        Messenger.resize(285, 530)
        self.centralwidget = QWidget(Messenger)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        Messenger.setCentralWidget(self.centralwidget)

        self.retranslateUi(Messenger)

        QMetaObject.connectSlotsByName(Messenger)
    # setupUi

    def retranslateUi(self, Messenger):
        Messenger.setWindowTitle(QCoreApplication.translate("Messenger", u"Messenger", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Messenger", u"Waiting for server connection...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Messenger", u"Enter your message...", None))
        self.pushButton.setText(QCoreApplication.translate("Messenger", u"Send", None))
    # retranslateUi

