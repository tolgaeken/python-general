# Hata Nesnesi Oluşturma (Raising an Exception)

# x = 10

# if x > 5:
#     raise Exception("x 5 den büyük değer alamaz")

def checkPassword(password):
    import re # regular expression
    if len(password) < 7:
        raise Exception("Parola en az 7 karakter olmalıdır")
    elif not re.search("[a-z]",password):
        raise Exception("Parola küçük harf içermelidir")
    elif not re.search("[A-Z]",password):
        raise Exception("Parola büyük harf içermelidir")
    elif not re.search("[0-9]",password):
        raise Exception("Parola rakam içermelidir")
    elif not re.search("[_@$]",password):
        raise Exception("Parola alfanümerik karakter içermelidir")
    elif re.search("\s",password):
        raise Exception("Parola boşluk içermemelidir")
    else:
        print("Parola geçerlidir")

pw = "1234567aA@"

try:
    checkPassword(pw)
except Exception as ex:
    print(f"Hata - {ex}")
finally:
    print("Doğrulama tamamlandı")