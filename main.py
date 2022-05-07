#!/usr/bin/env python3

import RPi.GPIO as GPIO # RPi.GPIOモジュールを使用
import time

# GPIO番号
PORT_DICT = {
"RS_PORT":3,
"E__PORT":2,
"D7_PORT":6,
"D6_PORT":13,
"D5_PORT":19,
"D4_PORT":26,
"D3_PORT":12,
"D2_PORT":16,
"D1_PORT":20,
"D0_PORT":21,
}

def init_gpio():
    # GPIO番号指定の準備
    GPIO.setmode(GPIO.BCM)

    # すべてのpinを出力に設定
    for value in PORT_DICT.values():
        GPIO.setup(value, GPIO.OUT)

def cleanup_gpio():
    # すべてのpinを出力に設定
    for value in PORT_DICT.values():
        GPIO.cleanup(value)

def function_set():
    # モード切り替え
    GPIO.output(PORT_DICT["RS_PORT"], 0)

    GPIO.output(PORT_DICT["E__PORT"], 1)
    GPIO.output(PORT_DICT["E__PORT"], 0)

    GPIO.output(PORT_DICT["D7_PORT"], 0)
    GPIO.output(PORT_DICT["D6_PORT"], 0)
    GPIO.output(PORT_DICT["D5_PORT"], 1)
    GPIO.output(PORT_DICT["D4_PORT"], 1)
    GPIO.output(PORT_DICT["D3_PORT"], 1)
    GPIO.output(PORT_DICT["D2_PORT"], 1)

def change_mode():
    GPIO.output(PORT_DICT["RS_PORT"], 1)
    GPIO.output(PORT_DICT["E__PORT"], 1)
    GPIO.output(PORT_DICT["E__PORT"], 0)

def change_display():  
    # H = 01001000
    change_mode()
    GPIO.output(PORT_DICT["D7_PORT"], 0)
    GPIO.output(PORT_DICT["D6_PORT"], 1)
    GPIO.output(PORT_DICT["D5_PORT"], 0)
    GPIO.output(PORT_DICT["D4_PORT"], 0)
    GPIO.output(PORT_DICT["D3_PORT"], 1)
    GPIO.output(PORT_DICT["D2_PORT"], 0)
    GPIO.output(PORT_DICT["D1_PORT"], 0)
    GPIO.output(PORT_DICT["D0_PORT"], 0)
    # i = 01101001
    change_mode()
    GPIO.output(PORT_DICT["D7_PORT"], 0)
    GPIO.output(PORT_DICT["D6_PORT"], 1)
    GPIO.output(PORT_DICT["D5_PORT"], 1)
    GPIO.output(PORT_DICT["D4_PORT"], 0)
    GPIO.output(PORT_DICT["D3_PORT"], 1)
    GPIO.output(PORT_DICT["D2_PORT"], 0)
    GPIO.output(PORT_DICT["D1_PORT"], 0)
    GPIO.output(PORT_DICT["D0_PORT"], 1)
    # ! = 00100001
    change_mode()
    GPIO.output(PORT_DICT["D7_PORT"], 0)
    GPIO.output(PORT_DICT["D6_PORT"], 0)
    GPIO.output(PORT_DICT["D5_PORT"], 1)
    GPIO.output(PORT_DICT["D4_PORT"], 0)
    GPIO.output(PORT_DICT["D3_PORT"], 0)
    GPIO.output(PORT_DICT["D2_PORT"], 0)
    GPIO.output(PORT_DICT["D1_PORT"], 0)
    GPIO.output(PORT_DICT["D0_PORT"], 1)

def main():
    # GPIOの初期化
    init_gpio()

    function_set()

    try:
        while True:
            change_display()
    except Exception as e:
        print('--- error ---')
        print('  type   :' + str(type(e)))
        print('  args   :' + str(e.args))
        print('  message:' + e.message)
        print('  e      :' + str(e))

    # GPIOを解放
    cleanup_gpio()

if __name__ == '__main__':
    main()
