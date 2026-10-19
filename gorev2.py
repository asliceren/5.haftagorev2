
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

def manuel_calc_hist(kanal_matrisi):
    hist = np.zeros(256, dtype=int)
    yukseklik, genislik = kanal_matrisi.shape
    
    for y in range(yukseklik):
        for x in range(genislik):
            piksel_degeri = kanal_matrisi[y, x]
            hist[piksel_degeri] += 1
            
    return hist

image = cv2.imread("renklifoto.jpg")
if image is None:
    print("Hata: 'renklifoto.jpg' bulunamadi!")
    exit()

b_kanali, g_kanali, r_kanali = cv2.split(image)

hist_b = manuel_calc_hist(b_kanali)
hist_g = manuel_calc_hist(g_kanali)
hist_r = manuel_calc_hist(r_kanali)

plt.figure(figsize=(9, 5))
plt.title("Manuel calcHist - BGR Histogrami")
plt.xlabel("Piksel Degeri (0 - 255)")
plt.ylabel("Piksel Sayisi")

plt.plot(hist_b, color="blue", label="Mavi Kanal (Manuel)", linewidth=1.5)
plt.plot(hist_g, color="green", label="Yesil Kanal (Manuel)", linewidth=1.5)
plt.plot(hist_r, color="red", label="Kirmizi Kanal (Manuel)", linewidth=1.5)

plt.xlim([0, 256])
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("manuel_histogram.png")
plt.show()
