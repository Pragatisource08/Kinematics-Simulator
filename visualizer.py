#Matplotlib Graph
import matplotlib.pyplot as plt
def plot_journey(sim):
    time_points=[0]
    position_point=[0]
    distance_point=[0]
    for segment in sim.segments:
        time_points.append(time_points[-1]+segment['time'])
        position_point.append(position_point[-1]+segment['distance']*segment['direction'])
        distance_point.append(distance_point[-1]+segment['distance'])
    #average velocity graph    
    plt.plot(time_points ,position_point,marker='o')
    plt.title("Displacement vs Time")
    plt.xlabel('Time(s)')
    plt.ylabel('Displacement(m)')
    plt.grid(True)
    plt.show()

    #average speed graph
    plt.plot(time_points,distance_point,marker='o')
    plt.title("Distance vs Time")
    plt.xlabel('Time(s)')
    plt.ylabel('Distance(m)')
    plt.grid(True)
    plt.show()
