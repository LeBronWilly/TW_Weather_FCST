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





from UI_V01 import *
import pandas as pd
import urllib
import json
# import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.max_rows', 1000)




class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TW_Weather_FCST()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon(".png"))
        self.setup_control()
        self.show()

    def setup_control(self):


        pass




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    IG_Photo_Downloader = AppWindow()
    IG_Photo_Downloader.show()
    sys.exit(app.exec_())



