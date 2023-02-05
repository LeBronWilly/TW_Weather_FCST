# -*- coding: utf-8 -*-
"""
Created on 01/14, 2023 (Happy Lunar New Year!)
@author: Willy Fang (WillyF)

"""

# https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
# https://opendata.cwb.gov.tw/dataset/forecast/F-C0032-001
# https://opendata.cwb.gov.tw/dist/opendata-swagger.html?urls.primaryName=openAPI#/%E9%A0%90%E5%A0%B1/get_v1_rest_datastore_F_C0032_001
# https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
# https://stackoverflow.com/questions/31306741/unmelt-pandas-dataframe
# https://medium.com/%E6%95%B8%E6%93%9A%E4%B8%8D%E6%AD%A2-not-only-data/pandas-%E5%BF%AB%E9%80%9F%E7%9E%AD%E8%A7%A3-pivot-table-%E8%88%87%E6%87%89%E7%94%A8-21e4c37b9216
# https://www.geeksforgeeks.org/python-pandas-series-str-cat-to-concatenate-string/
# https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html
# https://stackoverflow.com/questions/12646326/calling-a-class-function-inside-of-init


from UI_V01 import *
import pandas as pd
import urllib.request
import json
import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.max_rows', 1000)


def FCST_data_refresh_ETL():
    data_source = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-3D27458E-8F30-4BDF-9589-6DD4A337AA74&format=JSON&locationName=&elementName=&sort=time"
    json_url = urllib.request.urlopen(data_source)
    data = json.loads(json_url.read())
    data_df = pd.json_normalize(data["records"],
                                record_path=["location", "weatherElement", "time"],
                                meta=[['location', "locationName"],
                                      ['location', "weatherElement", "elementName"],
                                      'datasetDescription',
                                      ],
                                )
    data_df.columns = [x.split(".")[-1] for x in data_df.columns]
    data_df["parameterUnit"].replace("百分比", "%", inplace=True)
    data_df["parameterUnit"].replace("C", "°C", inplace=True)
    data_df["parameterUnit"].replace(np.nan, "", inplace=True)
    data_df["elementName"].replace("Wx", "Weather Forcast", inplace=True)
    data_df["elementName"].replace("PoP", "Probability of Precipitation", inplace=True)
    data_df["elementName"].replace("MinT", "Min Temperature", inplace=True)
    data_df["elementName"].replace("MaxT", "Max Temperature", inplace=True)
    data_df["elementName"].replace("CI", "Comfort Index", inplace=True)
    data_df["Parameter"] = data_df["parameterName"] + data_df["parameterUnit"]
    data_df["startTime"] = data_df["startTime"].apply(lambda x: x.replace("-", "/")[:-3])
    data_df["endTime"] = data_df["endTime"].apply(lambda x: x.replace("-", "/")[:-3])
    data_df_pivot = pd.pivot_table(data_df,
                                   index=["startTime", "endTime", 'locationName'],
                                   columns=["elementName"],
                                   values=["Parameter"],
                                   aggfunc=lambda x: x).reset_index()
    data_df_pivot.columns = ["startTime", "endTime", "locationName", "Comfort Index",
                             "Max Temperature", "Min Temperature", "Probability of Precipitation", "Weather Forcast"]
    data_df_pivot = data_df_pivot.sort_values(by=["locationName", "startTime", "endTime"]).reset_index(drop=True)
    data_df_pivot["Period"] = data_df_pivot["startTime"].str.cat(data_df_pivot["endTime"], sep=" ~ ")
    data_df_pivot["Temperature"] = data_df_pivot["Max Temperature"].str.cat(data_df_pivot["Min Temperature"], sep=" ~ ")
    data_df_pivot = data_df_pivot.rename(
        columns={"locationName": "Location", "Probability of Precipitation": "PoP",
                 "Weather Forcast": "Weather FCST"},
        errors="raise")
    return data_df_pivot


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TW_Weather_FCST()
        self.ui.setupUi(self)
        self.FCST_data = None
        # self.setWindowIcon(QIcon(".png"))
        self.setup_control()
        self.show()

    def setup_control(self):
        self.FCST_data = FCST_data_refresh_ETL()
        self.ui.Refresh_Button.clicked.connect(self.Refresh_Button_Clicked)
        self.ui.Search_Button.clicked.connect(self.Search_Button_Clicked)
        self.ui.Location_ComboBox.clear()
        self.ui.Location_ComboBox.addItem("Choose City/County")
        self.ui.loc_list = sorted(set(self.FCST_data["Location"]))
        for loc in self.ui.loc_list:
            self.ui.Location_ComboBox.addItem(loc)
        self.ui.Period_ComboBox.clear()
        self.ui.Period_ComboBox.addItem("Choose Time Period")
        self.ui.period_list = sorted(set(self.FCST_data["Period"]))
        for period in self.ui.period_list:
            self.ui.Period_ComboBox.addItem(period)


    def Refresh_Button_Clicked(self):
        self.ui.Info_Table.clear()
        self.FCST_data = FCST_data_refresh_ETL()
        self.ui.Location_ComboBox.clear()
        self.ui.Location_ComboBox.addItem("Choose City/County")
        self.ui.loc_list = sorted(set(self.FCST_data["Location"]))
        for loc in self.ui.loc_list:
            self.ui.Location_ComboBox.addItem(loc)
        self.ui.Period_ComboBox.clear()
        self.ui.Period_ComboBox.addItem("Choose Time Period")
        self.ui.Period_ComboBox.addItem("All")
        self.ui.period_list = sorted(set(self.FCST_data["Period"]))
        for period in self.ui.period_list:
            self.ui.Period_ComboBox.addItem(period)

    def Search_Button_Clicked(self):
        self.ui.Info_Table.clear()
        df_table = self.FCST_data.copy()[["Period", "Location", "Weather FCST", "Temperature",
                                          "PoP", "Comfort Index"]]
        df_table = df_table.loc[df_table["Location"] == self.ui.Location_ComboBox.currentText()]
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






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    TW_Weather_FCST = AppWindow()
    TW_Weather_FCST.show()
    sys.exit(app.exec_())



