# Pandas Data Frame

import pandas as pd

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1,oranges = s2)
# dataFrame = pd.DataFrame(data)
# print(dataFrame)


# df = pd.DataFrame()

# df = pd.DataFrame([1,2,3,4])

# data = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
# df = pd.DataFrame(data,[1,2,3,4],["Name","Grade"],dtype=float)
# df = pd.DataFrame(data,columns=["Name","Grade"],index= [1,2,3,4])

# dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}
# df = pd.DataFrame(dict,index=["212","232","233","321"])

dictList = [
    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"Yağmur","Grade":70},
    {"Name":"Çınar","Grade":80}
    ]

df = pd.DataFrame(dictList,index=["212","232","233","321"]) # Sözlük ile oluşturulan listenin index numarası belitirilerek dataframe oluşturulur

print(df)