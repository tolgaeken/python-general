# Pandas dataframe groupby
import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

dataFrame = pd.DataFrame(personeller)
result = dataFrame["Maaş"].sum() # Personellerin toplam maaşını getirir
result = dataFrame.groupby("Departman").groups # Departmana göre gruplayıp index numarasını gelirtir
result = dataFrame.groupby(["Departman","Semt"]).groups # Departman ve Semte göre gruplayıp index numarasını getirir

# for name,group in dataFrame.groupby("Semt"): # Tablo halinde gruplama yapar
#     print(name)
#     print(group)

# for name,group in dataFrame.groupby("Departman"):
#     print(name)
#     print(group)

result = dataFrame.groupby("Semt").get_group("Kadıköy") # Kadıköyde oturanları semte göre gruplar
result = dataFrame.groupby("Departman").get_group("Muhasebe")
result = dataFrame.groupby("Departman").sum() # "Departman" kolonundaki verilerin toplamını alır
result = dataFrame.groupby("Departman").mean() # "Departman" kolonundaki verilerin ortalamasını alır
result = dataFrame.groupby("Departman")["Maaş"].mean() # Departmana göre maaş bilgilerinin ortalamasını getirir
result = dataFrame.groupby("Semt")["Yaş"].mean() # Semte göre yaş ortalamalarını getirir
result = dataFrame.groupby("Semt")["Maaş"].mean()
result = dataFrame.groupby("Semt")["Çalışan"].count() # Her semtte çalışan sayısnı sayar
result = dataFrame.groupby("Departman")["Yaş"].max() # Her departmandaki en yüksek yaşa sahip personelleri getirir
result = dataFrame.groupby("Departman")["Maaş"].min() # Her departmandaki en düşük yaşa sahip personelleri getirir
result = dataFrame.groupby("Departman")["Maaş"].max()["Muhasebe"] # Muhasebe departmanındaki en yüksek alının maaşı gösterir
result = dataFrame.groupby("Departman").agg(np.mean)
result = dataFrame.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"] # Muhasebe departmanındaki bilgileri özet olarak getirir


print(result)