"""! @file main.py

"""

import motor_driver
import encoder_reader
import clp_controller
import utime
import pyb

u2 = pyb.UART(2, baudrate=115200, timeout = 10000)

while(not u2.any()):
    pass

motor_dvr = motor_driver.MotorDriver() # creates a working motor
encoder = encoder_reader.EncoderReader() # creates a working encoder
controller = clp_controller.CLPController() # creates a working controller

u2.write(str(controller.setpoint).encode())
setpoint = u2.readline() 
kp = float(u2.readline())
controller.set_setpoint(setpoint)
controller.set_Kp(kp)

encoder.zero()
start_time = utime.ticks_ms()

for i in range(250):
    meas_pos = encoder.read()
    motor_dvr.set_duty_cycle(
        controller.run(int(controller.setpoint.decode()), meas_pos)
        )
    controller.times.append(utime.ticks_ms() - start_time)
    controller.motor_positions.append(meas_pos)
    
    u2.write(
        str(controller.times[i]).encode() + b", " 
        + str(controller.motor_positions[i]).encode() + b"\r\n"
        )
    utime.sleep_ms(50)
    
u2.write(b"Done!\r\n")    
motor_dvr.set_duty_cycle(0)

    


