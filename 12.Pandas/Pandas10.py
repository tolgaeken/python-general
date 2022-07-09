# Pandas join ve merge işlemleri
import pandas as pd

# customers = {
#     "CustomerId":[1,2,3,4],
#     "FirstName":["Ahmet","Ali","Hasan","Canan"],
#     "LastName" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     "OrderId":[10,11,12,13],
#     "CustomerId":[1,2,5,7],
#     "OrderDate":["2010-07-04","2010-08-04","2010-07-07","2012-07-04"]
# }

# dfCustomers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# dfOrders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

# result = pd.merge(dfCustomers,dfOrders,how = "inner") # İki tablo için sadece ortak verileri listeler
# result = pd.merge(dfCustomers,dfOrders,how = "left") # "dfCustomers" tablosu için ortak olmayan kayıtları da listeler
# result = pd.merge(dfCustomers,dfOrders,how = "right") # "dfOrders" tablosu için ortak olmayan kayıtları da listeler
# result = pd.merge(dfCustomers,dfOrders,how = "outer") # Her iki tablo için veriler ortak olmasa bile listeler

customersA = {
    "CustomerId":[1,2,3,4],
    "FirstName":["Ahmet","Ali","Hasan","Canan"],
    "LastName" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    "CustomerId":[4,5,6,7],
    "FirstName":["Yağmur","Çınar","Cengiz","Can"],
    "LastName" : ["Bilge","Turan","Yılmaz","Turan"]
}

dfCustomersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
dfCustomersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result = pd.concat([dfCustomersA,dfCustomersB]) # İki tabloyu aşağıya doğru birleştirir
result = pd.concat([dfCustomersA,dfCustomersB],axis=1) # İki tabloyu yan yana birleştirir

print(result)