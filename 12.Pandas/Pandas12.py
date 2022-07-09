# Pandas uygulama - Nba verileri
# Excel viewer eklentisi yüklemek gerekir

import pandas as pd

dataFrame = pd.read_csv("12. Pandas/datasets/nba.csv")

# 1- İlk 10 kaydı getiriniz.
result = dataFrame.head(10)

# 2- Toplam kaç kayıt vardır ?
result = len(dataFrame.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
result = dataFrame["Salary"].mean()

# 4- En yüksek maaşı ne kadardır ?
result = dataFrame["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?
result = dataFrame[dataFrame["Salary"]==dataFrame["Salary"].max()]["Name"].iloc[0]
# result = dataFrame.query("Salary == Salary.max()")["Name"].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = dataFrame[(dataFrame["Age"]>=20) & (dataFrame["Age"]<=25)][["Name","Team","Age"]].sort_values("Age",ascending=False)
# result = dataFrame.query("25 >= Age >= 20")[["Name","Team","Age"]].sort_values("Age",ascending=False)

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = dataFrame[dataFrame["Name"]=="John Holland"]["Team"].iloc[0]
# result = dataFrame.query("Name == 'John Holland'")["Team"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = dataFrame.groupby("Team").mean()["Salary"]
result = round(result,2)

# 9- Kaç farklı takım mevcut ?
result = len(dataFrame.groupby("Team"))
result = dataFrame["Team"].nunique()

# 10- Her takımda kaç oyuncu oynamaktadır ?
result = dataFrame["Team"].value_counts(ascending=True)

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
dataFrame.dropna(inplace=True) # NaN değerlerin silinmesi gerekir Inplace ile orjinal verideki boş değerler silinsin
# result = dataFrame[dataFrame["Name"].str.contains("and")]
def strFind(name):
    if "and" in name.lower():
        return True
    return False

result = dataFrame[dataFrame["Name"].apply(strFind)]

print(result)