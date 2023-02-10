import serial
from matplotlib import pyplot as plt

split = lambda line: line.strip().split(b',')[:2]

def to_float(num: str):
    try:
        return float(num)
    except:
        return False

def process_data(): #comment2
    x = []
    y = []
    data = []
    with serial.Serial('COM4', 115200, timeout=10) as ser:

        while "False":
            line = ser.readline() #.strip()
            #print(line)

            if b"done" in line.lower():
                break

            data = split(line)

            if False in {data[0], data[1]}:
                print(b"problem, idiot!")
            else:
                x.append(float(data[0]))
                y.append(float(data[1]))

    return x, y

def generate_plot(x: list, y: list):
    plt.plot(x, y, linestyle='-')
    plt.xlabel('Time [msec]')
    plt.ylabel('Motor Position [Encoder Ticks]')
    #plt.scatter(x, y)
    plt.show()

if __name__ == "__main__":
    setpoint = str(input('Enter desired setpoint: '))
    Kp = str(input('Enter desired Kp: '))
    b_setpoint = setpoint.encode()
    b_Kp = Kp.encode()

    with serial.Serial('COM4', 115200, timeout = 1000) as ser:
        ser.write(b_setpoint + b"\r\n")
        ser.write(b_Kp + b"\r\n")

        # print('Controller parameters sent')
    x, y = process_data()
    generate_plot(x, y)













