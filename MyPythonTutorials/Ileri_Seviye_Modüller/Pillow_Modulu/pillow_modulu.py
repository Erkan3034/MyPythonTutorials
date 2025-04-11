from PIL import Image, ImageFilter

# 1. Görseli açma
image = Image.open("kuş.jpg")  # "kus.jpg" isimli görseli açıyoruz.

# 2. Görselin boyutlarını öğrenme
print("Orijinal Boyutlar:", image.size)  # Görselin boyutlarını yazdırıyoruz


# 3. Görseli yeniden boyutlandırma
resized_image = image.resize((800, 600))  # Görseli 800x600 boyutlarında yeniden boyutlandırıyoruz.
resized_image.show()  # Yeniden boyutlandırılmış görseli gösteriyoruz.
resized_image.save("kus_resized.jpg")  # Görseli 'resized' olarak kaydediyoruz.

a = image.filter(ImageFilter.GaussianBlur(10))
a.show()
a.save("kus_blurred.jpg")

# 4. Görseli kırpma
cropped_image = image.crop((100, 100, 400, 400))  # (sol, üst, sağ, alt) şeklinde koordinatlar vererek kırpıyoruz.
cropped_image.show()  # Kırpılmış görseli gösteriyoruz.
cropped_image.save("kus_cropped.jpg")  # Görseli 'cropped' olarak kaydediyoruz.

# 5. Görseli gri tonlara dönüştürme
gray_image = image.convert("L")  # Görseli gri tonlara dönüştürüyoruz.
gray_image.show()  # Gri tonlardaki görseli gösteriyoruz.
gray_image.save("kus_grayscale.jpg")  # Görseli 'grayscale' olarak kaydediyoruz.
"""
# 6. Görseli döndürme
rotated_image = image.rotate(90)  # Görseli 90 derece döndürüyoruz.
rotated_image.show()  # Döndürülmüş görseli gösteriyoruz.
rotated_image.save("kus_rotated_90.jpg")  # Görseli 'rotated_90' olarak kaydediyoruz.

# 7. Görsele bulanıklaştırma filtresi ekleme
blurred_image = image.filter(ImageFilter.BLUR)  # Görsele bulanıklaştırma filtresi uyguluyoruz.
blurred_image.show()  # Bulanıklaştırılmış görseli gösteriyoruz.
blurred_image.save("kus_blurred.jpg")  # Görseli 'blurred' olarak kaydediyoruz.

# 8. Görselin renk modunu değiştirme (örneğin RGB'ye dönüştürme)
rgb_image = image.convert("RGB")  # Görseli RGB moduna dönüştürüyoruz.
rgb_image.show()  # RGB modundaki görseli gösteriyoruz.
rgb_image.save("kus_rgb.jpg")  # Görseli 'rgb' olarak kaydediyoruz.
"""