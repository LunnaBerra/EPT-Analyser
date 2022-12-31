# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EPT_GUILDOlJi.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

'''from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
import PySide6.QtWidgets'''
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import sys

class Ui_MainWindow(object):
    app = QApplication(sys.argv)
    def __init__(self):
        win = QMainWindow()
        win.setObjectName("MainWindow")
        self.setupUi(win)
        win.show()
        sys.exit(self.app.exec_())

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1463, 1276)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 54, 163, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.centralwidget.setPalette(palette1)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1322, 958))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.image_team1 = QGraphicsView(self.verticalLayoutWidget)
        self.image_team1.setObjectName(u"image_team1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_team1.sizePolicy().hasHeightForWidth())
        self.image_team1.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.image_team1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.comboBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.image_team2 = QGraphicsView(self.verticalLayoutWidget)
        self.image_team2.setObjectName(u"image_team2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.image_team2.sizePolicy().hasHeightForWidth())
        self.image_team2.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.image_team2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.comboBox_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.dial_form_team1 = QDial(self.verticalLayoutWidget)
        self.dial_form_team1.setObjectName(u"dial_form_team1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dial_form_team1.sizePolicy().hasHeightForWidth())
        self.dial_form_team1.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        brush2 = QBrush(QColor(209, 209, 209, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        self.dial_form_team1.setPalette(palette2)
        self.dial_form_team1.setAutoFillBackground(True)
        self.dial_form_team1.setMaximum(200)
        self.dial_form_team1.setSingleStep(1)
        self.dial_form_team1.setSliderPosition(100)
        self.dial_form_team1.setNotchesVisible(True)

        self.verticalLayout_13.addWidget(self.dial_form_team1)

        self.dial_form_team1_value = QLabel(self.verticalLayoutWidget)
        self.dial_form_team1_value.setObjectName(u"dial_form_team1_value")
        self.dial_form_team1_value.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.dial_form_team1_value.sizePolicy().hasHeightForWidth())
        self.dial_form_team1_value.setSizePolicy(sizePolicy4)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.dial_form_team1_value.setPalette(palette3)
        self.dial_form_team1_value.setAutoFillBackground(True)

        self.verticalLayout_13.addWidget(self.dial_form_team1_value)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label.setPalette(palette4)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QFrame.Box)

        self.verticalLayout_14.addWidget(self.label)

        self.results_team1 = QTextBrowser(self.verticalLayoutWidget)
        self.results_team1.setObjectName(u"results_team1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.results_team1.sizePolicy().hasHeightForWidth())
        self.results_team1.setSizePolicy(sizePolicy5)

        self.verticalLayout_14.addWidget(self.results_team1)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_2.setPalette(palette5)
        self.label_2.setAutoFillBackground(True)

        self.verticalLayout_15.addWidget(self.label_2)

        self.results_team2 = QTextBrowser(self.verticalLayoutWidget)
        self.results_team2.setObjectName(u"results_team2")
        sizePolicy5.setHeightForWidth(self.results_team2.sizePolicy().hasHeightForWidth())
        self.results_team2.setSizePolicy(sizePolicy5)
        self.results_team2.setAutoFillBackground(False)

        self.verticalLayout_15.addWidget(self.results_team2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.dial_form_team2 = QDial(self.verticalLayoutWidget)
        self.dial_form_team2.setObjectName(u"dial_form_team2")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        self.dial_form_team2.setPalette(palette6)
        self.dial_form_team2.setFocusPolicy(Qt.WheelFocus)
        self.dial_form_team2.setContextMenuPolicy(Qt.NoContextMenu)
        self.dial_form_team2.setAutoFillBackground(True)
        self.dial_form_team2.setMaximum(200)
        self.dial_form_team2.setSliderPosition(100)
        self.dial_form_team2.setWrapping(False)
        self.dial_form_team2.setNotchesVisible(True)

        self.verticalLayout_16.addWidget(self.dial_form_team2)

        self.dial_form_team2_value = QLabel(self.verticalLayoutWidget)
        self.dial_form_team2_value.setObjectName(u"dial_form_team2_value")
        sizePolicy4.setHeightForWidth(self.dial_form_team2_value.sizePolicy().hasHeightForWidth())
        self.dial_form_team2_value.setSizePolicy(sizePolicy4)
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.dial_form_team2_value.setPalette(palette7)
        self.dial_form_team2_value.setAutoFillBackground(True)

        self.verticalLayout_16.addWidget(self.dial_form_team2_value)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_5.setPalette(palette8)
        self.label_5.setAutoFillBackground(True)

        self.verticalLayout_12.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.subscores_team1 = QTextBrowser(self.verticalLayoutWidget)
        self.subscores_team1.setObjectName(u"subscores_team1")
        sizePolicy5.setHeightForWidth(self.subscores_team1.sizePolicy().hasHeightForWidth())
        self.subscores_team1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.subscores_team1)

        self.recomendations_score_team1 = QTextBrowser(self.verticalLayoutWidget)
        self.recomendations_score_team1.setObjectName(u"recomendations_score_team1")
        sizePolicy5.setHeightForWidth(self.recomendations_score_team1.sizePolicy().hasHeightForWidth())
        self.recomendations_score_team1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.recomendations_score_team1)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_12)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_4.setPalette(palette9)
        self.label_4.setAutoFillBackground(True)

        self.verticalLayout_17.addWidget(self.label_4)

        self.textBrowser_2 = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy6)

        self.verticalLayout_17.addWidget(self.textBrowser_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_3.setPalette(palette10)
        self.label_3.setAutoFillBackground(True)

        self.verticalLayout_17.addWidget(self.label_3)

        self.textBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy6.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy6)

        self.verticalLayout_17.addWidget(self.textBrowser)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_17.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_17)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_6.setPalette(palette11)
        self.label_6.setAutoFillBackground(True)

        self.verticalLayout_11.addWidget(self.label_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.subscores_team2 = QTextBrowser(self.verticalLayoutWidget)
        self.subscores_team2.setObjectName(u"subscores_team2")
        sizePolicy5.setHeightForWidth(self.subscores_team2.sizePolicy().hasHeightForWidth())
        self.subscores_team2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.subscores_team2)

        self.recomendations_score_team2 = QTextBrowser(self.verticalLayoutWidget)
        self.recomendations_score_team2.setObjectName(u"recomendations_score_team2")
        sizePolicy5.setHeightForWidth(self.recomendations_score_team2.sizePolicy().hasHeightForWidth())
        self.recomendations_score_team2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.recomendations_score_team2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dial_form_team1_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">100</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Predicted Goals</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Predicted Goals</span></p></body></html>", None))
        self.dial_form_team2_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">100</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:600; text-decoration: underline;\">Recommendations and Scores</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Predicted Goals</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Predicted Goals</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:600; text-decoration: underline;\">Recommendations and Scores</span></p></body></html>", None))
    # retranslateUi

