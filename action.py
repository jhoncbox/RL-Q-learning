"""
Created on Thu May 14 17:07:54 2020

@author: Jhon Loaiza

Action Selection Module
"""
# for this modules we import the functions from the Motors file
from motors import goForward, goLeft, goRight
#random library
import random

#this functions select an action randomly when the agent choose to explore the environment
def doRandomAction():
    number = random.randint(0,2)
    if number == 0:
        print('Exploring forward')
        goForward()
    #elif number == 1:
        #print('Exploring Backwards')
        #goBackwards()
    elif number == 1:
        print('Exploring Left')
        goLeft()
    else:
        print('Exploring Right')
        goRight()
        
    return number

# here we implement the decision of an action by setting the parameter resulting from the Q-learning.
# the parameter (number) will be implemented from the Action selected from the q-table.
def doActionFromTable(number):
    if number == 0:
        print('from exploiting the table, going Forward')
        goForward()
    #elif number == 1:
        #print('from exploiting the table, going Backwards')
        #goBackwards()
    elif number == 1:
        print('from exploiting the table, going Left')
        goLeft()
    else:
        print('from exploiting the table, going Right')
        goRight()
        
    return number
    
