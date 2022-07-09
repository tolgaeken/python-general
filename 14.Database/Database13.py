# MongoDb - Delete
from Database7 import myCollection as coll,myDb as db

def listele():
    for i in coll.find():
        print(i)
    print("*"*50)

listele()



# # Silmek istenen kayıttan 2 tane varsa delete_one ile ilk bulunan silinir
# coll.delete_one({"name":"Samsung S8"})
# listele()

# # Birden fazla aynı kayıt var ve hepsinin üzerinde silme işlemi yapılması gerekiyorsa delete_many kullanılır
# coll.delete_many({"name": {"$regex": "^iP"}})
# listele()


# result = coll.delete_many({}) # Bütün kayıtları siler
# print(f"{result.deleted_count}") # Silinen kayıt sayısını gösterir