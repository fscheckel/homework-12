#brownian motion

import numpy as np
import matplotlib.pyplot as plt
#import problem2_a as p2a


if __name__ == "__main__":
    print("c.   Plot the track of the particle over 10000 steps (3 points)")
    pos = np.array([50, 50])
    X = Y = 50 #can only move 50 units max each
    maxsize = 101
    xvalues = []
    yvalues = []
    #run for 10,000 steps
    #steps1e4 = p2a.run_simulation(n_steps=10000, initial_pos=pos, maxsize=maxsize)
    steps1e4 = np.random.randint(0, 101, size = (10000, 2))
    #animate the figure

    for i in range(1000000):
        walk = np.random.randint(1,5)
        if walk == 1: #up
            if X == maxsize:
                continue
            else:
                X += 1
                xvalues.append(X)
                yvalues.append(Y)
        if walk == 2: #down
            if X == maxsize:
                continue
            else:
                X -= 1
                xvalues.append(X)
                yvalues.append(Y)
        if walk == 3: #right
            if Y == maxsize:
                continue
            else:
                Y -= 1
                xvalues.append(X)
                yvalues.append(Y)
        if walk == 4: #left
            if Y == maxsize:
                continue
            else:
                Y += 1
                xvalues.append(X)
                yvalues.append(Y)

    plt.ion()
    fig, ax = plt.subplots(figsize=(10,10))
    plt.xlim((0, maxsize))
    plt.ylim(0, maxsize)
    ax.set_aspect('equal')
    scat = ax.scatter(*pos)
    plt.title("Brownian motion in a box "+str(maxsize-1)+" units on a side")
    for i in range(10000):
        scat.set_offsets([steps1e4[i,0], steps1e4[i,1]])
        plt.draw()
        plt.pause(0.01)