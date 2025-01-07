# Price Matrix Export (Fiyat Matrisi Çıkartımı), genellikle işletmelerde farklı ürünlerin,
# kategorilerin veya hizmetlerin fiyatlarını temsil eden bir tabloyu dışa aktarma işlemidir.
# Bu işlem, fiyat verilerinin raporlanması, analiz edilmesi veya başka sistemlere entegrasyon için kullanılmasını sağlar.
# Örneğin, bir e-ticaret platformunda ürün fiyatlarının kategori bazında CSV dosyasına yazılması veya bir otelin oda
# fiyatlarını Excel'e aktarması price matrix export'a örnek olabilir.

# Fiyat Matrisi Export İşleminin Adımları
# Fiyat Verilerinin Toplanması: Veriler bir veritabanından, API'den veya dosyalardan alınır.
# Fiyat Matrisi Oluşturulması: Veriler, satırlar ve sütunlar halinde bir matrise dönüştürülür. Örneğin, satırlar ürünleri, sütunlar ise fiyat bilgilerini temsil edebilir.
# Dosya Formatının Belirlenmesi: Veriler genellikle CSV, Excel, JSON veya başka bir formatta dışa aktarılır.
# Dışa Aktarım İşlemi: Veriler belirtilen formata uygun olarak kaydedilir.

# Python ile Price Matrix Export Örnekleri
# 1. CSV Dosyasına Export

import csv

# Örnek fiyat matrisi
price_matrix = [
    ["Ürün Adı", "Kategori", "Fiyat"],
    ["Laptop", "Elektronik", 15000],
    ["Telefon", "Elektronik", 10000],
    ["Buzdolabı", "Ev Aletleri", 8000],
    ["Televizyon", "Elektronik", 12000]
]

# CSV dosyasına yazma
def export_to_csv(matrix, file_name):
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)
    print(f"{file_name} dosyasına başarıyla yazıldı.")

# Kullanım
# export_to_csv(price_matrix, "assets/fiyat_matrisi.csv")

# Excel Dosyasına Export
import openpyxl

# Örnek fiyat matrisi
price_matrix2 = [
    ["Ürün Adı", "Kategori", "Fiyat"],
    ["Laptop", "Elektronik", 15000],
    ["Telefon", "Elektronik", 10000],
    ["Buzdolabı", "Ev Aletleri", 8000],
    ["Televizyon", "Elektronik", 12000]
]

# Excel dosyasına yazma
def export_to_excel(matrix, file_name):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Fiyat Matrisi"

    # Verileri Excel'e yazma
    for row in matrix:
        sheet.append(row)

    # Dosyayı kaydetme
    workbook.save(file_name)
    print(f"{file_name} dosyasına başarıyla yazıldı.")

# Kullanım
# export_to_excel(price_matrix2, "assets/fiyat_matrisi.xlsx")

import json

# Örnek fiyat verileri
price_data = [
    {"Ürün Adı": "Laptop", "Kategori": "Elektronik", "Fiyat": 15000},
    {"Ürün Adı": "Telefon", "Kategori": "Elektronik", "Fiyat": 10000},
    {"Ürün Adı": "Buzdolabı", "Kategori": "Ev Aletleri", "Fiyat": 8000},
    {"Ürün Adı": "Televizyon", "Kategori": "Elektronik", "Fiyat": 12000}
]

# JSON dosyasına yazma
def export_to_json(data, file_name):
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"{file_name} dosyasına başarıyla yazıldı.")

# Kullanım
export_to_json(price_data, "assets/fiyat_matrisi.json")
