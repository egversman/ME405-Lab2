import motor_driver
import encoder_driver


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