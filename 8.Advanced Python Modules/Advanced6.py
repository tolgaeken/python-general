# pypi.org sitesinden requests modülünü yüklemek gerekir

# # Bu kod ile otomatik yüklenir
# import os
# os.system('cmd /c "py -m pip install requests"')

# Requests, HTML kodlarını görüntülemek için kullanılır
import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos") 
result = json.loads(result.text) # Gelen tip string olduğundan list tipine cast edilmesi gerekiyor

# print(type(result))
# print(result[0]["title"])
# print(result[0])

# for i in result:
#     print(i)
#     # print(i["title"])

for i in result:
    if i["userId"] ==1:
        print(i["title"])

