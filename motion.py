#Core Physics class
class Motion:
    def __init__(self):
        self.distance=float(input("Enter the distance"))
        self.total_time=float(input("Enter total time"))
        self.initial_time=float(input("Enter the time when the object was at initial position"))
        self.final_time=float(input("Enter the time at which the object waa at final position"))
        self.initial_position=float(input("Enter initial position"))
        self.final_position=float(input("Enter Final Position"))
    def get_displacement (self):
        return self.final_position-self.initial_position
    def get_delta_time(self):
        return self.final_time-self.initial_time
    def get_average_velocity(self):
        return self.get_displacement()/self.get_delta_time()
    def get_average_speed(self):
        return self.distance/self.total_time 
m=Motion()
print("Average Velocity:",m.get_average_velocity(),"m/s")
print("Average Speed:",m.get_average_speed(),"m/s")                