
# temp control with cooling fan.
# connect a fan via a npn transistor.
# power from the 5V of the rpi.

import os
import time
import RPi.GPIO as GPIO
fanPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(fanPin, GPIO.OUT)
threshHoldTempOn = 45
threshHoldTempOff = 40
pwmPrecentCycle = 75
p = GPIO.PWM(fanPin, 200)  # frequency=200Hz
p.start(0)

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return float((temp.replace("temp=","").replace("\'C\n","")))

try:
    while True:
        currentTemp = measure_temp()
        if currentTemp >= threshHoldTempOn:
            p.ChangeDutyCycle(pwmPrecentCycle)
            #GPIO.output(fanPin, GPIO.HIGH)
            print ("hot")
        elif currentTemp <= threshHoldTempOff:
            p.ChangeDutyCycle(0)
            #p.stop()
            #GPIO.output(fanPin, GPIO.LOW)
            print ("ok")
        else:
            print ("no chnage")
        print(currentTemp)
        print("----------------")
        
        time.sleep(30)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Press Ctrl-C to terminate while statement")
    pass

