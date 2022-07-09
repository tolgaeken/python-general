# DateTime Modülü Kullanımı

# import datetime
# print(dir(datetime))

from datetime import datetime
from datetime import timedelta
# print(dir(datetime))

simdi = datetime.now() # Şu anki zamanı gösterir
yil = simdi.year # Şu anki yılı gösterir
ay = simdi.month # Şu anki ayı gösterir
dakika = simdi.minute # Şu anki dakikayı gösterir

bugun = datetime.today() # Bugünü gösterir
result = datetime.ctime(simdi) # Casting işlemi yapar
result = datetime.strftime(simdi,"%Y") # String e cast işlemi yapar ve "%Y" ile yıl bilgisi için formatlar
result = datetime.strftime(simdi,"%X") # Saat bilgisi
result = datetime.strftime(simdi,"%d") # Gün bilgisi
result = datetime.strftime(simdi,"%A") # Gün bilgisi (yazı ile)
result = datetime.strftime(simdi,"%B") # Ay Bilgisi
result = datetime.strftime(simdi,"%Y %B %A")

print(result)

t = "21 April 2019 hour 10:12:30"

# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

dt=datetime.strptime(t,"%d %B %Y hour %H:%M:%S") # String olan tarih ifadesini DateTime tipine cast eder
dtResult = dt.year # Cast edilen string için yıl bilgisini alma

print(dt)
print(type(dt))

birthDate = datetime(1990,5,9)
birthDate = datetime(1990,5,9,12,13,14)
print(birthDate)

result = datetime.timestamp(birthDate) # Tarih objesi saniye cinsinden gösterilir
result = datetime.fromtimestamp(result) # Saniyeyi tarih cinsinden gösterir
# result = datetime.fromtimestamp(0)

result = simdi - birthDate # timedelta objesi
# result = result.days # aradaki farkı gün cinsinden gösterir
# result = result.seconds # aradaki farkı saniye cinsinden gösterir
print(result)


result = simdi + timedelta(days=10) # Bugünün üzerine 10 gün ekler
result = simdi + timedelta(days=720,minutes=10)
result = simdi - timedelta(days=15)
print(result)