import camera
import smtp_mail1
import RPi.GPIO as GPIO
import time
i=0
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) #BUzzer
GPIO.output(24, False)
time.sleep(1) # to stabilize sensor
while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            time.sleep(2) #Buzzer turns on for 0.5 sec
            
            camera.click_photo()
            smtp_mail1.sendPhoto()
            
        
            GPIO.output(24, False)
            print("Motion Detected...",i)
            i+=1
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay
