import threading
import time
import matplotlib.pyplot as plt
timeline_p1=[] 
timeline_p2=[] 
player1_progress=[] 
player2_progress=[] 
vr_headset=threading.Lock() 
game_server=threading.Lock() 

t1=threading.Thread(target=lambda: [
    timeline_p1.append(time.time()),
    player1_progress.append(1),
    print("Player 1: Acquiring VR Headset..."),
    vr_headset.acquire(),
    print("Player 1: VR Headset acquired."),
    time.sleep(1),
    timeline_p1.append(time.time()),
    player1_progress.append(2),
    print("Player 1: Waiting for Game Server..."),
    game_server.acquire(),
    print("Player 1: Game Server acquired."),
    game_server.release(),
    vr_headset.release()
])

t2=threading.Thread(target=lambda: [
    timeline_p2.append(time.time()),
    player2_progress.append(3),
    print("Player 2: Acquiring Game Server..."),
    game_server.acquire(),
    print("Player 2: Game Server acquired."),
    time.sleep(1),
    timeline_p2.append(time.time()),
    player2_progress.append(4),
    print("Player 2: Waiting for VR Headset..."),
    vr_headset.acquire(),
    print("Player 2: VR Headset acquired."),
    vr_headset.release(),
    game_server.release()
])

t1.start()
t2.start()

t1.join(timeout=3)
t2.join(timeout=3)

plt.figure(figsize=(10, 5)) 
plt.plot(timeline_p1, player1_progress, marker="o", label="Player 1 (VR → Game)") 
plt.plot(timeline_p2, player2_progress, marker="x", label="Player 2 (Game → VR)") 

if len(timeline_p1)>1 and len(timeline_p2)>1: 
    plt.scatter(timeline_p1[-1], player1_progress[-1], color='red', s=100, label="Deadlock Point") 
    plt.scatter(timeline_p2[-1], player2_progress[-1], color='red', s=100) 

plt.xlabel("Time") 
plt.ylabel("Resource Acquisition Steps") 
plt.yticks([1, 2, 3, 4], ["P1: Trying VR", "P1: Waiting Game", "P2: Trying Game", "P2: Waiting VR"]) 
plt.title("Deadlock in Metaverse Simulation") 
plt.legend() 
plt.grid() 
plt.show()