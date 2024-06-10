from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import threading
import time


# Функция для обработки данных
def process_data(rdd):
    # Здесь вы можете добавить логику обработки данных
    data = rdd.collect()
    for record in data:
        print(record)  # Или сохраните данные в нужную структуру


# Инициализация контекста Spark
sc = SparkContext(appName="ProduceConsoleApp")
ssc = StreamingContext(sc, 5)  # Интервал обработки 1 секунда

# Создание DStream из сокета (например, localhost:9999)
lines = ssc.socketTextStream("localhost", 9999)

# Применение функции обработки данных к каждому RDD
lines.foreachRDD(lambda rdd: process_data(rdd))


# Функция для запуска стриминга в отдельном потоке
def start_streaming():
    ssc.start()
    ssc.awaitTermination()


# Запуск стриминга в отдельном потоке
streaming_thread = threading.Thread(target=start_streaming)
streaming_thread.start()

# Основной поток вашего приложения
try:
    while True:
        time.sleep(1)  # Основной поток делает что-то другое
except KeyboardInterrupt:
    ssc.stop(stopSparkContext=True, stopGraceFully=True)
