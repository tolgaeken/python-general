# GitHub Rest API
import json
import requests

class Github:
    def __init__(self):
        self.apiUrl = "https://api.github.com"
        self.token = "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"

    def getUser(self,userName):
        response = requests.get(self.apiUrl + "/users/" + userName)
        return response.json()
    
    def getRepositories(self,userName):
        response = requests.get(self.apiUrl + "/users/" + userName + "/repos")
        return response.json()
    
    def createRepository(self,name):
        response = requests.post(self.apiUrl + "/user/repos?access_token=" + self.token,json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
    
github = Github()


while True:
    secim = int(input("1 - Kullanıcı Ara\n2 - Reapository getir\n3 - Repository Oluştur\n4 - Çıkış\n"))
    if secim == 4:
        break


    match secim:
        case 1:
            userName = input("Kullanıcı adı giriniz\n")
            result = github.getUser(userName)
            print(f"Adı : {result['name']}\nPublic Repository Sayısı : {result['public_repos']}\nTakipçileri : {result['followers']}")
        case 2:
            userName = input("Kullanıcı adı giriniz\n")
            result = github.getRepositories(userName)
            for repo in result:
                print(repo["name"])
        case 3:
            name = input("Yeni Repository adı giriniz\n")
            result = github.createRepository(name)
            print(result)
        case _:
            print("Hatalı giriş")