# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:02:29 2020

@author: Jhon Loaiza

State and reward check Module
"""
import RPi.GPIO as GPIO
from sensor import ping


#fucntion to check the distance from all sensors
def check_distances():
    #GPIO ports to be used (using the board configuration) from each sensor
    echopin = [31,40,35,36,26]
    trigpin = [33,38,37,32,24]
    
    #list of sensors
    distance = [1,2,3,4,5]
    
    #getting the distance from each of the sensors
    for j in range (5):
        #Setting the GPIO mode to for the board numbers.    
        GPIO.setmode(GPIO.BOARD)
        #setting motors GPIO pins for  inbound and outbound signals
        GPIO.setup(trigpin[j], GPIO.OUT)
        GPIO.setup(echopin[j], GPIO.IN)
        #saving the distances inside the distance list 
        distance[j] = ping(echopin[j], trigpin[j])
    
    #Clean up the GPIO setup   
    GPIO.cleanup()
    #return the list of distances
    return distance


#function to check the current state of the agent and gives the according reward.    
def check_state():
    #retrieving the distances from the Check_distances function
    distances = check_distances()
    #these are all the possible states the agent can have
    allClear = 0
    tooCloseFront = 1
    tooCloseRight = 2
    tooCloseLeft = 3
    #setting the initial State, Reward and if the car crashed (boolean)
    state = 0
    reward = 0
    crashed = False
    # these are range of distance for the agent to make decisions (between 10 and 40 cm)
    desire_distance = 40 #40 cm
    min_desire_distance = 10 #10 cm
    # this section present the if statement that will determine on which state is the agent according to the distances of the sensors
    # starting with the following:
    # if all distance are bigger than the desire_distance (40cm), then the agent state will be AllClear
    # and the rewars will be added 1
    if distances[0] > desire_distance and distances[1] > desire_distance and distances[2] > desire_distance and \
        distances[3] > desire_distance and distances[4] > desire_distance:
        
        print('allClear')
        state = allClear
        reward += 1
    
    # this statement means that one of the distances have being less than 10cm
    # wich will mean that the car has crashed and it is penalized with a reward of -1.
    elif distances[0] < min_desire_distance or distances[1] < min_desire_distance or \
        distances[2] < min_desire_distance or distances[3] < min_desire_distance or distances[4] < min_desire_distance:
        
        print('Car Crashed')
        crashed = True
        reward -= 10    
    # if the middle sensor checks a distance of less than 40cm but more than 10cm,
    # then the state will be too close front and a reward of zero.
    elif distances[2] < desire_distance and distances[2] > min_desire_distance:
        
        print('Too Close Front')
        state = tooCloseFront
        reward += 0   
    # if the sensor from the right side detect a distance of less than 40cm but more than 10cm,
    # then the state will be too close Right and a reward of zero.  
    elif distances[0] < desire_distance and distances[0] > min_desire_distance:
    
        print('Too Close Right')
        state = tooCloseRight
        reward += 0     
    # if the sensor from the left side detect a distance of less than 40cm but more than 10cm,
    # then the state will be too close Left and a reward of zero.    
    elif distances[4] < desire_distance and distances[4] > min_desire_distance:
        
        print('Too Close Left')
        state = tooCloseLeft
        reward += 0
    
    return state,reward,crashed    
#state, reward, crashed = check_state()
#print(state, reward, crashed)
print(check_distances())   

