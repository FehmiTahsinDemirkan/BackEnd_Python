# Tool Configuration (Araç Yapılandırması), bir yazılımın veya bir aracın işlevlerini belirlemek, yönetmek ve
# özelleştirmek için kullanılan yapılandırma sürecidir. Bu işlem genellikle
# bir araç veya uygulamanın doğru şekilde çalışması için gerekli parametrelerin ayarlanmasını içerir.

# Tool config işlemleri şunları içerebilir:

# Parametre Tanımları: Araçların hangi değerlerle çalışacağını belirleme.
# Dosya veya Ortam Temelli Yapılandırma: Config bilgilerini dosyalarda (JSON, YAML, INI) veya çevresel değişkenlerde saklama.
# Dinamik Yapılandırma: Çalışma sırasında araç parametrelerini değiştirme.

# INI Dosyaları ile Tool Config
import configparser

def create_config(file_name):
    config = configparser.ConfigParser()
    config['DATABASE'] = {
        'host': 'localhost',
        'port': '5432',
        'user': 'admin',
        'password': 'secret'
    }
    config['APP'] = {
        'debug': 'True',
        'log_level': 'INFO'
    }
    with open(file_name, 'w') as configfile:
        config.write(configfile)
    print(f"{file_name} dosyası oluşturuldu.")

def load_config(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)
    print("DATABASE Bilgileri:")
    print(f"Host: {config['DATABASE']['host']}")
    print(f"Port: {config['DATABASE']['port']}")
    print(f"Kullanıcı: {config['DATABASE']['user']}")
    print(f"Şifre: {config['DATABASE']['password']}")
    print("\nAPP Bilgileri:")
    print(f"Debug Modu: {config['APP']['debug']}")
    print(f"Log Seviyesi: {config['APP']['log_level']}")

# Kullanım
# config_file = "Database/config.ini"
# create_config(config_file)
# load_config(config_file)

# JSON Dosyaları ile Tool Config
import json

def create_config(file_name):
    config = {
        "DATABASE": {
            "host": "localhost",
            "port": 5432,
            "user": "admin",
            "password": "secret"
        },
        "APP": {
            "debug": True,
            "log_level": "INFO"
        }
    }
    with open(file_name, "w") as file:
        json.dump(config, file, indent=4)
    print(f"{file_name} dosyası oluşturuldu.")

def load_config(file_name):
    with open(file_name, "r") as file:
        config = json.load(file)
    print("DATABASE Bilgileri:")
    print(f"Host: {config['DATABASE']['host']}")
    print(f"Port: {config['DATABASE']['port']}")
    print(f"Kullanıcı: {config['DATABASE']['user']}")
    print(f"Şifre: {config['DATABASE']['password']}")
    print("\nAPP Bilgileri:")
    print(f"Debug Modu: {config['APP']['debug']}")
    print(f"Log Seviyesi: {config['APP']['log_level']}")

# Kullanım
# config_file = "Database/config.json"
# create_config(config_file)
# load_config(config_file)


# Çevresel Değişkenler ile Tool Config
import os

# Çevresel değişkenleri ayarla
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '5432'
os.environ['DB_USER'] = 'admin'
os.environ['DB_PASSWORD'] = 'secret'
os.environ['DEBUG'] = 'True'

# Çevresel değişkenlerden config yükle
def load_config_from_env():
    config = {
        "DATABASE": {
            "host": os.environ.get('DB_HOST'),
            "port": os.environ.get('DB_PORT'),
            "user": os.environ.get('DB_USER'),
            "password": os.environ.get('DB_PASSWORD'),
        },
        "APP": {
            "debug": os.environ.get('DEBUG') == 'True'
        }
    }
    print("Config Yüklendi:")
    print(config)

# Kullanım
# load_config_from_env()
# YAML Dosyaları ile Tool Config
import yaml

# Config dosyası oluştur
def create_config(file_name):
    config = {
        "DATABASE": {
            "host": "localhost",
            "port": 5432,
            "user": "admin",
            "password": "secret"
        },
        "APP": {
            "debug": True,
            "log_level": "INFO"
        }
    }
    with open(file_name, "w") as file:
        yaml.dump(config, file)
    print(f"{file_name} dosyası oluşturuldu.")

# Config dosyasını yükle
def load_config(file_name):
    with open(file_name, "r") as file:
        config = yaml.safe_load(file)
    print("DATABASE Bilgileri:")
    print(f"Host: {config['DATABASE']['host']}")
    print(f"Port: {config['DATABASE']['port']}")
    print(f"Kullanıcı: {config['DATABASE']['user']}")
    print(f"Şifre: {config['DATABASE']['password']}")
    print("\nAPP Bilgileri:")
    print(f"Debug Modu: {config['APP']['debug']}")
    print(f"Log Seviyesi: {config['APP']['log_level']}")

# Kullanım
# config_file = "Database/config.yaml"
# create_config(config_file)
# load_config(config_file)



# Tool Config Yönetiminin Faydaları
# Esneklik: Parametreler kolayca değiştirilebilir ve farklı ortamlar (geliştirme, üretim) için uyarlanabilir.
# Yeniden Kullanılabilirlik: Aynı yapılandırma farklı araçlarla paylaşılabilir.
# Okunabilirlik: JSON, YAML, veya INI formatları ile yapılandırmalar düzenli ve okunaklıdır.
# Dinamiklik: Çevresel değişkenler veya dosyalar ile çalışma zamanı yapılandırması yapılabilir.