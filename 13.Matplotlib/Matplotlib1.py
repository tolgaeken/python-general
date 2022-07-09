# Matplotlib ile veriler üzerinde grafik oluşturulur
# https://matplotlib.org/
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# Matplotlib kullanmak için kütüphaneyi yüklemek gerekir
# Aşağıdaki kod ile otomatik yüklenir
# import os
# os.system('cmd /c "py -m pip install matplotlib')

import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]
y = [1,4,9,16]
# plt.plot(x,y,color="red",linewidth="5") # (x ekseni,y ekseni) color çizgi rengini,linewidth ise çizgi kalınlığını belirler
plt.plot(x,y,"o--g") # -g parametresi düz yeşili, --g parametresi kesik çizgili yeşil,o--g ise değerlere işaret koyarak kesik çizgili yeşil yapar
# plt.plot(x,y,"o--r")
plt.axis([0,6,0,20]) # [x çizgisinin başlangıc değeri,x çizgisinin bitiş değeri,y çizgisinin başlangıç değeri,y çizgisinin bitiş değeri]
plt.title("Grafik Başlığı") # Grafik başlığını belirler
plt.xlabel("X Ekseni") # X Ekseninin adını belirler
plt.ylabel("Y Ekseni") # Y Ekseninin adını belirler
plt.grid() # Kılauz çizgilerini gösterir
plt.show() # Grafiği gösterir
"""

"""
x = np.linspace(0,2,100)
plt.plot(x,x,label = "linear",color = "red")
plt.plot(x,x**2,label = "quadratic",color = "yellow")
plt.plot(x,x**3,label = "cubic",color = "green")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.legend() # Label açıklamalarını grafik üzerinde gösterir
plt.show()
"""

# y = x² parabolü³
# x = np.linspace(-100,100,1000)
# plt.plot(x,x**2,"--g")
# plt.axis([-20,20,0,300])
# plt.xlabel("X Ekseni")
# plt.ylabel("Y Ekseni")
# plt.show()

# # y = x³ parabolü
# x = np.linspace(-100,100,1000)
# plt.plot(x,x**3,"--g")
# plt.axis([-20,20,-300,300])
# plt.xlabel("X Ekseni")
# plt.ylabel("Y Ekseni")
# plt.show()

# y = 4x-(x³/3) eğrisi
# x = np.linspace(-10,10,100)
# plt.plot(x,(4*x)-(x**3/3),"--g")
# plt.axis([-5,5,-6,6])
# plt.xlabel("X Ekseni")
# plt.ylabel("Y Ekseni")
# plt.grid()
# plt.show()

"""
x = np.linspace(0,2,100)
figure,axis = plt.subplots(3) # Birden fazla tablo oluşturmak için kullanılır
axis[0].plot(x,x,color = "red")
axis[0].set_title("linear") # Grafiğe başlık ekler
axis[1].plot(x,x**2,color = "green")
axis[1].set_title("quadratic")
axis[2].plot(x,x**3,color = "blue")
axis[2].set_title("cubic")
plt.tight_layout() # Grafikleri başlıkları ile hizalar
plt.show()
"""

"""
x = np.linspace(0,2,100)
figure,axis = plt.subplots(2,2) # Grafikleri bölümlendirmek için 2 parametre kullanılır
figure.suptitle("Grafik Başlığı")

axis[0,0].plot(x,x,color = "red") # 1. satırın 1. sütununu belirler
axis[0,1].plot(x,x**2,color = "green")
axis[1,0].plot(x,x**3,color = "blue")
axis[1,1].plot(x,x**4,color = "black")
plt.show()
"""

import pandas as pd
dataFrame = pd.read_csv("13. Matplotlib/nba.csv")
dataFrame = dataFrame.drop(["Number"],axis = 1).groupby("Team").mean() # nba takımlarının istatistiklerini listeler
dataFrame.plot(subplots = True) # subplots = True ile her grafikte 1 veri listesi olacak şekilde ayarlanır
plt.legend()
plt.show()
