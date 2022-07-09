# MongoDb - Veri Çekme (Select)
from Database7 import myCollection as coll,myDb as db


# result = coll.find_one() # Verilen sorgudan ilk kaydı getirir
# print(result)


# for i in coll.find(): # Birden fazla gelen kayıt için for döngüsü kullanılır
#     print(i)

# # Find parametrelerinin birincisi filtre şartını,ikincisi ise gösterilmek istenen alanı ifade eder
# for i in coll.find({},{"_id":0,"name":1,"price":1}): # Getirilen kayıtta id'nin gizlenmesi için 0,sadece istenen alanların gelmesi için 1 kullanılır
#     print(i)

# for i in coll.find({},{"_id":0}): # Sadece id gizlenir
#     print(i)

# for i in coll.find({},{"_id":0,"name":0}): # Hem id hem de name alanı gizlenir
#     print(i)

# for i in coll.find({},{"name":1}): # id ile birlikte sadece name alanı gösterilir
#     print(i)


