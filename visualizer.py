#Matplotlib Graph
#import matplotlib.pyplot as plt
#def plot_journey(sim):
 #   time_points=[0]
  #  position_point=[0]
   # distance_point=[0]
   # for segment in sim.segments:
   # time_points.append(time_points[-1]+segment['time'])
  #      position_point.append(position_point[-1]+segment['distance']*segment['direction'])
#        distance_point.append(distance_point[-1]+segment['distance'])
 #   #average velocity graph    
  #  plt.plot(time_points ,position_point,marker='o')
   # plt.title("Displacement vs Time")
   # plt.xlabel('Time(s)')
    #plt.ylabel('Displacement(m)')
  #  plt.grid(True)
   # plt.show()

    #average speed graph
 #   plt.plot(time_points,distance_point,marker='o')
  #  plt.title("Distance vs Time")
   # plt.xlabel('Time(s)')
 #   plt.ylabel('Distance(m)')


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_journey(sim):
    total_time=sim.total_time()
    times=np.linspace(0,total_time,100)

    position=[]
    distances=[]
    for t in times:
        pos=0
        dist=0
        elapsed=0
        for segment in sim.segments:
            if t>=elapsed+segment['time']:
                pos+=segment['distance']*segment['direction']
                elapsed+=segment['time']
                dist+=segment['distance']
            else:
                time_into_segment = t - elapsed
                speed = segment['distance'] / segment['time']
                pos += speed * segment['direction'] * time_into_segment
                dist += speed * time_into_segment
                break
        position.append(pos)        
        distances.append(dist)

        

    fig, ((ax1,ax2),(ax3,ax3)) = plt.subplots(2,2,figsize=(14,8))

    ax1.set_xlim(min(position)-10,max(position)+10)
    ax1.set_ylim(-1,1)
    ax1.set_title('Object Motion')
    ax1.set_xlabel('Position(m)')
    dot,=ax1.plot([],[],'bo', markersize=15)

    ax2.set_xlim(0,total_time)
    ax2.set_ylim(min(position)-10,max(position)+10)
    ax2.set_title('Displacement vs Time')
    ax2.set_xlabel('Time(sec)')
    ax2.set_ylabel('Displacement(m)')
    line,=ax2.plot([],[],'g-')
    
    ax3.set_xlim(0,total_time)
    ax3.set_ylim(0,sim.total_distance()+10)
    ax3.set_title('Distance vs Time')
    ax3.set_xlabel('Time(sec)')
    ax3.set_ylabel('Distance(m)')
    line1,=ax3.plot([],[],'g-')

    def update(frame):
        dot.set_data([position[frame]],[0])
        line.set_data(times[:frame],position[:frame])
        line1.set_data(times[:frame],distances[:frame])
        return dot ,line,line1

    ani=FuncAnimation(fig,update,frames=100,interval=50,blit=True)
    plt.tight_layout()
    plt.show()