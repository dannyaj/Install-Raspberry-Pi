import time
import RPi.GPIO as GPIO

sleep_time = 0.01

led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)

pwm_led.start(0)

while True:
    for i in range(99):
        i = i + 1
        pwm_led.ChangeDutyCycle(i)
        time.sleep(sleep_time)        
    for i in range(99):
        i = 100 - i
        pwm_led.ChangeDutyCycle(i)
        time.sleep(sleep_time)        
