import motor_driver
import encoder_reader
import clp_controller
import serial_test
import utime
 
motor_dvr = motor_driver.MotorDriver()
encoder = encoder_reader.EncoderReader()
controller = clp_controller.CLPController()
continue_char = 'y'

while continue_char == 'y':
    encoder.zero()
    
    controller.set_Kp(
        input(
            'Enter new Kp (current Kp is {controller.Kp}): '
            )
        )
    controller.set_setpoint(
        input(
            'Enter new setpoint (current setpoint is {controller.setpoint}): '
            )
        )
      
    for _ in range(100):
        motor_dvr.set_duty_cycle(controller.run())
        utime.ticks_ms(1)

    continue_char = input(
        'Try new controller parameters (Enter y/n)? '
        )[0].lower()


#initialize motor driver
#initialize encoder driver
#initialize controller
#loop to test different setpoints
    #call endcoder driver to set current position of motor to zero
    #call setpoint method in controller class to get a new setpoint
    #call run method in controller class to get the actuation value
    #call set duty cycle in motor driver using actuation value to move motor
    #utime.sleep.ms(10)

# motor_dvr = motor_driver.MotorDriver()
# encoder = encoder_reader.EncoderReader()
# controller = clp_controller.CLPController()
    # Set controller Kp and set point
    # controller.setKp = ()
    # controller.set_setpoint()
# encoder.zero()
# while controller.Kp:
#     controller.run()


#pseudo line 9 = actVal = controller.run(setpoint, currPos)
#pseudo line 3 = moe = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)


#initialize motor driver
#initialize encoder driver
#initialize controller
#loop to test different setpoints
    #call endcoder driver to set current position of motor to zero
    #call setpoint method in controller class to get a new setpoint
    #call run method in controller class to get the actuation value
    #call set duty cycle in motor driver using actuation value to move motor
    #utime.sleep.ms(10)


#pseudo line 9 = actVal = controller.run(setpoint, currPos)
#pseudo line 3 = moe = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)

#pseudo line 10 = moe.set_duty_cycle(actVal)