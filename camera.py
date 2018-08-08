import picamera
import time
camera =picamera.PiCamera()
def click_photo():
    

    camera.hflip=True
    camera.start_preview()
    
    '''
    for i in range(5):
        time.sleep(5)
        camera.capture('image%d.jpg'%i)
    '''

    camera.capture("image1.jpg")

    camera.stop_preview()
