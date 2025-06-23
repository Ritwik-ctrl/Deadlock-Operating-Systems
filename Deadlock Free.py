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
    print("Player 1: Acquiring Game Server..."),
    game_server.acquire(),
    print("Player 1: Game Server acquired. Playing Metaverse!"),
    time.sleep(1),
    game_server.release(),
    vr_headset.release()
])

t2=threading.Thread(target=lambda: [
    timeline_p2.append(time.time()),
    player2_progress.append(1),
    print("Player 2: Acquiring VR Headset..."),
    vr_headset.acquire(),
    print("Player 2: VR Headset acquired."),
    time.sleep(1),
    timeline_p2.append(time.time()),
    player2_progress.append(2),
    print("Player 2: Acquiring Game Server..."),
    game_server.acquire(),
    print("Player 2: Game Server acquired. Playing Metaverse!"),
    time.sleep(1),
    game_server.release(),
    vr_headset.release()
])

t1.start()
t2.start()

t1.join()
t2.join()

plt.figure(figsize=(10, 5)) 
plt.plot(timeline_p1, player1_progress, marker="o", label="Player 1") 
plt.plot(timeline_p2, player2_progress, marker="x", label="Player 2") 
plt.xlabel("Time") 
plt.ylabel("Resource Acquisition Steps") 
plt.yticks([1, 2], ["Acquiring VR", "Acquiring Game Server"]) 
plt.title("Deadlock-Free Metaverse Simulation") 
plt.legend() 
plt.grid() 
plt.show()