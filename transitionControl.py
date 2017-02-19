# Simulate the maze
import numpy as np
def transitionControl(curs,act):
    reward=0;
    signal=0;
    r=curs[0];
    c=curs[1];
    ends=np.array([0,8])
    obstacles=np.array([[1,2],[2,2],[3,2],[4,5],[1,7],[2,7],[0,7]])
    
    if act==0:
        c=c+1; # move right
    elif act==1:
        c=c-1; #move left
    elif act==2:
        r=r-1; # move up
    elif act==3:
        r=r+1; #move down
    
    ns=np.array([r,c]);
    if (ends==ns).all(): # reached goal state
        reward=1;
        signal=1;
        ns=ends
        return ns,signal,reward;
    
       
       # check if agent moves out of maze 
    if (c>8 or c< 0  or  r> 5 or r<0):
       ns=curs; 
       
    if any ((ns==obstacles).all(axis=1)):  # Have we moved  into an obstacle
       ns=curs;
    return ns,signal,reward
