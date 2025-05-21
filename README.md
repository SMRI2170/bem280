
##  概要

このプログラムは、**BME280センサー**を使用して、**温度・湿度・気圧**のデータを**1秒ごとにリアルタイムで取得・表示**するPythonスクリプトです。センサーとの通信にはI2Cインターフェースを使用しており、Adafruitの`adafruit_bme280`ライブラリを用いて簡単に操作できます。

https://qiita.com/ryosuke0712/items/68bce25875c3443fd0a3

##  使用ライブラリ

* `time`：データの取得間隔を制御するために使用。
* `board`：I2Cピンの設定に使用。
* `adafruit_bme280.basic`：BME280センサーを操作するためのAdafruitライブラリ。

##  セットアップ

```bash
pip install adafruit-circuitpython-bme280
```

##  ハードウェア接続

* **センサー**：BME280
* **接続方式**：I2C（例：Raspberry PiのSCL, SDA）

##  プログラムの流れ

1. I2C通信を初期化。
2. BME280センサーをインスタンス化。
3. 基準気圧（海面気圧）を設定（標準値：1013.25 hPa）。
4. `while`ループで温度・湿度・気圧を1秒ごとに取得し、表示。
5. `Ctrl + C`でループを中断し、終了メッセージを表示。

##  ソースコード（再掲）

```python
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
```

##  出力例

```
BME280センサーのデータ取得
温度: 24.36 °C
湿度: 48.21 %
気圧: 1012.87 hPa
------------------------------
```


