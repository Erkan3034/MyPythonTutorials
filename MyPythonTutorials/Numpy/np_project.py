import cv2
import numpy as np
import matplotlib.pyplot as plt

# Matplotlib'in etkileşimli modunu etkinleştir


# Dosya yolunu ayarla
image_path = r'C:\Users\ERKAN TURGUT\Desktop\MyJupyterNotebookNotes\PANDAS\Threshold_Tozero_Image-1024x609.png.webp'

# Görüntüyü yükle
img = cv2.imread(image_path, 0)
if img is None:
    print("Görüntü yüklenemedi!")
else:
    print(f"Görüntü boyutu: {img.shape}")  # Boyutu kontrol et

    # Eşikleme işlemi
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Görüntüleri göster
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Threshold Image')
    plt.imshow(thresh1, cmap='gray')
    plt.axis('off')

    plt.show()

