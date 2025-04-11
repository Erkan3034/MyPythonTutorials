import pandas as pd
import numpy as np

# Veri seti oluşturma (numpy ile rastgele veri)
np.random.seed(42)
veri = {
    "Gün": [f"Gün {i}" for i in range(1, 11)],
    "Sıcaklık": np.random.randint(15, 35, 10),
    "Nem": np.random.randint(30, 80, 10),
    "Yağış": np.random.choice(["Evet", "Hayır"], size=10, p=[0.3, 0.7])
}

# DataFrame oluşturma (pandas)
df = pd.DataFrame(veri)

# İstatistiksel bilgiler (pandas ile)
print("Veri Seti:\n", df)
print("\nSıcaklık Ortalaması:", df["Sıcaklık"].mean())
print("Nem Ortalaması:", df["Nem"].mean())
print("Yağış Olan Gün Sayısı:", (df["Yağış"] == "Evet").sum())

# Sıcaklık ve Nem sütunlarına numpy işlemleri uygulama
df["Sıcaklık (C)"] = np.round((df["Sıcaklık"] - 32) * 5/9, 2)  # Fahrenheit'tan Celsius'a dönüşüm
df["Nem (%)"] = np.round(df["Nem"] / 100, 2)  # Nem oranını normalize etme

# Günlere göre sıralama ve yüksek sıcaklık/nem günlerini filtreleme
sıcak_günler = df[df["Sıcaklık"] > 30]
# This code filters a DataFrame to select rows where the "Nem" (humidity) column has values greater than 70, indicating significant humidity days.
nemli_günler = df[df["Nem"] > 70]

# Güncellenmiş veri setini yazdırma
print("\nGüncellenmiş Veri Seti:\n", df)
print("\nSıcak Günler:\n", sıcak_günler)
print("\nNemli Günler:\n", nemli_günler)

# Görselleştirme (pandas ile hızlı çizim)
import matplotlib.pyplot as plt

df.plot(x="Gün", y="Sıcaklık", kind="line", marker="o", title="Günlük Sıcaklık", figsize=(8, 5))
plt.xlabel("Günler")
plt.ylabel("Sıcaklık (°F)")
plt.grid()
plt.show()

df.plot(x="Gün", y="Nem", kind="bar", title="Günlük Nem", figsize=(8, 5), color="orange")
plt.xlabel("Günler")
plt.ylabel("Nem (%)")
plt.grid(axis="y")
plt.show()
