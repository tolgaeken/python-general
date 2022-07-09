# Pandas farklı dosya tiplerinden veri okuma
import pandas as pd
import sqlite3

# "12. Pandas/datasets"

# dataFrame = pd.read_csv("12. Pandas/datasets/sample.csv") # csv formatındaki dosyaları okur
# dataFrame = pd.read_json("12. Pandas/datasets/sample.json",encoding="utf-8") # json formatındaki dosyaları okur

# Excel dosyalarını okuyabilmek için openpyxl kütüphanesini yüklemek gerekir
# Aşağıdaki kod ile otomatik yüklenir
# import os
# os.system('cmd /c "py -m pip install openpyxl"')
# dataFrame = pd.read_excel("12. Pandas/datasets/sample.xlsx")

connection = sqlite3.connect("12. Pandas/datasets/sample.db") # sqlite dosyalarına okue
dataFrame = pd.read_sql_query("select * from students",connection) # örnek sql sorgusu

print(dataFrame)