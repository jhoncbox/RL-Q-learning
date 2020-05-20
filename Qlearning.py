"""
Created on Thu May 14 17:07:54 2020

@author: Jhon Loaiza

Q-learning algorithm and learning sessions
"""
#essential libraries
import numpy as np
import random
import time

#importing the functions to Check state and control the agent
from state import check_state
from action import doRandomAction, doActionFromTable


#number of possible Actions and states
actions_number = 3
states_number = 4

#initializing the q-table with zeros
q_table = np.zeros((states_number,actions_number))
#q_table = np.loadtxt('qtable.csv', delimiter=',')

#I set the maximum number os sessions to 50.
num_sessions = 50
#per session the agent will have 15 times to make decitions without crashing
max_decisions_per_session = 15

#the learning rate is set to be 0.4, meaning that 40 percent of the old value will be retain when learning a new value.
learning_rate = 0.4

#discount rate that determines the importance of future rewards
discount_rate = 0.99

# the exploration rate is set  to start with one. the min a max possible exploration rate is set between 1 and 0.01
#the exploration decay is set to 0.002.
exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_rate_decay = 0.02

# initialization of the rewards per session
rewards_all_sessions = []




#Q-learning algorithm
for session in range(num_sessions):
    # to reset the device manually to its inittial position for the test, I delay the program for 10 seconds
    print('Session No: ', session+1)    
    print('waiting to be set up...')    
    time.sleep(10)
    #the initial state of the agent is set to zero    
    state = 0
    # crashed is initialized as False and I set the count of rewards to zero for current session
    crashed = False
    rewards_current_session = 0
    
    #loop for agent decisions (maximum 15)
    for decision in range(max_decisions_per_session):
            
        print('Session No: ', session+1) 
        print('decision No: ', decision+1)
        #exploration or exploitation approach
        exploration_rate_dividedline = random.uniform(0,1)
        
        # if the agent is set to exploit the knowledge from the table,
        # then check the table for the higher value at the current state.
        if exploration_rate_dividedline > exploration_rate:
            
            action = doActionFromTable(np.argmax(q_table[state,:]))
            
        else:
            #if the agent is set to explore, then perform a random action.
            action = doRandomAction()
        
        #after the action is performed, check the current state, and get the reward and if the car crashed. 
        new_state, reward, crashed = check_state()
        
        # this is the formula to update the Q-value at the Q-table. (the mathematical equation written in Python language)
        q_table[state,action] = q_table[state,action] * (1- learning_rate) + \
            learning_rate * reward + discount_rate * np.max(q_table[new_state, :])
        
        #set the state to be the new_state of the agent.
        state = new_state
        #add the reward obtained from the action.
        rewards_current_session += reward
        
        #if the car crashed, then the current session is terminated and the agent pass to the next session.
              
        if crashed == True:
            break
        
    
    # after the current session is done, we update the exploration rate accordingly
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * \
        np.exp(-exploration_rate_decay*session)
    # then we add the rewards obtained to the list of rewards for all sessions
    rewards_all_sessions.append(rewards_current_session)
    #here we save the final Q-table as a csv file to be used later for our test sessions
    np.savetxt('qtable.csv',q_table, delimiter=',', fmt='%1.5f')
    
#here we can caltulate the average reward per 10 sessions. for future
rewards_per_ten_sessions = np.split(np.array(rewards_all_sessions), num_sessions/10)
count = 10
for r in rewards_per_ten_sessions:
    print(count, ": ", str(sum(r/10)))
    count += 10

#printing the resulting Q-table
print('\nQ-table\n')
print(q_table)


