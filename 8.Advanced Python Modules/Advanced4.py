# Json Modülü
import json

personString = '{"name":"Ali","languages":["python","c#"]}' 
personDictionary = {"name":"Ali","languages":["Python","C#"]}

# result = json.loads(personString) # Json yapısını dictionary türüne çevirir
# print(type(result))

# with open("8. Advanced Python Modules/Advanced4.json") as f:
#     data = json.load(f)
#     print(data)
#     print(data["languages"][0])


# result = json.dumps(personDictionary) # dictionary türünü json yapısına çevirir
# print(type(result))

# with open("8. Advanced Python Modules/Advanced4.json","w") as f: # Verilen json dosyasına kaydetme
#     json.dump(personDictionary,f)

# personDictionary = json.loads(personString)
# result = json.dumps(personDictionary,indent= 4,sort_keys=True) # Json dosyasını düzenli şekilde yazdırır
# print(result)