import motor_driver
import encoder_reader
import clp_controller
# import serial_test
import utime
import pyb


u2 = pyb.UART(2, baudrate=115200, timeout = 10)
#u2.write when we want to write
 
motor_dvr = motor_driver.MotorDriver() # creates a working motor
encoder = encoder_reader.EncoderReader() # creates a working encoder
controller = clp_controller.CLPController() # creates a working controller
#continue_char = 'y'



u2.write(str(controller.setpoint).encode())



while (not u2.any()):
    pyb.delay(10)

setpoint = int(u2.readline().strip())
kp = float(u2.readline())

controller.set_setpoint(setpoint)
controller.set_Kp(kp)


encoder.zero()
start_time = utime.ticks_ms() 
    
for _ in range(5000):
    meas_pos = encoder.read()
    motor_dvr.set_duty_cycle(controller.run(controller.setpoint, meas_pos))
    
    controller.times.append(utime.ticks_ms() - start_time)
    controller.motor_positions.append(meas_pos)
    
    utime.sleep_ms(10000)
    
u2.write(controller.print_response().encode('utf-8')) #something up over here
    
    


