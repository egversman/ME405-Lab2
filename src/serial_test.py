import serial
import csv
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
    with serial.Serial('COM4', 115200, timeout=10) as ser:

        for line in ser:
            try:
                data = line.readline().strip().split(b',')
                to_float(data[0])
                to_float(data[1])

            except ValueError:
                continue  # go to the next iteration of the loop
            else:
                x.append(float(data[0]))
                y.append(float(data[1]))
    return x, y

def generate_plot(x: list, y: list):
   # plt.plot(x, y)
    plt.xlabel('Time [sec? msec?]')
    plt.ylabel('Motor Position [Encoder Ticks?]')
    plt.scatter(x, y)
    plt.show()
    
    
if __name__ == "__main__":
    setpoint = str(input('Enter desired setpoint: '))
    Kp = str(input('Enter desired Kp: '))
    b_setpoint = setpoint.encode()
    b_Kp = Kp.encode()

    with serial.Serial('COM4', 115200, timeout = 10) as ser:
        ser.write(b_setpoint + b"\r\n")
        ser.write(b_Kp + b"\r\n")

    print('Controller parameters sent')

generate_plot(*process_data())

# runs step response tests
    # send characters through USB serial port to Micropython board
    # read the resulting data
    # plot the step response with correctly labeled axes and titles











                
