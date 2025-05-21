import time
import board
from adafruit_bme280 import basic as adafruit_bme280

# I2Cバスの初期化
i2c = board.I2C()

# BME280センサーの初期化
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# 設定
bme280.sea_level_pressure = 1013.25  # 基準気圧 (hPa)

# データ取得ループ
print("BME280センサーのデータ取得")
try:
    while True:
        temperature = bme280.temperature  # 温度 (°C)
        humidity = bme280.humidity        # 湿度 (%)
        pressure = bme280.pressure        # 気圧 (hPa)

        print(f"温度: {temperature:.2f} °C")
        print(f"湿度: {humidity:.2f} %")
        print(f"気圧: {pressure:.2f} hPa")
        print("-" * 30)

        time.sleep(1)  # 1秒間隔で更新
except KeyboardInterrupt:
    print("プログラムを終了します")
