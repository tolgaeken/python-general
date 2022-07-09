# Pandas Uygulama Imdb veri analizi
import pandas as pd

dataFrame = pd.read_csv("12. Pandas/datasets/imdb.csv")

# 1- Dosyada hakkındaki bilgiler.
# result = dataFrame.columns
# result = dataFrame.info
# result = dataFrame.info()

# 2- ilk 5 kaydı gösterin
result = dataFrame.head()

# 3- ilk 10 kaydı gösterin
result = dataFrame.head(10)

# 4- Son 5 kaydı gösterin
result = dataFrame.tail()

# 5- Son 10 kaydı gösterin
result = dataFrame.tail(10)

# 6- Sadece Movie_Title kolonunu alın.
result = dataFrame["Movie_Title"]

# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
result = dataFrame["Movie_Title"].head()

# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.
result = dataFrame[["Movie_Title","Rating"]].head()

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
result = dataFrame[["Movie_Title","Rating"]].tail(7)

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın.
result = dataFrame[5:][["Movie_Title","Rating"]].head()
result = dataFrame[5:10][["Movie_Title","Rating"]]

# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 
#     ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
result = dataFrame[dataFrame["Rating"] > 8.0][["Movie_Title","Rating"]].head(50)


# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
result = dataFrame[(dataFrame["YR_Released"]>=2014) & (dataFrame["YR_Released"]<=2015)][["Movie_Title","Rating","YR_Released"]]
result = dataFrame.query("YR_Released >= 2014 & YR_Released <= 2015")[["Movie_Title","Rating","YR_Released"]]
result = dataFrame.query("2015 >= YR_Released >= 2014")[["Movie_Title","Rating","YR_Released"]]

# 13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
#     8 ile 9 arasında olan filmleri listeleyiniz.  
result = dataFrame[(dataFrame["Num_Reviews"] >= 100000) | ((dataFrame["Rating"] >= 8) & (dataFrame["Rating"] <= 9))][["Movie_Title","Num_Reviews","Rating"]]
result = dataFrame.query("Num_Reviews > 100000 | 9.0 >= Rating >= 8.0")[["Movie_Title","Num_Reviews","Rating"]]


print(result)