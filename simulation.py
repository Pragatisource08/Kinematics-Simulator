from motion import Motion 
from visualizer import animate_journey

class Simulation:
    def __init__(self):
        self.segments=[]

    def add_segments(self,distance,direction,time):
        self.segments.append({'distance':distance,'direction':direction,'time':time})

    def total_distance(self):
        total=0
        for segment in self.segments:
            total+=segment['distance']
        return total      

    def total_displacement(self):
        result_displacement =0
        for segment in self.segments:
            result_displacement+=segment['distance']*segment['direction']
        return result_displacement

    def total_time(self):
        time_taken=0
        for segment in self.segments:
            time_taken+=segment['time']
        return time_taken             
 
def get_input2():
    distance=float(input("Enter the distance"))
    time=float(input("Enter the time"))
    direction=int(input("Enter -1 for backward direction & +1 for forward direction"))
    return distance,direction,time

sim=Simulation()
n=int(input("How many parts does your journey have ?"))
for i in range (n):
    distance,direction,time=get_input2()
    sim.add_segments(distance,direction,time)

m=Motion(sim.total_distance(),sim.total_time(),0,sim.total_time(),0,sim.total_displacement())
m.summary()
animate_journey(sim)