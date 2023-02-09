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

    while True:
        line = ser.readline()

        if 'done' in line.lower():
            break

        data = split(line)
        if False in {data[0], data[1]}:
            print("problem")
        else:
            x.append(to_float(data[0]))
            y.append(to_float(data[1]))

        # continue_char = input(
        #     'Try new Kp (Enter y/n)? '
        #      )[0].lower()
        # ser.write(continue_char.encode())

    return x, y

def generate_plot(x: list, y: list):
    plt.plot(x, y)   
    plt.xlabel('Time [sec? msec?]')
    plt.ylabel('Motor Position [Encoder Ticks?]')
    plt.scatter(x, y)
    plt.show()
    
    
if __name__ == "__main__":
    b_setpoint = str(input('Enter desired setpoint: ')).encode()
    b_Kp = str(input('Enter desired Kp: ')).encode()

    with serial.Serial('COM3', 115200) as ser:
        ser.write(b_setpoint + b"\r\n")
        ser.write(b_Kp + b"\r\n")
    print('Controller parameters sent')

    generate_plot(*process_data())

# runs step response tests
    # send characters through USB serial port to Micropython board
    # read the resulting data
    # plot the step response with correctly labeled axes and titles











                
