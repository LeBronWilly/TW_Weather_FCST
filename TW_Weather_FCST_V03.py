# -*- coding: utf-8 -*-
"""
Created on 08/06, 2023
@author: WillyF

"""

# https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
# https://opendata.cwb.gov.tw/dataset/forecast/F-C0032-001
# https://opendata.cwb.gov.tw/dist/opendata-swagger.html?urls.primaryName=openAPI#/%E9%A0%90%E5%A0%B1/get_v1_rest_datastore_F_C0032_001
# https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
# https://stackoverflow.com/questions/31306741/unmelt-pandas-dataframe
# https://medium.com/%E6%95%B8%E6%93%9A%E4%B8%8D%E6%AD%A2-not-only-data/pandas-%E5%BF%AB%E9%80%9F%E7%9E%AD%E8%A7%A3-pivot-table-%E8%88%87%E6%87%89%E7%94%A8-21e4c37b9216
# https://docs.python.org/3/library/stdtypes.html#str.isdigit
# https://datagy.io/python-string-to-date/
# https://www.itsolutionstuff.com/post/how-to-check-if-today-is-wednesday-or-not-in-pythonexample.html
# https://stackoverflow.com/questions/19289171/importing-a-variable-from-one-python-script-to-another
# https://blog.netwrix.com/2022/11/14/how-to-hide-api-keys-github/


from UI_V03 import *
import pandas as pd
import urllib.request
import json
# import numpy as np
from datetime import datetime, timedelta
from apikeyconfig import api_key_WF
from PySide2 import QtWebEngineWidgets
import plotly.graph_objects as go

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# import warnings
# warnings.filterwarnings("ignore")
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.max_rows', 1000)


def FCST_data_refresh_ETL():
    TW_Region = pd.read_csv(
        "https://github.com/LeBronWilly/TW_Weather_FCST/raw/main/TW_Region.csv",
        encoding='utf8')
    # api_key_WF = "XXXXX"
    data_source = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=" + api_key_WF + "&sort=time"
    json_url = urllib.request.urlopen(data_source)
    data = json.loads(json_url.read())
    days_name = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."]
    data_df = pd.json_normalize(data["records"],
                                record_path=['locations', "location", "weatherElement", 'time', "elementValue"],
                                meta=[['locations', 'location', 'locationName'],
                                      ['locations', 'location', 'lon'],
                                      ['locations', 'location', 'lat'],
                                      ['locations', "location", "weatherElement", "elementName"],
                                      ['locations', "location", "weatherElement", "description"],
                                      ['locations', "location", "weatherElement", 'time', "startTime"],
                                      ['locations', "location", "weatherElement", 'time', "endTime"]])
    data_df.columns = ["Value", "Unit", "Location", "Long", "Lat", "Element_EN", "Element", "StartTime", "EndTime"]
    data_df = data_df[["StartTime", "EndTime", "Location", "Element", "Element_EN", "Value", "Unit", "Long", "Lat"]]
    data_df = data_df[data_df["Unit"] != "自定義 Wx 單位"].reset_index(drop=True)
    data_df["Unit"].replace("百分比", "%", inplace=True)
    data_df["Unit"].replace("8方位", "", inplace=True)
    data_df["Unit"].replace("紫外線指數", "", inplace=True)
    data_df["Unit"].replace("攝氏度", "°C", inplace=True)
    data_df["Unit"].replace("公尺/秒", "m/s", inplace=True)
    data_df["Unit"].replace("自定義 CI 文字", "", inplace=True)
    data_df["Unit"].replace("自定義 Wx 文字", "", inplace=True)
    data_df["Unit"].replace("自定義 Wx 單位", "", inplace=True)
    data_df.loc[(data_df["Element"].str.contains("紫外線指數")) & (data_df["Unit"].str.contains("曝曬級數")),
    "Element"] = "曝曬級數"
    data_df.loc[(data_df["Element"].str.contains("最大風速")) & (data_df["Unit"].str.contains("蒲福風級")),
    "Element"] = "蒲福風級"
    data_df.loc[(data_df["Element"].str.contains("最大舒適度指數")) & (~data_df["Value"].str.isdigit()),
    "Element"] = "最大舒適度"
    data_df.loc[(data_df["Element"].str.contains("最小舒適度指數")) & (~data_df["Value"].str.isdigit()),
    "Element"] = "最小舒適度"
    data_df["Unit"].replace("曝曬級數", "", inplace=True)
    data_df["Unit"].replace("蒲福風級", "", inplace=True)
    data_df["Unit"].replace("NA", "", inplace=True)
    data_df["Unit"].replace("NA ", "", inplace=True)
    data_df["Unit"].replace(" ", "", inplace=True)
    data_df["Value"].replace("<= 1", "≤1", inplace=True)
    data_df["Parameter"] = data_df["Value"] + data_df["Unit"]
    data_df["Parameter"].replace(" %", "-", inplace=True)
    data_df["StartTime"] = data_df["StartTime"].apply(lambda x: x.replace("-", "/")[:-3])
    data_df["StartTime"] = data_df["StartTime"].apply(
        lambda x: x + " (" + days_name[datetime.strptime(x, '%Y/%m/%d %H:%M').weekday()] + ")")
    data_df["Date"] = data_df["StartTime"].apply(lambda x: x.split(" ")[0] + " " + x.split(" ")[-1])
    data_df["EndTime"] = data_df["EndTime"].apply(lambda x: x.replace("-", "/")[:-3])
    data_df["EndTime"] = data_df["EndTime"].apply(
        lambda x: x + " (" + days_name[datetime.strptime(x, '%Y/%m/%d %H:%M').weekday()] + ")")
    data_df = data_df.merge(TW_Region, how="left", left_on='Location', right_on='City/County', validate="many_to_one")
    data_df["Location"].replace("臺", "台", inplace=True, regex=True)
    data_df["Long"] = data_df["Long"].astype(float)
    data_df["Lat"] = data_df["Lat"].astype(float)
    data_df_pivot = pd.pivot_table(data_df,
                                   index=["StartTime", "Date", "EndTime", "Region", 'Location'],
                                   columns=["Element"],
                                   values=["Parameter"],
                                   aggfunc=lambda x: x).reset_index()
    data_df_pivot.columns = ["StartTime", "Date", "EndTime", "Region", "Location", "12hr PoP", "Weather FCST",
                             "Weather Desc",
                             "AvgT", "AvgRH", "AvgDPT", "EL", "MinT", "MinAT", "MaxC", "MaxCI",
                             "MaxWS", "MinC", "MinCI", "MaxT", "MaxAT", "UVI", "BWS", "WD"]
    # 平均相對濕度、平均露點溫度、曝曬級數、蒲福風級
    data_df_pivot = data_df_pivot.sort_values(by=["Region", "Location", "StartTime", "EndTime"]).reset_index(drop=True)
    data_df_pivot_graph = data_df_pivot.copy()[
        ["StartTime", "Location", "MinT", "MaxT", "AvgT", "AvgDPT", "MinAT", "MaxAT"]]
    data_df_pivot["Period"] = data_df_pivot["StartTime"].str.cat(data_df_pivot["EndTime"], sep=" ~ ")
    data_df_pivot["T"] = data_df_pivot["MinT"].str.cat(data_df_pivot["MaxT"], sep=" ~ ")
    data_df_pivot["AT"] = data_df_pivot["MinAT"].str.cat(data_df_pivot["MaxAT"], sep=" ~ ")
    data_df_pivot["C"] = data_df_pivot["MinC"].str.cat(data_df_pivot["MaxC"], sep=" ~ ")
    data_df_pivot["CI"] = data_df_pivot["MinCI"].str.cat(data_df_pivot["MaxCI"], sep=" ~ ")
    data_df_pivot["EL"].fillna("-", inplace=True)
    data_df_pivot["CI"] = data_df_pivot["CI"] + " (" + data_df_pivot["C"] + ")"
    data_df_pivot["UVI"] = data_df_pivot["UVI"] + " (" + data_df_pivot["EL"] + ")"
    data_df_pivot["UVI"].fillna("-", inplace=True)
    data_df_pivot = data_df_pivot[
        ["Date", "Period", "Region", "Location", "Weather FCST", "12hr PoP", "T", "AvgT", "AT",
         "AvgRH", "AvgDPT", "UVI",
         "MaxWS", "BWS", "WD", "CI", "Weather Desc"]]
    data_df_pivot_graph['MinT'] = data_df_pivot_graph['MinT'].apply(lambda x: int(x.replace("°C", "")))
    data_df_pivot_graph['MaxT'] = data_df_pivot_graph['MaxT'].apply(lambda x: int(x.replace("°C", "")))
    data_df_pivot_graph["AvgT"] = data_df_pivot_graph["AvgT"].apply(lambda x: int(x.replace("°C", "")))
    data_df_pivot_graph["AvgDPT"] = data_df_pivot_graph["AvgDPT"].apply(lambda x: int(x.replace("°C", "")))
    data_df_pivot_graph["MinAT"] = data_df_pivot_graph["MinAT"].apply(lambda x: int(x.replace("°C", "")))
    data_df_pivot_graph["MaxAT"] = data_df_pivot_graph["MaxAT"].apply(lambda x: int(x.replace("°C", "")))
    data_df_pivot_graph["StartTime"] = data_df_pivot_graph["StartTime"].apply(
        lambda x: datetime.strptime(x.split("(")[0].strip(), '%Y/%m/%d %H:%M'))
    data_df_pivot_graph["StartTime"] = pd.to_datetime(data_df_pivot_graph['StartTime'])
    return data_df_pivot, data_df_pivot_graph


Region_Order = {"北部地區": 0, "中部地區": 1, "南部地區": 2, "東部地區": 3, "外島地區": 4}


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TW_Weather_FCST()
        self.ui.setupUi(self)
        self.Chart_Plotly = QtWebEngineWidgets.QWebEngineView(self)
        self.Chart_Plotly.setGeometry(QRect(30, 449, 1781, 311))
        self.Chart_Plotly.setContentsMargins(1, 1, 1, 1)
        print("Loading Taiwan Weather Data......")
        self.FCST_data = None
        self.FCST_chart_data = None
        # self.WX_img = None
        # self.setWindowIcon(QIcon("weather-forecast.png"))
        self.setup_control()
        print("Done!")
        self.show()

    def setup_control(self):
        self.ui.WinIcon_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/TW_Weather_FCST/main/weather-forecast.png'
        img_data = urllib.request.urlopen(url).read()
        self.ui.WinIcon_img.loadFromData(img_data)
        self.ui.WinIcon_img = self.ui.WinIcon_img.scaled(75, 75)
        self.setWindowIcon(QIcon(self.ui.WinIcon_img))
        # self.WX_img = QPixmap('weather-forecast.png').scaled(75, 75)
        # self.WX_img = self.ui.WinIcon_img
        # self.ui.Pic_Label.setPixmap(self.WX_img)
        self.ui.Pic_Label.setPixmap(self.ui.WinIcon_img)
        self.ui.Pic_Label.setAlignment(Qt.AlignCenter)
        self.Chart_Plotly.setHtml("")
        self.ui.Info_Table.clear()
        self.ui.Info_Table.setColumnCount(0)
        self.ui.Info_Table.setRowCount(0)
        self.ui.Field_Desc_Table.resizeColumnsToContents()
        # self.ui.Field_Desc_Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Field_Desc_Table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.FCST_data, self.FCST_chart_data = FCST_data_refresh_ETL()
        self.ui.Period_ComboBox.clear()
        self.ui.Period_ComboBox.addItem("所有期間")
        self.ui.period_list = sorted(set(self.FCST_data["Date"]))
        for period in self.ui.period_list:
            self.ui.Period_ComboBox.addItem(period)
        self.ui.Region_ComboBox.clear()
        self.ui.Region_ComboBox.addItem("所有地區 (北/中/南/東/外島)")
        self.ui.region_list = sorted(set(self.FCST_data["Region"]), key=lambda x: Region_Order[x])
        for region in self.ui.region_list:
            self.ui.Region_ComboBox.addItem(region)
        self.ui.Location_ComboBox.clear()
        self.ui.loc_list = sorted(set(self.FCST_data["Location"]))
        for loc in self.ui.loc_list:
            self.ui.Location_ComboBox.addItem(loc)
        self.ui.Location_ComboBox.setCurrentText("新竹市")
        self.ui.Refresh_Button.clicked.connect(self.Refresh_Button_Clicked)
        self.ui.Search_Button.clicked.connect(
            lambda: self.Search_Button_Clicked(self.ui.Location_ComboBox.currentText(),
                                               self.ui.Period_ComboBox.currentText()))
        self.ui.Region_ComboBox.currentTextChanged.connect(
            lambda: self.Region_Change(self.ui.Region_ComboBox.currentText()))
        self.ui.Update_Time_Label.setText("Data Last Updated: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    def Region_Change(self, Region_Name):
        if Region_Name is None:
            return None
        if Region_Name == "所有地區 (北/中/南/東/外島)":
            current_loc = self.ui.Location_ComboBox.currentText()
            # self.ui.Period_ComboBox.clear()
            # self.ui.Period_ComboBox.addItem("所有期間")
            # self.ui.period_list = sorted(set(self.FCST_data["Period"]))
            # for period in self.ui.period_list:
            #     self.ui.Period_ComboBox.addItem(period)
            self.ui.Location_ComboBox.clear()
            self.ui.loc_list = sorted(set(self.FCST_data["Location"]))
            for loc in self.ui.loc_list:
                self.ui.Location_ComboBox.addItem(loc)
            self.ui.Location_ComboBox.setCurrentText(current_loc)
        else:
            df_table = self.FCST_data.copy()
            df_table = df_table[df_table["Region"] == Region_Name]
            # self.ui.Period_ComboBox.clear()
            # self.ui.Period_ComboBox.addItem("所有期間")
            # self.ui.period_list = sorted(set(df_table["Period"]))
            # for period in self.ui.period_list:
            #     self.ui.Period_ComboBox.addItem(period)
            self.ui.Location_ComboBox.clear()
            self.ui.loc_list = sorted(set(df_table["Location"]))
            for loc in self.ui.loc_list:
                self.ui.Location_ComboBox.addItem(loc)

    def Refresh_Button_Clicked(self):
        print("Refreshing Taiwan Weather Data......")
        current_loc = self.ui.Location_ComboBox.currentText()
        self.Chart_Plotly.setHtml("")
        self.ui.Info_Table.clear()
        self.ui.Info_Table.setColumnCount(0)
        self.ui.Info_Table.setRowCount(0)
        self.FCST_data, self.FCST_chart_data = FCST_data_refresh_ETL()
        self.ui.Period_ComboBox.clear()
        self.ui.Period_ComboBox.addItem("所有期間")
        self.ui.period_list = sorted(set(self.FCST_data["Date"]))
        for period in self.ui.period_list:
            self.ui.Period_ComboBox.addItem(period)
        self.ui.Region_ComboBox.clear()
        self.ui.Region_ComboBox.addItem("所有地區 (北/中/南/東/外島)")
        self.ui.region_list = sorted(set(self.FCST_data["Region"]), key=lambda x: Region_Order[x])
        for region in self.ui.region_list:
            self.ui.Region_ComboBox.addItem(region)
        self.ui.Location_ComboBox.clear()
        self.ui.loc_list = sorted(set(self.FCST_data["Location"]))
        for loc in self.ui.loc_list:
            self.ui.Location_ComboBox.addItem(loc)
        self.ui.Location_ComboBox.setCurrentText(current_loc)
        self.ui.Update_Time_Label.setText("Data Last Updated: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        print("Done!")

    def Graph_Show(self, LocationName):
        df = self.FCST_chart_data.copy()
        df = df[df["Location"] == LocationName]
        # print(df)
        fig = go.Figure()
        for col in ["MinT", "MaxT", "AvgT", "AvgDPT", "MinAT", "MaxAT"]:
            fig.add_trace(
                go.Scatter(x=df["StartTime"], y=df[col], name=col, visible=True, mode="lines+markers+text",
                           text=df[col],
                           textposition="top center", marker=dict(size=10, symbol="square"),
                           line=dict(shape='spline')))
        # fig.update_layout(xaxis=dict(tickformat='%Y-%m-%d', range=[df["StartTime"].min() - timedelta(hours=36), None]))
        fig.update_layout(xaxis=dict(dtick='6H'))
        fig.update_layout(
            margin=dict(l=0, r=0, t=10, b=0),
        )
        self.Chart_Plotly.setHtml(fig.to_html(include_plotlyjs='cdn', full_html=True,
                                              default_width="100%", default_height="100%"))
        # print("Graphing")

    def Search_Button_Clicked(self, LocationName, PeriodName):
        # self.Chart_Plotly.setHtml("")
        self.ui.Info_Table.clear()
        self.Graph_Show(LocationName)
        # data_df_pivot[["Period", "Region", "Location", "Weather FCST", "12hr PoP", "T", "AvgT","AT",
        #                "AvgRH", "AvgDPT", "UVI", "MaxWS", "BWS", "WD", "CI", "Weather Desc"]]
        df_table = self.FCST_data.copy()[["Period", "Region", "Location", "Weather FCST", "12hr PoP", "T",
                                          "AvgT", "AT", "AvgRH", "AvgDPT", "UVI", "MaxWS", "BWS", "WD", "CI"]]
        if PeriodName == "所有期間":
            PeriodName = ""
        df_table = df_table[(df_table["Location"] == LocationName)]
        df_table = df_table[(df_table["Period"].str.contains(PeriodName.split(" ")[0], regex=False))]
        df_table_nrows = df_table.shape[0]
        df_table_ncolumns = df_table.shape[1]
        df_table_columns_names = df_table.columns
        self.ui.Info_Table.setColumnCount(df_table_ncolumns)
        self.ui.Info_Table.setRowCount(df_table_nrows)
        self.ui.Info_Table.setHorizontalHeaderLabels(df_table_columns_names)
        for i in range(0, df_table_nrows):
            df_table_row_values_list = list(df_table.iloc[i])
            self.ui.Info_Table.setRowHeight(i, 1)
            for j in range(0, df_table_ncolumns):
                df_table_values_item = str(df_table_row_values_list[j])
                new_item = QTableWidgetItem(df_table_values_item)
                new_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.ui.Info_Table.setItem(i, j, new_item)
                self.ui.Info_Table.horizontalHeader().setSectionResizeMode(j, QHeaderView.ResizeToContents)
        print(LocationName, PeriodName)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    TW_Weather_FCST = AppWindow()
    TW_Weather_FCST.show()
    sys.exit(app.exec_())
    input("WillyF")
