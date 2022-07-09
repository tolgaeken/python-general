# MongoDb - Veri Ekleme
from Database7 import myCollection as coll ,myDb as db


# print(db.list_collection_names())

# product = {"name":"Samsung S5","price":2000}
# result = coll.insert_one(product) # Tek kayıt ekler
# print(result)
# print(type(result))
# print(result.inserted_id) # Eklenen kaydın id sini gösterir


productList = [
    # {"_id":"123","name":"Samsung S6","price":3000}, # İsteğe bağlı olarak elle id verilebilir. Fakat elle girilen id ler eşsiz olmalıdır
    {"name":"Samsung S6","price":3000},
    {"name":"Samsung S7","price":4000},
    {"name":"Samsung S8","price":5000},
    {"name":"Samsung S9","price":6000},
    ]
# result = coll.insert_many(productList) # Birden fazla kayıt ekler
# print(result.inserted_ids) # Eklenen kayıtların idlerini gösterir


productList2 = [
    {"name":"Samsung S10","price":7000,"description":"İyi telefon"}, # Alternatif bilgiler eklenebilir
    {"name":"Samsung S11","price":8000,"categories":["telefon","elektronik"]} # Alternatif bilgiler eklenebilir
]
# result = coll.insert_many(productList2)
# print(result.inserted_ids)