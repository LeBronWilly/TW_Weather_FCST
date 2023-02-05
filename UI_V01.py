# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TW_Weather_FCST_UI_V01GoFzbx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TW_Weather_FCST(object):
    def setupUi(self, TW_Weather_FCST):
        if not TW_Weather_FCST.objectName():
            TW_Weather_FCST.setObjectName(u"TW_Weather_FCST")
        TW_Weather_FCST.resize(913, 508)
        self.Refresh_Button = QPushButton(TW_Weather_FCST)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setEnabled(True)
        self.Refresh_Button.setGeometry(QRect(410, 430, 181, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Refresh_Button.setFont(font)
        self.List_Label = QLabel(TW_Weather_FCST)
        self.List_Label.setObjectName(u"List_Label")
        self.List_Label.setGeometry(QRect(30, 70, 301, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.List_Label.setFont(font1)
        self.List_Label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.WillyF_Label = QLabel(TW_Weather_FCST)
        self.WillyF_Label.setObjectName(u"WillyF_Label")
        self.WillyF_Label.setGeometry(QRect(10, 470, 411, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.WillyF_Label.setFont(font2)
        self.WillyF_Label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Pic_Label = QLabel(TW_Weather_FCST)
        self.Pic_Label.setObjectName(u"Pic_Label")
        self.Pic_Label.setGeometry(QRect(680, 410, 80, 80))
        self.Pic_Label.setFont(font1)
        self.Pic_Label.setAlignment(Qt.AlignCenter)
        self.Location_ComboBox = QComboBox(TW_Weather_FCST)
        self.Location_ComboBox.addItem("")
        self.Location_ComboBox.setObjectName(u"Location_ComboBox")
        self.Location_ComboBox.setGeometry(QRect(320, 70, 481, 41))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        self.Location_ComboBox.setFont(font3)
        self.List_Label_2 = QLabel(TW_Weather_FCST)
        self.List_Label_2.setObjectName(u"List_Label_2")
        self.List_Label_2.setGeometry(QRect(30, 150, 301, 41))
        self.List_Label_2.setFont(font1)
        self.List_Label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Period_ComboBox = QComboBox(TW_Weather_FCST)
        self.Period_ComboBox.addItem("")
        self.Period_ComboBox.setObjectName(u"Period_ComboBox")
        self.Period_ComboBox.setGeometry(QRect(320, 150, 481, 41))
        self.Period_ComboBox.setFont(font3)
        self.Info_Table = QTableWidget(TW_Weather_FCST)
        self.Info_Table.setObjectName(u"Info_Table")
        self.Info_Table.setGeometry(QRect(30, 270, 851, 141))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.Info_Table.setFont(font4)
        self.Info_Table.setAlternatingRowColors(False)
        self.label_4 = QLabel(TW_Weather_FCST)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 230, 461, 31))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setTextFormat(Qt.MarkdownText)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Search_Button = QPushButton(TW_Weather_FCST)
        self.Search_Button.setObjectName(u"Search_Button")
        self.Search_Button.setEnabled(True)
        self.Search_Button.setGeometry(QRect(470, 220, 181, 41))
        self.Search_Button.setFont(font)
        self.Pic_Label_2 = QLabel(TW_Weather_FCST)
        self.Pic_Label_2.setObjectName(u"Pic_Label_2")
        self.Pic_Label_2.setGeometry(QRect(890, 400, 80, 80))
        self.Pic_Label_2.setFont(font1)
        self.Pic_Label_2.setAlignment(Qt.AlignCenter)
        self.Pic_Label.raise_()
        self.List_Label.raise_()
        self.WillyF_Label.raise_()
        self.Refresh_Button.raise_()
        self.Location_ComboBox.raise_()
        self.List_Label_2.raise_()
        self.Period_ComboBox.raise_()
        self.Info_Table.raise_()
        self.label_4.raise_()
        self.Search_Button.raise_()
        self.Pic_Label_2.raise_()

        self.retranslateUi(TW_Weather_FCST)

        QMetaObject.connectSlotsByName(TW_Weather_FCST)
    # setupUi

    def retranslateUi(self, TW_Weather_FCST):
        TW_Weather_FCST.setWindowTitle(QCoreApplication.translate("TW_Weather_FCST", u"TW_Weather_FCST", None))
        self.Refresh_Button.setText(QCoreApplication.translate("TW_Weather_FCST", u"Refresh Data", None))
        self.List_Label.setText(QCoreApplication.translate("TW_Weather_FCST", u"Location List:", None))
        self.WillyF_Label.setText(QCoreApplication.translate("TW_Weather_FCST", u"Developed by WillyF", None))
        self.Pic_Label.setText("")
        self.Location_ComboBox.setItemText(0, QCoreApplication.translate("TW_Weather_FCST", u"Choose City/County", None))

        self.Location_ComboBox.setCurrentText(QCoreApplication.translate("TW_Weather_FCST", u"Choose City/County", None))
        self.List_Label_2.setText(QCoreApplication.translate("TW_Weather_FCST", u"FCST Period List:", None))
        self.Period_ComboBox.setItemText(0, QCoreApplication.translate("TW_Weather_FCST", u"Choose Time Period", None))

        self.Period_ComboBox.setCurrentText(QCoreApplication.translate("TW_Weather_FCST", u"Choose Time Period", None))
        self.label_4.setText(QCoreApplication.translate("TW_Weather_FCST", u"Weather Forecast Info:", None))
        self.Search_Button.setText(QCoreApplication.translate("TW_Weather_FCST", u"Search", None))
        self.Pic_Label_2.setText("")
    # retranslateUi

