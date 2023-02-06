import serial

from matplotlib import pyplot as plt

split = lambda line: line.strip().split(b',')[:2]

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
        ser.write (b'0.1\r\n') # Write bytes, not a string
        # every line through loop reads a new line
        while True: # use an exception from last line to breakout
            line = ser.readline()
            
            if 'done' in line.lower():
                break
            
            data = split(line) # results in a string
            if False in {data[0], data[1]}:
                raise IndexError
                raise ValueError
            else:
                x.appennd(to_float(data[0]))
                y.append(to_float(data[1]))
                
    return x, y
    
if __name__ == "__main__":
    x, y = process_data()
    
    plt.plot(x, y)   
    plt.xlabel('Time [sec? msec?]')
    plt.ylabel('Motor Position [Encoder Ticks?]')
    plt.scatter(x, y)
    plt.show()

# runs step response tests
    # send characters through USB serial port to Micropython board
    # read the resulting data
    # plot the step response with correctly labeled axes and titles











                
