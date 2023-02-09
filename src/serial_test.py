import serial

from matplotlib import pyplot as plt

split = lambda line: line.strip().split(b',')[:2]

# add user input lines
# convert inputs
# using the same serial info below, serial.write()

def to_float(num: str):
        try:
            return float(num)
        except:
            return False

def process_data():
    x = []
    y = []
    data = []

    with serial.Serial ('COM3', 115200) as ser:
        prev_setpoint = ser.readline().decode()
        setpoint = float(input(
            f'Enter desired setpoint (default setpoint is {prev_setpoint}): '
            ))
        ser.write(setpoint.encode())
        
        prev_Kp = ser.readline().decode()
        Kp = float(input(f'Enter new Kp (current Kp is {prev_Kp}): '))
        ser.write(Kp.encode())
        # ser.write (b'0.1\r\n') # Write bytes, not a string
        # every line through loop reads a new line
        while True: # use an exception from last line to breakout
            line = ser.readline()
            
            if 'done' in line.lower():
                break
            
            data = split(line) # results in a string
            if False in {data[0], data[1]}:
                print("problem")
            else:
                x.append(to_float(data[0]))
                y.append(to_float(data[1]))
                
            continue_char = input(
                'Try new Kp (Enter y/n)? '
                 )[0].lower()
            ser.write(continue_char.encode())
         
    ser.close()
    return x, y

def generate_plot(x: list, y: list):
    x, y = process_data()
    
    plt.plot(x, y)   
    plt.xlabel('Time [sec? msec?]')
    plt.ylabel('Motor Position [Encoder Ticks?]')
    plt.scatter(x, y)
    plt.show()
    
    
if __name__ == "__main__":
    generate_plot(*process_data())

# runs step response tests
    # send characters through USB serial port to Micropython board
    # read the resulting data
    # plot the step response with correctly labeled axes and titles











                
