# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TW_Weather_FCST_UI_V02agVujZ.ui'
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
        TW_Weather_FCST.resize(1841, 621)
        self.Refresh_Button = QPushButton(TW_Weather_FCST)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setEnabled(True)
        self.Refresh_Button.setGeometry(QRect(690, 550, 201, 41))
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
        self.WillyF_Label.setGeometry(QRect(10, 580, 411, 31))
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
        self.Pic_Label.setGeometry(QRect(1730, 530, 80, 80))
        self.Pic_Label.setFont(font1)
        self.Pic_Label.setFrameShape(QFrame.NoFrame)
        self.Pic_Label.setAlignment(Qt.AlignCenter)
        self.Location_ComboBox = QComboBox(TW_Weather_FCST)
        self.Location_ComboBox.addItem("")
        self.Location_ComboBox.setObjectName(u"Location_ComboBox")
        self.Location_ComboBox.setGeometry(QRect(320, 70, 351, 41))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        self.Location_ComboBox.setFont(font3)
        self.List_Label_2 = QLabel(TW_Weather_FCST)
        self.List_Label_2.setObjectName(u"List_Label_2")
        self.List_Label_2.setGeometry(QRect(850, 70, 301, 41))
        self.List_Label_2.setFont(font1)
        self.List_Label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Region_ComboBox = QComboBox(TW_Weather_FCST)
        self.Region_ComboBox.addItem("")
        self.Region_ComboBox.setObjectName(u"Region_ComboBox")
        self.Region_ComboBox.setGeometry(QRect(1140, 70, 351, 41))
        self.Region_ComboBox.setFont(font3)
        self.Info_Table = QTableWidget(TW_Weather_FCST)
        self.Info_Table.setObjectName(u"Info_Table")
        self.Info_Table.setGeometry(QRect(30, 310, 1781, 211))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.Info_Table.setFont(font4)
        self.Info_Table.setAlternatingRowColors(False)
        self.label_4 = QLabel(TW_Weather_FCST)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 250, 411, 41))
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
        self.Search_Button.setGeometry(QRect(370, 250, 251, 41))
        self.Search_Button.setFont(font)
        self.Update_Time_Label = QLabel(TW_Weather_FCST)
        self.Update_Time_Label.setObjectName(u"Update_Time_Label")
        self.Update_Time_Label.setGeometry(QRect(1400, 10, 411, 31))
        self.Update_Time_Label.setFont(font2)
        self.Update_Time_Label.setLayoutDirection(Qt.RightToLeft)
        self.Update_Time_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Period_ComboBox = QComboBox(TW_Weather_FCST)
        self.Period_ComboBox.addItem("")
        self.Period_ComboBox.setObjectName(u"Period_ComboBox")
        self.Period_ComboBox.setGeometry(QRect(320, 170, 351, 41))
        self.Period_ComboBox.setFont(font3)
        self.List_Label_3 = QLabel(TW_Weather_FCST)
        self.List_Label_3.setObjectName(u"List_Label_3")
        self.List_Label_3.setGeometry(QRect(30, 170, 301, 41))
        self.List_Label_3.setFont(font1)
        self.List_Label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.List_Label_4 = QLabel(TW_Weather_FCST)
        self.List_Label_4.setObjectName(u"List_Label_4")
        self.List_Label_4.setGeometry(QRect(850, 170, 351, 41))
        self.List_Label_4.setFont(font1)
        self.List_Label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.List_Label_5 = QLabel(TW_Weather_FCST)
        self.List_Label_5.setObjectName(u"List_Label_5")
        self.List_Label_5.setGeometry(QRect(850, 220, 961, 41))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        self.List_Label_5.setFont(font6)
        self.List_Label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.List_Label_6 = QLabel(TW_Weather_FCST)
        self.List_Label_6.setObjectName(u"List_Label_6")
        self.List_Label_6.setGeometry(QRect(850, 250, 961, 41))
        self.List_Label_6.setFont(font6)
        self.List_Label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Field_Desc_Table = QTableWidget(TW_Weather_FCST)
        if (self.Field_Desc_Table.columnCount() < 11):
            self.Field_Desc_Table.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.Field_Desc_Table.rowCount() < 1):
            self.Field_Desc_Table.setRowCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.Field_Desc_Table.setItem(0, 10, __qtablewidgetitem22)
        self.Field_Desc_Table.setObjectName(u"Field_Desc_Table")
        self.Field_Desc_Table.setGeometry(QRect(850, 220, 961, 71))
        font7 = QFont()
        font7.setPointSize(9)
        self.Field_Desc_Table.setFont(font7)
        self.Field_Desc_Table.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.Field_Desc_Table.setLayoutDirection(Qt.LeftToRight)
        self.Field_Desc_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Field_Desc_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Field_Desc_Table.horizontalHeader().setCascadingSectionResizes(False)
        self.Field_Desc_Table.verticalHeader().setCascadingSectionResizes(False)
        self.Pic_Label.raise_()
        self.List_Label.raise_()
        self.WillyF_Label.raise_()
        self.Refresh_Button.raise_()
        self.Location_ComboBox.raise_()
        self.Info_Table.raise_()
        self.label_4.raise_()
        self.Search_Button.raise_()
        self.Update_Time_Label.raise_()
        self.Period_ComboBox.raise_()
        self.List_Label_3.raise_()
        self.Region_ComboBox.raise_()
        self.List_Label_2.raise_()
        self.List_Label_4.raise_()
        self.List_Label_5.raise_()
        self.List_Label_6.raise_()
        self.Field_Desc_Table.raise_()

        self.retranslateUi(TW_Weather_FCST)

        QMetaObject.connectSlotsByName(TW_Weather_FCST)
    # setupUi

    def retranslateUi(self, TW_Weather_FCST):
        TW_Weather_FCST.setWindowTitle(QCoreApplication.translate("TW_Weather_FCST", u"7-Day Taiwan Weather Forecast", None))
        self.Refresh_Button.setText(QCoreApplication.translate("TW_Weather_FCST", u"Refresh Data", None))
        self.List_Label.setText(QCoreApplication.translate("TW_Weather_FCST", u"Location List:", None))
        self.WillyF_Label.setText(QCoreApplication.translate("TW_Weather_FCST", u"Developed by WillyF", None))
        self.Pic_Label.setText("")
        self.Location_ComboBox.setItemText(0, QCoreApplication.translate("TW_Weather_FCST", u"Choose City/County", None))

        self.Location_ComboBox.setCurrentText(QCoreApplication.translate("TW_Weather_FCST", u"Choose City/County", None))
        self.List_Label_2.setText(QCoreApplication.translate("TW_Weather_FCST", u"Region List:", None))
        self.Region_ComboBox.setItemText(0, QCoreApplication.translate("TW_Weather_FCST", u"Choose Region", None))

        self.Region_ComboBox.setCurrentText(QCoreApplication.translate("TW_Weather_FCST", u"Choose Region", None))
        self.label_4.setText(QCoreApplication.translate("TW_Weather_FCST", u"Weather Forecast Info:", None))
        self.Search_Button.setText(QCoreApplication.translate("TW_Weather_FCST", u"Search", None))
        self.Update_Time_Label.setText("")
        self.Period_ComboBox.setItemText(0, QCoreApplication.translate("TW_Weather_FCST", u"Choose Period", None))

        self.Period_ComboBox.setCurrentText(QCoreApplication.translate("TW_Weather_FCST", u"Choose Period", None))
        self.List_Label_3.setText(QCoreApplication.translate("TW_Weather_FCST", u"Period List:", None))
        self.List_Label_4.setText(QCoreApplication.translate("TW_Weather_FCST", u"Fields Description:", None))
        self.List_Label_5.setText(QCoreApplication.translate("TW_Weather_FCST", u"     12hr PoP\u3000\u3000\u3000 T         AvgT          AT             AvgRH            AvgDPT            UVI          MaxWS       BWS       WD       CI", None))
        self.List_Label_6.setText(QCoreApplication.translate("TW_Weather_FCST", u"12\u5c0f\u6642\u964d\u96e8\u6a5f\u7387\u3000\u6eab\u5ea6\u3000\u5e73\u5747\u6eab\u5ea6\u3000\u9ad4\u611f\u6eab\u5ea6\u3000\u5e73\u5747\u76f8\u5c0d\u6fd5\u5ea6\u3000\u5e73\u5747\u9732\u9ede\u6eab\u5ea6\u3000\u7d2b\u5916\u7dda\u6307\u6578\u3000\u6700\u5927\u98a8\u901f\u3000\u84b2\u798f\u98a8\u7d1a\u3000\u98a8\u5411\u3000\u8212\u9069\u5ea6", None))
        ___qtablewidgetitem = self.Field_Desc_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TW_Weather_FCST", u"12hr Pop", None));
        ___qtablewidgetitem1 = self.Field_Desc_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TW_Weather_FCST", u"T", None));
        ___qtablewidgetitem2 = self.Field_Desc_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TW_Weather_FCST", u"AvgT", None));
        ___qtablewidgetitem3 = self.Field_Desc_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TW_Weather_FCST", u"AT", None));
        ___qtablewidgetitem4 = self.Field_Desc_Table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TW_Weather_FCST", u"AvgRH", None));
        ___qtablewidgetitem5 = self.Field_Desc_Table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TW_Weather_FCST", u"AvgDPT", None));
        ___qtablewidgetitem6 = self.Field_Desc_Table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TW_Weather_FCST", u"UVI", None));
        ___qtablewidgetitem7 = self.Field_Desc_Table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TW_Weather_FCST", u"MaxWS", None));
        ___qtablewidgetitem8 = self.Field_Desc_Table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TW_Weather_FCST", u"BWS", None));
        ___qtablewidgetitem9 = self.Field_Desc_Table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TW_Weather_FCST", u"WD", None));
        ___qtablewidgetitem10 = self.Field_Desc_Table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TW_Weather_FCST", u"CI", None));
        ___qtablewidgetitem11 = self.Field_Desc_Table.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TW_Weather_FCST", u"Desc.", None));

        __sortingEnabled = self.Field_Desc_Table.isSortingEnabled()
        self.Field_Desc_Table.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.Field_Desc_Table.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TW_Weather_FCST", u"12\u5c0f\u6642\u964d\u96e8\u6a5f\u7387", None));
        ___qtablewidgetitem13 = self.Field_Desc_Table.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u6eab\u5ea6", None));
        ___qtablewidgetitem14 = self.Field_Desc_Table.item(0, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u5e73\u5747\u6eab\u5ea6", None));
        ___qtablewidgetitem15 = self.Field_Desc_Table.item(0, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u9ad4\u611f\u6eab\u5ea6", None));
        ___qtablewidgetitem16 = self.Field_Desc_Table.item(0, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u5e73\u5747\u76f8\u5c0d\u6fd5\u5ea6", None));
        ___qtablewidgetitem17 = self.Field_Desc_Table.item(0, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u5e73\u5747\u9732\u9ede\u6eab\u5ea6", None));
        ___qtablewidgetitem18 = self.Field_Desc_Table.item(0, 6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u7d2b\u5916\u7dda\u6307\u6578", None));
        ___qtablewidgetitem19 = self.Field_Desc_Table.item(0, 7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u6700\u5927\u98a8\u901f", None));
        ___qtablewidgetitem20 = self.Field_Desc_Table.item(0, 8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u84b2\u798f\u98a8\u7d1a", None));
        ___qtablewidgetitem21 = self.Field_Desc_Table.item(0, 9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u98a8\u5411", None));
        ___qtablewidgetitem22 = self.Field_Desc_Table.item(0, 10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("TW_Weather_FCST", u"\u8212\u9069\u5ea6", None));
        self.Field_Desc_Table.setSortingEnabled(__sortingEnabled)

    # retranslateUi

