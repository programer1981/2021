from datetime import datetime
import RPi.GPIO as GPIO    #импорт библиотеки для работы с GPIO
import time

GPIO.setmode(GPIO.BOARD)   #first comm GPIO
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

GPIO.output(10, 1)
time.sleep(1)

GPIO.output(22, 0)      #D0 k2
GPIO.output(10, 0)      #D1 k2
GPIO.output(9, 0)       #D2 K2

GPIO.output(4, 0)       #D0
GPIO.output(17, 0)      #D1
GPIO.output(27, 0)      #D2
strobe()

time.sleep(60)
    
GPIO.output(22, 1)      #D0 k2
GPIO.output(10, 0)      #D1 k2
GPIO.output(9, 0)       #D2 K2

GPIO.output(4, 1)       #D0
GPIO.output(17, 0)      #D1
GPIO.output(27, 0)      #D2
strobe()

time.sleep(60)

GPIO.output(22, 0)      #D0 k2
GPIO.output(10, 1)      #D1 k2
GPIO.output(9, 0)       #D2 K2

GPIO.output(4, 0)       #D0
GPIO.output(17, 1)      #D1
GPIO.output(27, 0)      #D2
strobe()
time.sleep(60)


GPIO.output(22, 0)      #D0 k2
GPIO.output(10, 1)      #D1 k2
GPIO.output(9, 1)       #D2 K2

GPIO.output(4, 0)       #D0
GPIO.output(17, 1)      #D1
GPIO.output(27, 1)      #D2
strobe()
time.sleep(60)


def strobe():
    
    GPIO.output(15, 0)    
    time.sleep(0.1)
    GPIO.output(15, 1)
    
    GPIO.output(5, 0)    
    time.sleep(0.1)
    GPIO.output(5, 1)

while(True):
    now= datetime.now()
    minute=int(now.strftime("%M"))
    if 0 <= minute and minute < 15 : #faza 1
        GPIO.output(22, 0)      #D0 k2
        GPIO.output(10, 0)      #D1 k2
        GPIO.output(9, 0)       #D2 K2

        GPIO.output(4, 0)       #D0
        GPIO.output(17, 0)      #D1
        GPIO.output(27, 0)      #D2
        strobe()
        time.sleep(60)

    
    if 15 <= minute and minute < 30: #faza 2
        
        GPIO.output(22, 1)      #D0 k2
        GPIO.output(10, 0)      #D1 k2
        GPIO.output(9, 0)       #D2 K2

        GPIO.output(4, 1)       #D0
        GPIO.output(17, 0)      #D1
        GPIO.output(27, 0)      #D2
        strobe()


    if 30 <= minute and minute < 45: #faza 3
        
        GPIO.output(22, 0)      #D0 k2
        GPIO.output(10, 1)      #D1 k2
        GPIO.output(9, 0)       #D2 K2

        GPIO.output(4, 0)       #D0
        GPIO.output(17, 1)      #D1
        GPIO.output(27, 0)      #D2
        strobe()
        
    if 45 <= minute and minute < 60: #faza 3
        #chenal 1 comm 1
        GPIO.output(22, 1)      #D0 k2
        GPIO.output(10, 0)      #D1 k2
        GPIO.output(9, 0)       #D2 K2

        GPIO.output(4, 1)       #D0 
        GPIO.output(17, 0)      #D1
        GPIO.output(27, 0)      #D2
        strobe()

GPIO.cleanup()