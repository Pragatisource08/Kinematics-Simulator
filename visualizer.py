import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.animation import FuncAnimation

def animate_journey(sim):
    total_time=sim.total_time()
    times=np.linspace(0,total_time,100)

    position=[]
    distances=[]
    velocities=[]
    speeds=[]

    for t in times:
        pos=0
        dist=0
        elapsed=0
        velocity=0
        speed=0
        for segment in sim.segments:
            if t>=elapsed+segment['time']:
                pos+=segment['distance']*segment['direction']
                velocity = segment['distance'] / segment['time'] * segment['direction']
                speed = segment['distance'] / segment['time']
                elapsed+=segment['time']
                dist+=segment['distance']
            else:
                time_into_segment = t - elapsed
                speed = segment['distance'] / segment['time']
                pos += speed * segment['direction'] * time_into_segment
                velocity = segment['distance'] / segment['time'] * segment['direction']
                dist += speed * time_into_segment
                break
        position.append(pos)        
        distances.append(dist)
        velocities.append(velocity)
        speeds.append(speed)
    
    fig = plt.figure(figsize=(14,8))
    gs=gridspec.GridSpec(3,2,figure=fig)

    ax_dot = fig.add_subplot(gs[0,:])
    ax_disp=fig.add_subplot(gs[1,0])
    ax_dist=fig.add_subplot(gs[1,1])
    ax_vel =fig.add_subplot(gs[2,0])
    ax_spd =fig.add_subplot(gs[2,1])



    ax_dot.set_xlim(min(position)-10,max(position)+10)
    ax_dot.set_ylim(-1,1)
    ax_dot.set_title('Object Motion')
    ax_dot.set_xlabel('Position(m)')
    dot,=ax_dot.plot([],[],'bo', markersize=15)

    ax_disp.set_xlim(0,total_time)
    ax_disp.set_ylim(min(position)-10,max(position)+10)
    ax_disp.set_title('Displacement vs Time')
    ax_disp.set_xlabel('Time(sec)')
    ax_disp.set_ylabel('Displacement(m)')
    line,=ax_disp.plot([],[],'g-')
    
    ax_dist.set_xlim(0,total_time)
    ax_dist.set_ylim(0,sim.total_distance()+10)
    ax_dist.set_title('Distance vs Time')
    ax_dist.set_xlabel('Time(sec)')
    ax_dist.set_ylabel('Distance(m)')
    line1,=ax_dist.plot([],[],'g-')

    ax_vel.set_xlim(0,total_time)
    ax_vel.set_ylim(min(velocities)-5,max(velocities)+5)
    ax_vel.set_title('Velocity vs Time')
    ax_vel.set_xlabel('Time(sec)')
    ax_vel.set_ylabel('Velocity(m/s)')
    line2,=ax_vel.plot([],[],'g-')

    ax_spd.set_xlim(0,total_time)
    ax_spd.set_ylim(0,max(speeds)+10)
    ax_spd.set_title('Speed vs Time')
    ax_spd.set_xlabel('Time(sec)')
    ax_spd.set_ylabel('Speed(m/s)')
    line3,=ax_spd.plot([],[],'g-')

    stats_text=fig.text(0.5 , 0.01 ,' ', fontsize=10 , ha='center',
    bbox=dict(boxstyle='round',facecolor='lightblue',edgecolor='black',alpha=0.8))

   
    def update(frame):
        dot.set_data([position[frame]],[0])
        line.set_data(times[:frame],position[:frame])
        line1.set_data(times[:frame],distances[:frame])
        line2.set_data(times[:frame],velocities[:frame])
        line3.set_data(times[:frame],speeds[:frame])
        t_now = times[frame]
        avg_velocity = position[frame] / t_now if t_now > 0 else 0
        avg_speed = distances[frame] / t_now if t_now > 0 else 0
        flag = abs(position[frame]) < 0.5 and distances[frame] > 0
        stats_text.set_text(f"Time: {times[frame]:.2f}s | Position: {position[frame]:.2f}m | Velocity: {velocities[frame]:.2f} m/s\n"
             f"Avg Velocity so far: {avg_velocity:.2f} m/s | Avg Speed so far: {avg_speed:.2f} m/s\n"
        f"{'Returned near origin ⚡' if flag else ''}")

             
        return dot ,line,line1,line2,line3,stats_text

    ani=FuncAnimation(fig,update,frames=100,interval=50,blit=False)
    plt.tight_layout()
    plt.show()