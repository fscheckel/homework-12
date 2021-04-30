import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    NTl = 1000
    NPb = 0
    NBi = 10000
    tau_Tl = 3.053*60 #half life of thallium in seconds
    timestep = 1 #second
    tmax = 1000
    p_decay = 1-2**(-timestep/tau_Tl) #decay probability in one second

    ts = np.arange(0, tmax, timestep)

    Tl = []
    Pb = []
    Bi = []
    for t in ts:
        #log number of remaning Tl and Pb
        Tl.append(NTl)
        Pb.append(NPb)
        Bi.append(NBi)
        #step through # of Tl atoms remaining
        for i in range(NTl):
            #if atom decays, one
            if np.random.random()<p_decay:
                NTl = NTl-1
                NPb = NPb+1
                NBi = NBi+2
    plt.plot(ts, Bi, 'g.', label = 'Bi')
    plt.plot(ts, Tl, 'k.', label = 'Tl')
    plt.plot(ts, Pb, 'r.', label = 'Pb')
    plt.xlabel('Time [s]')
    plt.ylabel('Number of atoms')
    plt.legend()
    plt.show()