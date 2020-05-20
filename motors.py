"""
Created on Wed May 13 11:09:32 2020

@author: Jhon Loaiza

Motors Control Functions
"""
import RPi.GPIO as GPIO
import time


#GPIO pins to be used (using the board configuration)
Motor1A = 11
Motor1B = 13

Motor2A = 16
Motor2B = 18

# function for motors to Go forward
def goForward():
    #Setting the GPIO mode to for the board numbers   
    GPIO.setmode(GPIO.BOARD)    
    
    #setting motors GPIO pins for outbound signals (OUT)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)    
    
    print ("Turning motors Forward")
    # setting motors signals in order to move engines forward
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)

    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    
    #setting tehe time of the action to 1 second
    time.sleep(0.8)
    #clening the GPIO setup
    GPIO.cleanup()

# function for motors to go Backwards
def goBackwards():
    #Setting the GPIO mode to for the board numbers
    GPIO.setmode(GPIO.BOARD)
    #setting motors GPIO pins for outbound signals (OUT)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)    
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)   
    
    #setting motors signals in order to move engines backwards    
    print ("Turning motors Backwards")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)

    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    
    #setting tehe time of the action to 1 second
    time.sleep(0.8)
    #clening the GPIO setup
    GPIO.cleanup()

# function for motors to go left
def goLeft():
    #Setting the GPIO mode to for the board numbers
    GPIO.setmode(GPIO.BOARD)
    #setting motors GPIO pins for outbound signals (OUT)    
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)    
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    #setting motors signals in order to move engines to the left    
    print ("Turning motors Left")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)

    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    #setting tehe time of the action to 1 second
    time.sleep(0.5)
    #clening the GPIO setup
    GPIO.cleanup()

# function for motors to go right
def goRight():
    #Setting the GPIO mode to for the board numbers
    GPIO.setmode(GPIO.BOARD)
    #setting motors GPIO pins for outbound signals (OUT)    
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)    
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    #setting motors signals in order to move engines to the right        
    print ("Turning motors Right")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)

    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    #setting tehe time of the action to 1 second
    time.sleep(0.5)
    #clening the GPIO setup
    GPIO.cleanup()
