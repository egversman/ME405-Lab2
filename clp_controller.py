"""! @file clp_controller.py
   
   something about closed loop proportional control
  
"""
import pyb

class CLPController:
    """! 
    closed loop proportional control 
    """

    def __init__ (self, Kp, init_set_point):
        """! 
        what it do 
        @param 
        @param 
        """
        self.Kp = 1
        self.init_set_point = 0
        
        self.times = list()
        self.motor_positions = list()
        
    def __repr__(self):
        pass

    def __str__(self):
        pass

        
    def run (self, set_point, meas_output):
        """!
        something about run
        @param 
        """
        return self.Kp * (set_point - meas_output)
    
    def set_setpoint(self, new_set_point):
        """!
        something about set_setpoint
        @param 
        """
        self.set_point = new_set_point
    
    def set_Kp(self, new_Kp):
        """!
        something about set_Kp
        @param 
        """
        self.Kp = new_Kp

        
if __name__ == "__main__":
    pass
    
