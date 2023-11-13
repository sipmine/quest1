import pandas as pd
import cv2
import pyzbar.pyzbar as pyzbar
import logging

# Настройка логирования
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Загрузка данных из CSV файла
data = pd.read_csv('data.csv')

# Функция для распознавания QR-кода и вывода информации о наличии заказа
def process_order(qr_code_path):
    try:
        # Загрузка изображения QR-кода
        qr_code_image = cv2.imread(qr_code_path)
        
        # Распознавание QR-кода с использованием pyzbar
        decoded_objects = pyzbar.decode(qr_code_image)
        
        for obj in decoded_objects:
            order_id = obj.data.decode('utf-8')
            if order_id.startswith('http://'):
                order_id = order_id.split('/')[-1]
            

            # Поиск заказа в данных
            order_info = data[data['order_id'] == int(order_id)]
            if not order_info.empty:
                logging.info(f"Заказ {order_id} найден в базе данных: {order_info[['order_id', 'order_name', 'order_path', 'order_prcie']].to_dict('records')}")
            else:
                logging.info(f"Заказ {order_id} не найден в базе данных.")
        
        if not decoded_objects:
            logging.info("QR-код не распознан.")
    except Exception as e:
        logging.error(f"Ошибка обработки заказа: {str(e)}")


for i in range(1,29):
    qr_code_path = f'qr_date/{i}.png'  # Путь к файлу с QR-кодом
    process_order(qr_code_path)
