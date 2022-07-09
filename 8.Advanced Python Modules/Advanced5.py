import json
import os

class User:
    def __init__(self,userName,password,eMail):
        self.userName = userName
        self.password = password
        self.eMail = eMail

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists("8. Advanced Python Modules/Advanced5.json"):
            with open("8. Advanced Python Modules/Advanced5.json") as f:
                users = json.load(f)
                for user in users:
                    user = json.loads(user)
                    newUser = User(userName = user["userName"],password= user["password"],eMail=user["eMail"])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanıcı Oluşturuldu")

    def login(self,userName,password):
        for user in self.users:
            if user.userName == userName and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Giriş Yapıldı")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış Yapıldı")

    def identity(self):
        if self.isLoggedIn:
            print(f"Kullanıcı Adı \t{self.currentUser.userName}")
        else:
            print("Giriş Yapılmadı")
    def saveToFile(self):
        liste = []
        # json dosyasını göndermek için objenin dict olması gerekir fakat fonksiyonda list olarak kaydedildiği için
        # verileri tekrar alıp for döngüsü ile alıp dict tipine cast etmek gerekir
        for user in self.users:
            liste.append(json.dumps(user.__dict__))

        with open("8. Advanced Python Modules/Advanced5.json","w",encoding="utf-8") as f:
            json.dump(liste,f)


repository = UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim = int(input("1 - Kayıt\n2 - Giriş Yap\n3 - Çıkış Yap\n4 - Kimlik Bilgisi\n5 - Çıkış\n"))

    match secim:
        case 1:
            userName = input("Kullanıcı adı giriniz\n")
            password = input("Parola giriniz\n")
            eMail = input("E - Mail giriniz\n")

            user = User(userName = userName,password=password,eMail=eMail)
            repository.register(user)

            print(repository.users)


        case 2:
            if repository.isLoggedIn:
                print("Mevcut bir giriş zaten yapılmıştır")
            else:
                userName = input("Kullanıcı Adı Giriniz\n")
                password = input("Parola Giriniz\n")
                repository.login(userName,password)
        case 3:
            repository.logout()
        case 4:
            repository.identity()
        case 5:
            break
        case _:
            print("Hatalı giriş")
