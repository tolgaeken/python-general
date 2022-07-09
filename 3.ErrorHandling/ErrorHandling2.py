# try:
#     x = int(input("X : "))
#     y = int(input("Y : "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Sıfıra bölme hatası!")
# except ValueError:
#     print("Sayısal değer hatası")

# try:
#     x = int(input("X : "))
#     y = int(input("Y : "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e: # Birden fazla hata için aynı except bloğuna işlem yaptırılabilir
#     print("Hatalı bilgi")
#     print(e)

try:
    x = int(input("X : "))
    y = int(input("Y : "))
    print(x/y)
except Exception as ex: # Sadece except de yazılabilir fakat hatanın ne olduğu print ile gösterilemez
    print(f"Hatalı bilgi - {ex}")
else: # Eğer else varsa ya except e ya da else e girer, ikisine birden girmez
    print("Herşey yolunda")
finally: # Finally bloğu hata olsa da olmasa da her şekilde çalıştırılır
    print("Hata yönetimi sonlandırıldı")
