# Pandas uygulama - youtube video istatistik veri analizi
import pandas as pd

dataFrame = pd.read_csv("12. Pandas/datasets/youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.
result = dataFrame.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = dataFrame[5:10].head(5)

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = dataFrame.columns
result = len(dataFrame.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
dataFrame.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
result = dataFrame

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = dataFrame["likes"].mean()
result = dataFrame["dislikes"].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = dataFrame.head(50)[["title","likes","dislikes"]]

# 7- En çok görüntülenen video hangisidir ?
result = dataFrame[dataFrame["views"] == dataFrame["views"].max()][["title","views"]]
# result = dataFrame[dataFrame["views"] == dataFrame["views"].max()]["title"].iloc[0]
# result = dataFrame.query("views == views.max()").max()[["title","views"]] # transpoze işlemi araştırılacak

# 8- En düşük görüntülenen video hangisidir?
result = dataFrame[dataFrame["views"] == dataFrame["views"].min()][["title","views"]]
# result = dataFrame[dataFrame["views"] == dataFrame["views"].min()]["title"].iloc[0]
# result = dataFrame.query("views == views.min()").max()[["title","views"]] # transpoze işlemi araştırılacak

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = dataFrame.sort_values("views",ascending=False).head(10)[["title","views"]]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = dataFrame.groupby("category_id").mean().sort_values("likes")["likes"]
result = round(result,2)

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = dataFrame.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

# 12- Her kategoride kaç video vardır ?
result = dataFrame["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
dataFrame["title_len"] = dataFrame["title"].apply(len)
result = dataFrame

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# def tagCount(tag):
#     return len(tag.split("|"))
# dataFrame["tag_count"] = dataFrame["tags"].apply(tagCount)

dataFrame["tag_count"] = dataFrame["tags"].apply(lambda x : len(x.split("|")))
result = dataFrame[["title","tag_count"]]

# print(result)

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)


def likeDislikeOranHesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList)) # zip ile her videonun like ve dislike değerleri tuple olarak gelir

    oranListesi = []

    for like,dislike in liste:
        if (like+dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

dataFrame["like_rate"] = likeDislikeOranHesapla(dataFrame)

print(dataFrame.sort_values("like_rate",ascending=False)[["title","likes","dislikes","like_rate"]])