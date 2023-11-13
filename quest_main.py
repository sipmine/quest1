import pandas as pd # data.csv proccessing
import cv2 # opencv 
import pyzbar.pyzbar as pyzbar # qr recogniton
import logging # loggin log file

# Настройка логирования
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Загрузка данных из CSV файла
data = pd.read_csv('data.csv')

# Функция для распознавания QR-кода и вывода информации о наличии заказа
def process_order(qr_code_path):
    try:
        # Загрузка изображения QR-кода
        qr_code_image = cv2.imread(qr_code_path)
    except Exception as e:
        logging.error(f"Ошибка обработки заказа: {str(e)}")


for i in range(1,29):
    qr_code_path = r'qr_date\{i}.png'  # Путь к файлу с QR-кодом
    process_order(qr_code_path)
