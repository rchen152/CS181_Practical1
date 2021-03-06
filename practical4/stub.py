
import numpy as np
import numpy.random as npr
import sys

from SwingyMonkey import SwingyMonkey

tree_dist_bins = 10
tree_top_bins = 10
m_vel_bins = 10
m_top_bins = 10
num_act = 2

screen_width  = 600
screen_height = 400
horz_speed    = 25
impulse       = 15
gravity       = 3
tree_mean     = 5
tree_gap      = 200
tree_offset   = -300
edge_penalty  = -10.0
tree_penalty  = -5.0
tree_reward   = 1.0
max_m_vel = 2*impulse
min_m_vel = impulse / 2
min_tree_dist = -100 # assumes cannot be less than -200 from tree
mint_tree_top = 350
max_tree_top = 200

class Learner:

    def __init__(self):
        self.last_state  = None
        self.last_action = None
        self.last_reward = None
        self.q_fn = np.zeros((tree_dist_bins,tree_top_bins,m_vel_bins, m_top_bins,num_act))

    def reset(self):
        self.last_state  = None
        self.last_action = None
        self.last_reward = None

    def action_callback(self, state):
        '''Implement this function to learn things and take actions.
        Return 0 if you don't want to jump and 1 if you do.'''

        # You might do some learning here based on the current state and the last state.

        # You'll need to take an action, too, and return it.
        # Return 0 to swing and 1 to jump.
        
        if (state['tree']['dist']<= min_tree_dist):
            tree_dist = 0
        else:
            #assumes the distace to the tree is at most the distance of the screen. Computes the bin to put the distance in
            tree_dist = (state['tree']['dist']+min_tree_dist)*tree_dist_bins/(min_tree_dist+screen_width) 
        
        if (state['tree']['top'] <= 
tree_top = state['tree']['top'] * tree_top_bins/
        if(state['monkey']['vel'] >= max_m_vel):
            m_vel = m_vel_bins
        m_vel = state['monkey']['vel'] * m_vel_bins / 



        new_action = npr.rand() < 0.1
        new_state  = state

        self.last_action = new_action
        self.last_state  = new_state

        return self.last_action

    def reward_callback(self, reward):
        '''This gets called so you can see what reward you get.'''        
        self.last_reward = reward
  
iters = 100
learner = Learner()

for ii in xrange(iters):

    # Make a new monkey object.
    swing = SwingyMonkey(sound=False,            # Don't play sounds.
                         text="Epoch %d" % (ii), # Display the epoch on screen.
                         tick_length=1,          # Make game ticks super fast.
                         action_callback=learner.action_callback,
                         reward_callback=learner.reward_callback)

    # Loop until you hit something.
    while swing.game_loop():
        pass

    # Reset the state of the learner.
    learner.reset()



    
