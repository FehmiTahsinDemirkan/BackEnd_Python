#
# ?Image Check (Görüntü Kontrolü) Nedir?
# Image check, bir görüntünün belirli kriterlere göre doğruluğunu, uygunluğunu veya içeriğini analiz etmek anlamına gelir. Bu işlem, genellikle aşağıdaki durumlarda gerçekleştirilir:
#
# Boyut Kontrolü: Görüntünün belirli bir çözünürlükte olup olmadığını kontrol etmek.
# Format Kontrolü: Görüntünün istenilen formatta (ör. PNG, JPEG) olup olmadığını doğrulamak.
# Dosya Boyutu Kontrolü: Görüntü dosyasının boyutunun belirli bir sınırı aşıp aşmadığını kontrol etmek.
# Renk Alanı veya Mod Kontrolü: Görüntünün RGB mi, siyah-beyaz mı olduğunu doğrulamak.
# ! Metin veya Nesne Tespiti: Görüntüde belirli nesnelerin veya metinlerin olup olmadığını analiz etmek.

from PIL import Image

# Görüntü Boyutunu ve Formatını Kontrol Etme
def check_image_properties(image_path):
    try:
        with Image.open(image_path) as img:
            # Boyutları al
            width, height = img.size
            # Formatı al
            image_format = img.format
            print(f"Boyut: {width}x{height}, Format: {image_format}")

            # Kontroller
            if width > 1920 or height > 1080:
                print("Görüntü boyutu çok büyük!")
            if image_format not in ["JPEG", "PNG"]:
                print("Uygun olmayan format!")
    except Exception as e:
        print(f"Hata: {e}")

# check_image_properties("assets/ornek_resim.jpg")


# Dosya Boyutunu Kontrol Etme

import os

def check_file_size(image_path, max_size_kb):
    file_size = os.path.getsize(image_path) / 1024  # KB cinsine çevir
    print(f"Dosya Boyutu: {file_size:.2f} KB")
    if file_size > max_size_kb:
        print("Görüntü dosyası çok büyük!")

# check_file_size("assets/ornek_resim.jpg", max_size_kb=90000)

#Renk Modunu Kontrol Etme (RGB/Siyah-Beyaz)
from PIL import Image

def check_color_mode(image_path):
    try:
        with Image.open(image_path) as img:
            color_mode = img.mode
            print(f"Renk Modu: {color_mode}")
            if color_mode != "RGB":
                print("Görüntü RGB değil!")
    except Exception as e:
        print(f"Hata: {e}")

# check_color_mode("assets/ornek_resim.jpg")
# Görüntüde Metin Tespiti (OCR ile)
import pytesseract
from PIL import Image

def check_text_in_image(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
            if text.strip():
                print("Görüntüde metin tespit edildi!")
                print("Metin İçeriği:")
                print(text)
            else:
                print("Görüntüde metin bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")

# Tesseract OCR yolunu belirtin (gerekiyorsa)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# check_text_in_image("assets/pngimg.png")

# Görüntüde Nesne Tespiti (OpenCV ile)
import cv2


def detect_faces(image_path):
    # Haar Cascade dosyasını yükleyin
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Görüntüyü yükle ve gri tonlamaya çevir
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Tespit edilen yüz sayısı: {len(faces)}")
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Görüntüyü göster
    cv2.imshow("Yüzler", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Kullanım
detect_faces("assets/IMG_5775.jpg")



