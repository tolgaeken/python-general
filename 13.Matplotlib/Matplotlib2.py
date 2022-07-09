# Matplotlib ile figure oluşturma

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

"""
figure = plt.figure()
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) # (Sol,alt,sağ,üst) kısımlardan yüzdesel olarak boşluk bırakılan değerleri belirtir
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X Ekseni")
axes_cube.set_ylabel("Y Ekseni")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15,0.6,0.25,0.25]) # Sol üst boyut
axes_square.plot(x,z,"r")
axes_square.set_xlabel("X Ekseni")
axes_square.set_ylabel("Y Ekseni")
axes_square.set_title("Square")
plt.show()
"""


"""
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=3) # (Sağ üst,sol üst,sol alt,sağ alt) köşeye legend koyar
plt.show()
"""


"""
figure,(axes1,axes2) = plt.subplots(nrows =2,ncols =1,figsize = (8,8)) # satır, sütun sayısı ve büyüklük değeri girilebilir
axes1.plot(x,y)
axes1.set_title("Cube")
axes2.plot(x,z)
axes2.set_title("Square")
# figure.tight_layout()
plt.tight_layout()
figure.savefig("13. Matplotlib/figure1.png")
figure.savefig("13. Matplotlib/figure1.pdf")
plt.show()
"""