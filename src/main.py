import motor_driver
import encoder_reader
import clp_controller
#import serial_test
import utime
import pyb
 
u2 = pyb.UART(2, baudrate=115200)
#u2.write when we want to write
 
motor_dvr = motor_driver.MotorDriver()
encoder = encoder_reader.EncoderReader()
controller = clp_controller.CLPController()
continue_char = 'y'

controller.set_setpoint(
        # input() may not work on UART, try u2.readline()
        # must convert string to byte array or bytes object before write()
        float(input(
            f'Enter desired setpoint (default setpoint is {controller.setpoint}): '
            ))
        )

# while(not serial.any()):
#    delay()
# readline() setpoint
# readline() KP


while continue_char == 'y':
    encoder.zero()
    start_time = utime.ticks_ms()
    controller.set_Kp(
        float(input(
            f'Enter new Kp (current Kp is {controller.Kp}): '
            ))
        )
    
    for _ in range(500):
        meas_pos = encoder.read()
        motor_dvr.set_duty_cycle(controller.run(controller.setpoint, meas_pos))
        controller.times.append(utime.ticks_ms() - start_time)
        controller.motor_positions.append(meas_pos)
        utime.sleep_ms(10)
        
        u2.write(controller.print_response())
    
    continue_char = input(
        'Try new controller parameters (Enter y/n)? '
        )[0].lower()
    
u2.write(controller.print_response())


