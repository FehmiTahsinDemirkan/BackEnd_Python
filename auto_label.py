# Python'da otomatik etiketleme (automatic labeling), bir veri kümesindeki nesneleri veya bilgileri otomatik olarak
# sınıflandırmak veya etiketlemek için kullanılan bir tekniktir. Bu işlem, makine öğrenimi, derin öğrenme veya doğal dil işleme (NLP) gibi
# çeşitli yöntemlerle gerçekleştirilebilir. Örneğin, görüntülerdeki nesneleri belirlemek, metinlerden konu etiketleri çıkarmak veya
# verilerde sınıflandırma yapmak için kullanılabilir.

# Otomatik Label Yapmanın Temel Adımları
# Veri Hazırlığı: İşlenecek veri (metin, görüntü, video vb.) ve etiketler hazırlanır.
# Model veya Kural Tanımı: Veriye uygun bir makine öğrenimi modeli veya kural seti belirlenir.
# Eğitim veya Kural Uygulama: Model eğitilir veya doğrudan kurallar uygulanır.
# Etiketleme: Model veya kural ile veriler otomatik olarak etiketlenir.

# Metin Verisi İçin Otomatik Etiketleme
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Eğitim verisi
train_texts = [
    "Bu bir spor haberidir",
    "Futbol oynayan bir takım",
    "Teknoloji haberleri burada",
    "Yapay zeka geleceği şekillendiriyor",
    "Basketbol maç sonuçları açıklandı",
    "Yeni telefon modelleri piyasaya çıktı"
]
train_labels = ["spor", "spor", "teknoloji", "teknoloji", "spor", "teknoloji"]

# Model oluştur ve eğit
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train_texts, train_labels)

# Test verisini etiketle
test_texts = ["Yeni bilgisayar teknolojileri", "Futbol ligindeki son durum"]
predicted_labels = model.predict(test_texts)

# Sonuçlar
# for text, label in zip(test_texts, predicted_labels):
#     print(f"Metin: '{text}' => Tahmin Edilen Etiket: {label}")

#Görüntü Verisi İçin Otomatik Etiketleme
import cv2


def label_objects_in_image(image_path):
    # Haar Cascade modelini yükle
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Görüntüyü yükle ve griye dönüştür
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Yüzleri etiketle
    for i, (x, y, w, h) in enumerate(faces, start=1):
        label = f"Yüz {i}"
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Sonuçları göster
    cv2.imshow("Otomatik Etiketleme", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# # Kullanım
# label_objects_in_image("IMG_5775.jpg")


# Kural Tabanlı Etiketleme
def label_based_on_rules(data):
    labels = []
    for item in data:
        if item.isdigit():
            labels.append("Rakam")
        elif item.isalpha():
            labels.append("Harf")
        else:
            labels.append("Karışık")
    return labels

# Kullanım
data = ["123", "abc", "a1b2", "456", "xyz"]
labels = label_based_on_rules(data)

# Sonuç
for item, label in zip(data, labels):
    print(f"'{item}' => Etiket: {label}")
