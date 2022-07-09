def yetkiSorgula(page):
    def inner(role):
        if role == "Admin":
            return f"{role} rolü {page} sayfasına ulaşabilir"
        else:
            return f"{role} rolü {page} sayfasına ulaşamaz"
        
    return inner

user1 = yetkiSorgula("ProductEdit")
print(user1("Admin"))

user2 = yetkiSorgula("ProductEdit")
print(user2("User"))