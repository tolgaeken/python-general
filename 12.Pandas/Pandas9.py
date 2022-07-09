# Pandas ile string fonksiyonlarının kullanımı
import pandas as pd

data = pd.read_csv("12. Pandas/datasets/nba.csv")
data.dropna(inplace=True)
# data["Name"] = data["Name"].str.upper() # "Name" kolonundaki string ifadelerin tümünü büyük harfe çevirir
# data["Name"] = data["Name"].str.lower() # "Name" kolonundaki string ifadelerin tümünü küçük harfe çevirir

# data["Index"] = data["Name"].str.find("a") 
# "Index adında yeni bir kolon oluşturur, 
# "Name" kolonu içinde a harfi var ise kaçıncı sırada olduğunu gösterir 
# fakat kayıt içindeki son "a" harfinin index numarasını belirtir, 
# Eğer "Name" kolonunda "a" harfi yok ise -1 değerini döndürür "

# data = data[data.Name.str.contains("Jordan")] # "Name" kolonunda "Jordan" adı geçen kayıtları listeler
# data = data.Team.str.replace(" ","-") # "Team" kolonundaki kayıtlarda " " olan yerleri "-" olarak değiştirir
# data = data.Team.str.replace(" ","-").str.replace("a","e") # Birden fazla değişim yapılması mümkündür

data[["FirstName","LastName"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)
# Split ile veriyi böler (parametre girilmezse varsayılan olarak " " olur)
# "str.len()==2" ile karakter bölündüğünde eğer 2 değer çıkıyor ise o kayıt ikiye bölünebilir anlamına gelir

print(data)