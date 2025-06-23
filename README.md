# Deadlock-Operating-Systems
These codes simulate how threads i.e. players try to acquire shared resources (VR Headset and Game Server) in a multithreaded environment using Python. The goal is to visualize deadlock vs deadlock-free execution using matplotlib.

First code represents Deadlock Simulation where:
Player 1 tries to acquire VR Headset first. Once acquired, it tries to acquire Game Server.
Player 2 tries to acquire Game Server first. Once acquired, it tries to acquire VR Headset.

Now, if Player 1 holds VR Headset and Player 2 holds Game Server, both wait forever for each other’s resource, thus leading to Deadlock.
Threads get stuck, shown by the join(timeout=3) timeout and a red "Deadlock Point" is marked on the plot.

Second code represents Deadlock-Free Simulation where:
Both Player 1 and Player 2 always acquire VR Headset first, then Game Server.
They follow the same lock order, now, because both threads acquire locks in the same order, there’s no circular wait and hence, no deadlock.
One player waits until the other releases the resources, but the system continues smoothly.
