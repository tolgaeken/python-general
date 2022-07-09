# MongoDb - Update
from Database7 import myCollection as coll,myDb as db

# # İlk parametre güncellenmek istenen kayıtların şartını, ikinci parametre ise yeni değer belirtir
# # Güncellenmek istenen kayıttan 2 tane varsa update_one ile ilk bulunan güncellenir
# coll.update_one(
#     {"name":"Samsung S5"},
#     {"$set":{
#         "name":"iPhone 5",
#     }}
#     )

# # Tek kayıt üserinde birden fazla değişiklik yapılabilir
# coll.update_one(
#     {"name":"Samsung S6"},
#     {"$set":{
#         "name":"iPhone 6",
#         "price":6500
#     }}
#     )

# # Birden fazla aynı kayıt var ve hepsinin üzerinde güncelleme yapılması gerekiyorsa update_many kullanılır
# coll.update_many(
#     {"name":"Samsung S7"},
#     {"$set":{
#         "name":"iPhone 7",
#         "price":7300
#     }}
#     )

# # Alternatif
# query={"name":"Samsung S7"}
# newValues= {"$set":{
#                 "name":"iPhone 7",
#                 "price":7300
#             }}
# result = coll.update_many(query,newValues)
# print(f"{result.modified_count} adet kayıt güncellendi") # Güncellene kayıtların sayısını belirtir

for i in coll.find():
    print(i)