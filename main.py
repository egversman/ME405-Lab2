import motor_driver

actVal = controller.run(setpoint, currPos)
moe = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
moe.set_duty_cycle(actVal)