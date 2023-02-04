"""! @file clp_controller.py
   
   something about closed loop proportional control
  
"""
import pyb

class CLPController:
    """! 
    closed loop proportional control 
    """

    def __init__ (self, Kp = 1, setpoint = 0):
        """! 
        what it do 
        @param 
        @param 
        """
        self.Kp = Kp
        self.setpoint = setpoint
        
        self.times = list()
        self.motor_positions = list()
        
    def __repr__(self):
        return f'CLPController(Kp={self.Kp}, init_setpoint={self.init_setpoint})'
    
    def __str__(self):
        return f'Closed-loop proportional controller:\n\tKp={self.Kp} and\n\tinit_setpoint={self.init_setpoint}'

    def run (self, setpoint, meas_output):
        """!
        something about run
        @param 
        """
        self.motor_positions.append(meas_output)
        return self.Kp * (setpoint - meas_output)
    
    def set_setpoint(self, new_setpoint):
        """!
        something about set_setpoint
        @param 
        """
        self.setpoint = new_setpoint
    
    def set_Kp(self, new_Kp):
        """!
        something about set_Kp
        @param 
        """
        self.Kp = new_Kp
        
    def print_response(self):
        if not self.times or not self.motor_positions:
            print('No data available.')
            return
        
        for time, position in zip(self.times, self.motor_positions):
            print(f'{time}, {position}')
        
if __name__ == "__main__":
    pass
    
