#physics core
class Motion:
    def __init__(self,distance,total_time,initial_time,final_time,initial_position,final_position):
        self.distance=distance
        self.total_time=total_time
        self.initial_time=initial_time
        self.final_time=final_time
        self.initial_position=initial_position
        self.final_position=final_position

    def get_displacement (self):
        return self.final_position-self.initial_position

    def get_delta_time(self):
        return self.final_time-self.initial_time

    def get_average_velocity(self):
        delta_t=self.get_delta_time()
        if delta_t==0:
            raise ValueError("Time Interval cannot be 0")
        return self.get_displacement()/delta_t

    def get_average_speed(self):
        if self.total_time==0:
            raise ValueError("Total Time cannot be 0")
        return self.distance/self.total_time

    def summary(self):
        print(f"Average Velocity:{self.get_average_velocity():.2f}m/s")
        print(f"Average Speed:{self.get_average_speed():.2f}m/s")

    @staticmethod    
    def get_inputs():
        distance         = float(input("Enter total distance traveled (m)         : "))
        total_time       = float(input("Enter total time taken (s)                : "))
        initial_time     = float(input("Enter initial time (s)                    : "))
        final_time       = float(input("Enter final time (s)                      : "))
        initial_position = float(input("Enter initial position (m)                : "))
        final_position   = float(input("Enter final position (m)                  : "))
        return Motion(distance, total_time, initial_time, final_time, initial_position, final_position)

if __name__=='__main__':
    m=Motion.get_inputs()
    m.summary()