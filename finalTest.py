# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:56:46 2020

@author: Jhon Loaiza

Final test using the Q-table from the learning session
"""
# necessary libraries and functions
import numpy as np
from state import check_state
from action import doActionFromTable
import time

#importing the Q-table (cvs file) 
q_table = np.loadtxt('qtable.csv', delimiter=',')

#setting the masimum decision
num_sessions = 4
max_decisions_per_session = 20

# loop to start sessions, for this test i set up 4 sessions
for session in range(num_sessions):
    state = 0
    crashed = False
    print('SESSION NO: ', session+1 )
    time.sleep(10)
    # loop to start the decision making process
    for decision in range(max_decisions_per_session):
        #getting an action from the imported table
        action = doActionFromTable(np.argmax(q_table[state,:]))
        # resulting state, reward and if the car crashed
        new_state, reward, crashed = check_state()
        
        #printing the resulting output
        if crashed:
            print('THE CAR JUST CRASHED')
            break
        else:
            print('THE CAR DID NOT CRASHED')
            
        #setting the new state
        state = new_state
            
        
