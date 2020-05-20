"""
Created on Wed May 13 12:41:04 2020

@author: Jhon Loaiza

Sensor distance calculator
"""
import RPi.GPIO as GPIO
import time

#funtcion to retrieve the distance from a single HC-SR04 sensor.
def ping(echo, trig):
    #Setting the GPIO mode to for the board numbers.
    GPIO.setmode(GPIO.BOARD)
    # As the console will be used to check live what is happening with the prototype
    # I turn off the warnings ussually shown from the GPIO module.
    GPIO.setwarnings(False)

    #this allows time for the module to settle
    time.sleep(0.1)
    
    # here I'm activating the trigger sensor to send the signal for 1 ml (miliseconds).
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    #Then we save the start time from the receiving signal .
    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    # And the arrival time of the signal received.
    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    #then the time difference between start and arrival is saved.
    pulse_duration = pulse_end - pulse_start
    
    # In this section I multiplied the duration the by sonicspeed (34300cm/s)
    # and divided it by 2, because of the going forward and bacward travel that the signal does.
    distance = pulse_duration * (34300/2)
    
    #to clean the result I rounded the value to 2 decimal points.
    distance = round(distance, 2)
    #Clean up the GPIO setup
    GPIO.cleanup()
    #return the result    
    return distance
    
    