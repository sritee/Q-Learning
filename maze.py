import numpy as np
import pylab as plt
from transitionControl import transitionControl
alpha=0.1
epsilon=0.1 # exploration policy
num_iters=1e2
gamma=0.95


allstates=np.zeros([6,9]) # Change the size of the maze.
num_step_taken=np.zeros(int(num_iters))
# action 0 is right,left is 1, up is 2,down is 3.
qvalues=np.zeros([54,4])

for hi in range (int(num_iters)):
    num_tries=0
    curstate=[2,0]
    csi=np.ravel_multi_index(curstate,allstates.shape) # initialize the current state to start state [3,1]
    qvisit=np.zeros([54,4])
    while (1): #until terminal state
        num_tries=num_tries+1
        #print(curstate)
        np.ravel_multi_index(curstate,allstates.shape)     #convert to index                                       # convert state to index
        
        if(np.random.rand(1)>epsilon): # greedy action
            action=np.argmax(qvalues[csi,:])
            qvisit[csi,action]=1
        else:
            temp=np.random.permutation(4) # exploring action
            action=temp[0]
            qvisit[csi,action]=1
        
        nextstate,signal,reward= transitionControl(curstate,action)
        nsi=np.ravel_multi_index(nextstate,allstates.shape)
        
        if signal==1 : # we have now reached a terminal state
            qvalues[csi,action]=qvalues[csi,action]+ alpha*(reward- qvalues[csi,action])
            qvisit[csi,action]=1
            break
        
        q_next=np.argmax(qvalues[nsi,:])
        
        qvalues[csi,action]=qvalues[csi,action]+ alpha*(reward +qvalues[nsi,q_next]- qvalues[csi,action])
        curstate=nextstate
        csi=nsi
       
    print('Henry has completed the task in',int(num_tries))
    num_step_taken[hi]=num_tries

 
   
#now we shall plot everthing
plt.plot(range(int(num_iters)),num_step_taken,'k')
plt.xlabel('Number of iterations')
plt.ylabel('Number of moves taken to solve')
plt.title('Agent on Maze Task')
plt.show()

# Simulate the maze

