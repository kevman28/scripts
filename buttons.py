import RPi.GPIO as GPIO
import time
import os
import subprocess

os.system('raspi-gpio set 19 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button next video
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # power off
os.system('raspi-gpio set 19 op a5')


def playNextVideo():
    print ("Next movie")
    os.system('ps -aux | grep omxplayer | grep -v grep | awk \'{ print $2 }\' | xargs kill -9')

def rewidVideo():
    print ("rewid 15 second")
    position = int(os.popen("/home/pi/simpsonstv/dbuscontrol.sh status | grep 'Position:' | awk '{print $2}'").read())
    print (position)
    rewidTime = int(15) # 15 second
    newPosition = position - (rewidTime * 1000 * 1000) # position - 15 second (time must be in microsecond)
    print (newPosition)
    os.system('/home/pi/simpsonstv/dbuscontrol.sh setposition %s' % (newPosition)) #

def shutdownSystem():
    print ("Poweroff")
    os.system('poweroff')

def restartVideo():
        print ("restarting video")
        zero = int(0) #
        os.system('/home/pi/simpsonstv/dbuscontrol.sh setposition $s' % (zero)) #


buttonRight = True
buttonLeft = True

while (True):
    # If you are having and issue with the button doing the opposite of what you want
    # IE Turns on when it should be off, change this line to:
    # input = not GPIO.input(26)
    time.sleep(0.3)

    inputButtonRight = GPIO.input(6)
    inputButtonLeft = GPIO.input(5)


    # check push left and right button
    if ((inputButtonLeft != buttonLeft) and (inputButtonRight != buttonRight)):
        inputButtonLeft != buttonLeft
        inputButtonRight != buttonRight
        if (buttonLeft and buttonRight):
#            shutdownSystem()
                restartVideo()
    else:
        # check push right button
        if inputButtonRight != buttonRight:
            buttonRight = inputButtonRight
            if buttonRight:
                playNextVideo()

        # check push left button
        if inputButtonLeft != buttonLeft:
            buttonLeft = inputButtonLeft
            if buttonLeft:
                rewidVideo()
