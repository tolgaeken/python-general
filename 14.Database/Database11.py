# MongoDb - Sort
from Database7 import myCollection as coll,myDb as db

# result = coll.find().sort("name") # name alanına göre artan şekilde sıralar
# result = coll.find().sort("name",1) # aynı şekilde name alanına göre artan şekilde sıralar, 1 yazılması zorunlu değildir
# result = coll.find().sort("name",-1) # name alanına göre azalan şekilde sıralar
# result = coll.find().sort("price",-1) # price alanına göre azalan şekilde sıralar
result = coll.find().sort([("name",1),("price",-1)]) # önce name alanına göre artan şekilde sıralar, eğer aynı değerler varsa price alanına göre azalan şekilde sıralar
for i in result:
    print(i)