# MongoDb - Query
from Database7 import myCollection as coll,myDb as db
from bson.objectid import ObjectId

# filter = {"name":"Samsung S5"}
# result = coll.find(filter)
# for i in result:
#     print(i)

# result = coll.find_one(filter)
# print(result)

# result = coll.find_one({"_id":ObjectId("61e1f2b97c3bfb3080b9f56c")}) # id ile filtreleme yapmak için ObjectId import edilip cast edilir
# print(result)

# result = coll.find({
#     "name":{
#         "$in" : ["Samsung S5","Samsung S6"] # name alanında sadece belirli değerler belirtilir
#     }
# })

# result = coll.find({
#     "price": {
#         "$gt":5000 # price alanında 5000 den büyük değerleri getirir
#     }
# })
    
# result = coll.find({
#     "price": {
#         "$gte":5000 # price alanında 5000 ve 5000 den büyük değerleri getirir
#     }
# })

# result = coll.find({
#     "price": {
#         "$eq":5000 # price alanı sadece 5000 olanları getirir
#     }
# })
 
# result = coll.find({
#     "price": {
#         "$lt":5000 # price alanında 5000 den küçük değerleri getirir
#     }
# })
 
# result = coll.find({
#     "price": {
#         "$lte":5000 # price alanında 5000 ve 5000 den küçük değerleri getirir
#     }
# })

result = coll.find({
    "name": {"$regex": "^S"} # name alanında S ile başlayan kayıtları getirir (Regular Expression)
})
for i in result:
    print(i)

# https://docs.mongodb.com/manual/reference/operator/
# https://docs.mongodb.com/manual/reference/operator/query/

