import motor_driver
import encoder_reader
import clp_controller
import utime
import pyb

u2 = pyb.UART(2, baudrate=115200, timeout = 10000)
 
motor_dvr = motor_driver.MotorDriver() # creates a working motor
encoder = encoder_reader.EncoderReader() # creates a working encoder
controller = clp_controller.CLPController() # creates a working controller

u2.write(str(controller.setpoint).encode())

#while (not u2.any()):
#    pyb.delay(10)
#u2.write(b'setpoint please\r\n')

setpoint = u2.readline() #.strip()
#u2.write(b"enter kp\r\n")

kp = float(u2.readline())
#u2.write(b"ok\r\n")
controller.set_setpoint(setpoint)
controller.set_Kp(kp)


encoder.zero()
start_time = utime.ticks_ms()


for i in range(500):
    meas_pos = encoder.read()
    #u2.write("setpoint type: " + str(type(controller.setpoint)) + ", pos type: " + str(type(meas_pos)))
    motor_dvr.set_duty_cycle(controller.run(int(controller.setpoint.decode()), meas_pos))
    controller.times.append(utime.ticks_ms() - start_time)
    controller.motor_positions.append(meas_pos)
    u2.write(str(controller.times[i]).encode() + b", " + str(controller.motor_positions[i]).encode() + b"\r\n")
 
    utime.sleep_ms(50)
    
u2.write(b"Done!\r\n")    
motor_dvr.set_duty_cycle(0)
#u2 = pyb.UART(2, baudrate=115200, timeout = 10)

#for i in range(len(controller.motor_positions)):
#    u2.write(f'{controller.times[i]}, {control.motor_positions[i]}\r\n')
 #something up over here
    
    


